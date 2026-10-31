"""Offline analysis: metrics.csv, sentence families (local clustering), summary.md. No API calls."""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

from .metrics import mean_sd, read_jsonl_gz, seed_metrics, write_csv

ROOT = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------- clustering
def _char_ngrams(s: str, lo=3, hi=5) -> Counter:
    s = " " + re.sub(r"\s+", " ", s.lower()) + " "
    c = Counter()
    for n in range(lo, hi + 1):
        for i in range(len(s) - n + 1):
            c[s[i:i + n]] += 1
    return c


def cluster_sentences(texts_with_weight: dict[str, int], threshold: float = 0.5) -> list[dict]:
    """TF-IDF over char 3-5 grams, cosine similarity, greedy leader clustering by frequency."""
    texts = sorted(texts_with_weight, key=lambda t: (-texts_with_weight[t], t))
    if not texts:
        return []
    grams = [_char_ngrams(t) for t in texts]
    df = Counter()
    for g in grams:
        df.update(g.keys())
    vocab = {k: i for i, k in enumerate(df)}
    N = len(texts)
    idf = np.zeros(len(vocab))
    for k, i in vocab.items():
        idf[i] = math.log((1 + N) / (1 + df[k])) + 1
    M = np.zeros((N, len(vocab)), dtype=np.float32)
    for r, g in enumerate(grams):
        for k, c in g.items():
            M[r, vocab[k]] = (1 + math.log(c)) * idf[vocab[k]]
    M /= np.linalg.norm(M, axis=1, keepdims=True) + 1e-9
    leaders: list[int] = []
    assign = [-1] * N
    for i in range(N):
        if leaders:
            sims = M[leaders] @ M[i]
            j = int(np.argmax(sims))
            if sims[j] >= threshold:
                assign[i] = j
                continue
        assign[i] = len(leaders)
        leaders.append(i)
    fams = defaultdict(lambda: {"weight": 0, "members": []})
    for i, c in enumerate(assign):
        fams[c]["weight"] += texts_with_weight[texts[i]]
        fams[c]["members"].append((texts_with_weight[texts[i]], texts[i]))
    out = []
    for c, f in fams.items():
        f["members"].sort(key=lambda t: -t[0])
        out.append({"leader": texts[leaders[c]], "weight": f["weight"], "n_variants": len(f["members"]),
                    "top_variants": f["members"][:3]})
    out.sort(key=lambda f: -f["weight"])
    return out


# ---------------------------------------------------------------- helpers
def seed_dirs(results: Path) -> list[Path]:
    return sorted([p for p in results.glob("seed-*") if p.is_dir()], key=lambda p: int(p.name.split("-")[1]))


def final_gen(rows, seed):
    gens = [r["generation"] for r in rows if r["seed"] == seed]
    return max(gens) if gens else None


def _fmt(m, s):
    return "n/a" if m != m else f"{m:+.3f} ± {s:.3f}"


def example_encounters(seed_dir: Path, k: int = 3) -> list[dict]:
    """Mechanical pick from the main story seed's final generation: first mutual GIVE, first broken
    promise where a GIVE-declarer TAKEs, and first encounter from the LAMARCK population (else any)."""
    encs = list(read_jsonl_gz(seed_dir / "encounters.jsonl.gz"))
    if not encs:
        return []
    last = max(e["gen"] for e in encs)
    fin = [e for e in encs if e["gen"] == last]
    picks = []
    rules = [
        lambda e: e["a"]["action"] == "GIVE" and e["b"]["action"] == "GIVE",
        lambda e: any(s["declare"] == "GIVE" and s["action"] == "TAKE" for s in (e["a"], e["b"])),
        lambda e: e["pop"] == "LAMARCK",
        lambda e: True,
    ]
    for rule in rules:
        for e in fin + encs:
            if rule(e) and e not in picks:
                picks.append(e)
                break
        if len(picks) >= k:
            break
    return picks[:k]


# ---------------------------------------------------------------- main
def analyze(results: Path = ROOT / "results") -> str:
    cfg = json.loads((ROOT / "config" / "frozen.json").read_text())
    rows = []
    sds = seed_dirs(results)
    for sd in sds:
        rows += seed_metrics(sd)
    write_csv(rows, results / "metrics.csv")
    pops = cfg["populations"]
    seeds = sorted({r["seed"] for r in rows})
    L = ["# Prompt DNA — results summary", ""]
    locked = ROOT / "config" / "locked.json"
    if locked.exists():
        lk = json.loads(locked.read_text())
        L.append(f"Player model: `{lk['player_model']}`, generations per seed: {lk['generations']}, "
                 f"seeds analysed: {seeds}.")
    L.append("All numbers below are computed mechanically from `results/seed-*/` logs (no LLM judge).")
    L.append("")

    # main metric
    L += ["## Main metric: benchmark payoff per encounter (survivors vs fixed opponents)", "",
          "Final generation of each seed; mean ± sd across seeds. Also mean over the last 5 generations.", "",
          "| population | final gen (mean ± sd over seeds) | last-5-gen mean ± sd | per seed (final gen) |",
          "|---|---|---|---|"]
    winners = {}
    for p in pops:
        fin, last5, per = [], [], []
        for s in seeds:
            fg = final_gen(rows, s)
            r = [x for x in rows if x["seed"] == s and x["population"] == p]
            f = [x["bench_mean"] for x in r if x["generation"] == fg]
            l5 = [x["bench_mean"] for x in r if x["generation"] > fg - 5 and x["bench_mean"] is not None]
            if f and f[0] is not None:
                fin.append(f[0])
                per.append(f"{f[0]:+.2f}")
            if l5:
                last5.append(sum(l5) / len(l5))
        winners[p] = mean_sd(fin)[0]
        L.append(f"| {p} | {_fmt(*mean_sd(fin))} | {_fmt(*mean_sd(last5))} | {' '.join(per)} |")
    L.append("")
    per_seed_winner = []
    for s in seeds:
        fg = final_gen(rows, s)
        cand = {x["population"]: x["bench_mean"] for x in rows if x["seed"] == s and x["generation"] == fg}
        if cand and all(v is not None for v in cand.values()):
            per_seed_winner.append(max(cand, key=cand.get))
    if per_seed_winner:
        L.append(f"Winner per seed (final generation): {', '.join(f'seed {s}: {w}' for s, w in zip(seeds, per_seed_winner))}.")
        L.append("")

    # secondary
    L += ["## Secondary metrics (final generation, mean ± sd across seeds)", "",
          "| population | coop rate | TAKE rate | broken promise | genome words | novel words / genome | distinct sentence IDs | invalid rate |",
          "|---|---|---|---|---|---|---|---|"]
    for p in pops:
        def col(key):
            xs = []
            for s in seeds:
                fg = final_gen(rows, s)
                xs += [x[key] for x in rows if x["seed"] == s and x["population"] == p and x["generation"] == fg]
            return _fmt(*mean_sd(xs))
        L.append(f"| {p} | {col('coop_rate')} | {col('take_rate')} | {col('broken_promise_rate')} | "
                 f"{col('genome_words_mean')} | {col('novel_words_mean')} | {col('sentence_ids_distinct')} | {col('invalid_rate')} |")
    L.append("")

    # trajectory
    L += ["## Trajectory (mean over seeds)", "",
          "| gen | " + " | ".join(f"{p} bench" for p in pops) + " | " + " | ".join(f"{p} TAKE" for p in pops) + " |",
          "|---|" + "---|" * (2 * len(pops))]
    gens = sorted({r["generation"] for r in rows})
    for g in gens:
        cells = []
        for key in ("bench_mean", "take_rate"):
            for p in pops:
                xs = [x[key] for x in rows if x["population"] == p and x["generation"] == g and x[key] is not None]
                cells.append(f"{sum(xs) / len(xs):+.2f}" if xs else "")
        shock = any(x["shocked"] for x in rows if x["generation"] == g)
        L.append(f"| {g}{' (shock)' if shock else ''} | " + " | ".join(cells) + " |")
    L.append("")

    # prediction vs measurement
    pred_path = ROOT / "predict.json"
    if pred_path.exists() and rows:
        pred = json.loads(pred_path.read_text())
        L += ["## Prediction vs measurement", ""]
        measured_winner = max(winners, key=lambda p: winners[p] if winners[p] == winners[p] else -1e9)
        L.append(f"- Main-metric winner: predicted **{pred['main_metric_winner']}**, measured **{measured_winner}** "
                 f"(mean over seeds, final generation).")
        for p in pops:
            xs = []
            for s in seeds:
                fg = final_gen(rows, s)
                xs += [x["take_rate"] for x in rows if x["seed"] == s and x["population"] == p and x["generation"] == fg]
            m, sd = mean_sd(xs)
            L.append(f"- Final TAKE rate {p}: predicted {pred['final_take_rate'][p]:.2f}, measured {m:.2f} ± {sd:.2f}.")
        pw = []
        for s in seeds:
            fg = final_gen(rows, s)
            for x in rows:
                if x["seed"] == s and x["generation"] == fg and x["password_emerged"]:
                    pw.append(f"seed {s} {x['population']}: \"{x['password_phrase']}\" "
                              f"(msgs {x['password_msg_share']:.0%}, genomes {x['password_genome_share']:.0%})")
        L.append(f"- Password phrase: predicted {'yes' if pred['password_emerges'] else 'no'}; measured "
                 f"{'yes — ' + '; '.join(pw) if pw else 'no (pre-registered 30%/30% rule never met in a final generation)'}.")
        for p in ("DARWIN", "LAMARCK"):
            xs = []
            for s in seeds:
                fg = final_gen(rows, s)
                xs += [x["genome_words_mean"] for x in rows if x["seed"] == s and x["population"] == p and x["generation"] == fg]
            m, sd = mean_sd(xs)
            L.append(f"- Genome length {p}: predicted {pred['genome_length'][p]}, measured {m:.1f} ± {sd:.1f} words at the "
                     f"final generation (start: 1 word).")
        L.append("")

    # sentence families
    weights = Counter()
    for sd in sds:
        for gp in sorted((sd / "genomes").glob("gen-*.json")):
            for pop, agents in json.loads(gp.read_text()).items():
                for a in agents:
                    for s in a["genome"]["sentences"]:
                        weights[s["text"]] += 1
    fams = cluster_sentences(dict(weights))
    L += ["## 8 largest sentence families", "",
          "Offline clustering: TF-IDF over character 3–5-grams, cosine ≥ 0.5, greedy leader clustering by frequency. "
          "Weight = number of (agent, generation) occurrences across all seeds and populations.", "",
          "| # | weight | variants | leader sentence | other frequent variants |", "|---|---|---|---|---|"]
    for i, f in enumerate(fams[:8], 1):
        other = " / ".join(f"“{t}” ({w})" for w, t in f["top_variants"][1:3])
        L.append(f"| {i} | {f['weight']} | {f['n_variants']} | “{f['leader']}” | {other} |")
    L.append("")
    (results / "sentence_families.json").write_text(json.dumps(fams[:50], indent=1, ensure_ascii=False))

    # examples
    if sds:
        main_seed = cfg["main_story_seed"]
        msd = results / f"seed-{main_seed}"
        ex = example_encounters(msd) if msd.exists() else []
        L += [f"## 3 example encounters (seed {main_seed})", ""]
        for i, e in enumerate(ex, 1):
            L.append(f"**{i}. {e['pop']}, generation {e['gen']}, round {e['round'] + 1} ({e['currency']})**")
            L.append("")
            for side in ("a", "b"):
                s = e[side]
                L.append(f"- {s['agent']}: declared **{s['declare']}** “{s['message']}” → action **{s['action']}** → "
                         f"payoff {s['payoff']:+g}{' (exposed)' if s['exposed'] else ''}")
            L.append("")

    # refusals / moralizing
    L += ["## Refusals and moralizing (findings, not retried)", ""]
    for p in pops:
        r = [x for x in rows if x["population"] == p]
        L.append(f"- {p}: refusals {sum(x['refusals'] for x in r)}, messages with moralizing language "
                 f"{sum(x['moralizing_msgs'] for x in r)}, with refusal language {sum(x['refusal_language_msgs'] for x in r)}.")
    L.append("")
    text = "\n".join(L) + "\n"
    (results / "summary.md").write_text(text)
    return text
