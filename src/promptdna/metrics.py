"""Mechanical metrics from the result logs. No model calls, no LLM judge."""
from __future__ import annotations

import csv
import gzip
import json
import math
import re
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
STOPWORDS = set("""a an the and or but if then else of to in on at by for with from as is are be been was were
i you we they he she it me my your our their this that these those not no do does did will would can could
should shall may might must so than too very just only also all any some each every one two three when what
who whom which where why how up down out over under again here there now its it's i'm you're let let's""".split())


@lru_cache(maxsize=1)
def wordlist() -> frozenset:
    with gzip.open(ROOT / "data" / "wordlist-web2.txt.gz", "rt") as f:
        return frozenset(w.strip() for w in f if w.strip())


GAME_TERMS = {"glim", "vorn", "give", "ask", "take", "gives", "takes", "asks"}


def novel_words(text: str) -> set[str]:
    wl = wordlist()
    out = set()
    for w in WORD_RE.findall(text or ""):
        lw = w.lower()
        base = lw[:-2] if lw.endswith("'s") else lw
        if base in wl or base in GAME_TERMS:
            continue
        # simple inflection handling so ordinary plurals/verb forms are not counted as new
        if any(base.endswith(suf) and base[: -len(suf)] in wl for suf in ("s", "es", "ed", "ing", "ly", "er", "est", "d")):
            continue
        out.add(lw)
    return out


def read_jsonl_gz(path: Path):
    if not path.exists():
        return
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def ngrams(text: str, n: int) -> set[tuple]:
    w = [x.lower() for x in WORD_RE.findall(text or "")]
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def password_check(messages: list[str], genomes: list[str], threshold: float = 0.30) -> dict:
    """Pre-registered rule: a 2-4 gram (not all stopwords) in >=30% of messages AND >=30% of genomes."""
    best = None
    if not messages or not genomes:
        return {"emerged": False, "phrase": None, "msg_share": 0.0, "genome_share": 0.0}
    cm, cg = Counter(), Counter()
    for m in messages:
        for n in (2, 3, 4):
            cm.update(ngrams(m, n))
    for g in genomes:
        for n in (2, 3, 4):
            cg.update(ngrams(g, n))
    for gram, c in cm.items():
        if all(t in STOPWORDS for t in gram):
            continue
        ms, gs = c / len(messages), cg.get(gram, 0) / len(genomes)
        cand = (min(ms, gs), ms, gs, " ".join(gram))
        if best is None or cand > best:
            best = cand
    if best is None:
        return {"emerged": False, "phrase": None, "msg_share": 0.0, "genome_share": 0.0}
    return {"emerged": best[0] >= threshold, "phrase": best[3], "msg_share": round(best[1], 4),
            "genome_share": round(best[2], 4)}


def simpson(counter: Counter) -> float:
    n = sum(counter.values())
    if n == 0:
        return 0.0
    return 1.0 - sum((c / n) ** 2 for c in counter.values())


def seed_metrics(seed_dir: Path) -> list[dict]:
    """One row per (seed, population, generation)."""
    agg = defaultdict(lambda: {"n": 0, "give": 0, "take": 0, "ask": 0, "broken": 0, "mutual_give": 0,
                               "pairs": 0, "invalid": 0, "calls": 0, "refusal": 0, "moral": 0, "refusal_lang": 0,
                               "msg_trunc": 0, "payoff_sum": 0.0, "exposed": 0, "messages": []})
    for e in read_jsonl_gz(seed_dir / "encounters.jsonl.gz"):
        k = (e["seed"], e["pop"], e["gen"])
        a = agg[k]
        a["pairs"] += 1
        a["mutual_give"] += e["a"]["action"] == "GIVE" and e["b"]["action"] == "GIVE"
        for s in (e["a"], e["b"]):
            a["n"] += 1
            a["give"] += s["action"] == "GIVE"
            a["take"] += s["action"] == "TAKE"
            a["ask"] += s["action"] == "ASK"
            a["broken"] += s["declare"] != s["action"]
            a["calls"] += 2
            a["invalid"] += (not s["valid_declare"]) + (not s["valid_action"])
            a["refusal"] += sum(r == "refusal" for r in s["invalid_reasons"])
            a["moral"] += "moralizing_language" in s["flags"]
            a["refusal_lang"] += "refusal_language" in s["flags"]
            a["msg_trunc"] += "msg_truncated" in s["flags"]
            a["payoff_sum"] += s["payoff"]
            a["exposed"] += bool(s["exposed"])
            a["messages"].append(s["message"])

    bench = defaultdict(list)
    bench_opp = defaultdict(lambda: defaultdict(list))
    for b in read_jsonl_gz(seed_dir / "benchmark.jsonl.gz"):
        k = (b["seed"], b["pop"], b["gen"])
        bench[k].append(b["score"])
        for r in b["encounters"]:
            bench_opp[k][r["opponent"]].append(r["payoff"])

    mut = defaultdict(Counter)
    for m in read_jsonl_gz(seed_dir / "mutations.jsonl.gz"):
        mut[(m["seed"], m["pop"], m["gen"])][m["edit"]["op"] if m["edit"] else "none"] += 1
        for f in m["flags"]:
            mut[(m["seed"], m["pop"], m["gen"])]["flag:" + f] += 1

    shocked_by_gen = {}
    gl = seed_dir / "generations.jsonl"
    if gl.exists():
        for line in gl.read_text().splitlines():
            d = json.loads(line)
            shocked_by_gen[d["gen"]] = d["shocked"]

    rows = []
    for gpath in sorted((seed_dir / "genomes").glob("gen-*.json")):
        gen_genomes = json.loads(gpath.read_text())
        gen = int(gpath.stem.split("-")[1])
        for pop, agents in gen_genomes.items():
            seed = int(seed_dir.name.split("-")[-1])
            k = (seed, pop, gen)
            a = agg.get(k)
            if a is None:
                continue
            texts = [x["genome"]["text"] for x in agents]
            sids = Counter(s["id"] for x in agents for s in x["genome"]["sentences"])
            nw = [novel_words(t) for t in texts]
            union_novel = set().union(*nw) if nw else set()
            surv_texts = [x["genome"]["text"] for x in agents if x["fate"] != "dies"]
            pw = password_check(a["messages"], surv_texts or texts)
            bscores = bench.get(k, [])
            row = {
                "seed": seed, "population": pop, "generation": gen, "shocked": shocked_by_gen.get(gen),
                "bench_mean": round(sum(bscores) / len(bscores), 4) if bscores else None,
                "bench_n": len(bscores),
                **{f"bench_vs_{o.lower()}": round(sum(v) / len(v), 4) for o, v in sorted(bench_opp[k].items())},
                "fitness_mean": round(a["payoff_sum"] / a["n"], 4),
                "coop_rate": round(a["give"] / a["n"], 4),
                "mutual_give_rate": round(a["mutual_give"] / a["pairs"], 4),
                "take_rate": round(a["take"] / a["n"], 4),
                "ask_rate": round(a["ask"] / a["n"], 4),
                "broken_promise_rate": round(a["broken"] / a["n"], 4),
                "exposed_rate": round(a["exposed"] / a["n"], 4),
                "genome_words_mean": round(sum(len(t.split()) for t in texts) / len(texts), 2),
                "genome_words_max": max(len(t.split()) for t in texts),
                "genome_sentences_mean": round(sum(len(x["genome"]["sentences"]) for x in agents) / len(agents), 2),
                "novel_words_mean": round(sum(len(x) for x in nw) / len(nw), 3),
                "novel_words_distinct": len(union_novel),
                "novel_words_examples": " ".join(sorted(union_novel)[:10]),
                "sentence_ids_distinct": len(sids),
                "sentence_id_simpson": round(simpson(sids), 4),
                "sentence_id_top_share": round(max(sids.values()) / len(agents), 4) if sids else 0,
                "distinct_genomes": len(set(texts)),
                "invalid_rate": round(a["invalid"] / a["calls"], 4),
                "refusals": a["refusal"],
                "moralizing_msgs": a["moral"],
                "refusal_language_msgs": a["refusal_lang"],
                "msg_truncated": a["msg_trunc"],
                "password_phrase": pw["phrase"],
                "password_msg_share": pw["msg_share"],
                "password_genome_share": pw["genome_share"],
                "password_emerged": pw["emerged"],
                "mutations": json.dumps(dict(mut.get(k, {}))),
            }
            rows.append(row)
    return rows


def write_csv(rows: list[dict], path: Path):
    if not rows:
        path.write_text("")
        return
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def mean_sd(xs: list[float]) -> tuple[float, float]:
    xs = [x for x in xs if x is not None]
    if not xs:
        return float("nan"), float("nan")
    m = sum(xs) / len(xs)
    if len(xs) < 2:
        return m, 0.0
    return m, math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
