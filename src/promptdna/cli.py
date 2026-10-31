"""Command line: fake-run | pilot | decide | run | analyze | sha."""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import shutil
import sys
import time
from pathlib import Path

from .engine import InvalidRateStop, SeedRun, _write_jsonl_gz
from .llm import AdaptiveLimiter, AnthropicBackend, Budget, BudgetExceeded, FakeBackend, FatalAPIError, Gateway

ROOT = Path(__file__).resolve().parents[2]
CFG_PATH = ROOT / "config" / "frozen.json"
LEDGER = ROOT / "results" / "budget_ledger.json"

EXIT_BUDGET, EXIT_FATAL, EXIT_INVALID, EXIT_TIMEOUT = 3, 4, 5, 6


def load_cfg() -> dict:
    return json.loads(CFG_PATH.read_text())


def cfg_sha256() -> str:
    return hashlib.sha256(CFG_PATH.read_bytes()).hexdigest()


def real_backend(cfg):
    """Anthropic backend; PROMPTDNA_FAKE=1 swaps in the offline fake (pipeline dry-runs only)."""
    import os
    if os.environ.get("PROMPTDNA_FAKE") == "1":
        return FakeBackend()
    return AnthropicBackend(cfg["model_params"])


def make_gateway(cfg, backend, budget) -> Gateway:
    c = cfg["concurrency"]
    return Gateway(backend=backend, budget=budget, limiter=AdaptiveLimiter(c["start"], c["min"], c["max"]))


def _flush_aborted(gw: Gateway, path: Path):
    recs = gw.log.drain()
    if recs:
        _write_jsonl_gz(path, recs)
    gw.budget.save()


# ---------------------------------------------------------------- fake
def cmd_fake_run(a):
    cfg = load_cfg()
    out = Path(a.out)
    if out.exists():
        shutil.rmtree(out)
    budget = Budget(a.budget, cfg["prices_per_mtok"], out / "budget_ledger.json")
    gw = make_gateway(cfg, FakeBackend(invalid_prob=a.invalid_prob, throttle_prob=a.throttle_prob, seed=a.seed), budget)
    gw.backoff_base = 0.001
    run = SeedRun(seed=a.seed, cfg=cfg, n_gens=a.gens, player_model=a.player, gateway=gw,
                  out_dir=out / f"seed-{a.seed}", log_path=out / "logs" / f"seed-{a.seed}.jsonl.gz")
    s = asyncio.run(run.run())
    print(json.dumps({"generations": len(s), "spent_usd": round(budget.spent, 4), "calls": budget.n_calls}))


# ---------------------------------------------------------------- pilot
async def _pilot_one(cfg, model, budget, minutes_left):
    gw = make_gateway(cfg, real_backend(cfg), budget)
    out = ROOT / "results" / "pilot" / model
    if out.exists():
        shutil.rmtree(out)
    log = ROOT / "logs" / f"pilot-{model}.jsonl.gz"
    if log.exists():
        log.unlink()
    run = SeedRun(seed=0, cfg=cfg, n_gens=1, player_model=model, gateway=gw, out_dir=out, log_path=log, tag="pilot")
    spent0 = budget.spent
    t0 = time.time()
    status = "ok"
    try:
        await asyncio.wait_for(run.run(resume=False), timeout=max(60, minutes_left * 60))
    except BudgetExceeded as e:
        status = f"budget_stop: {e}"
    except InvalidRateStop as e:
        status = f"invalid_rate_stop: {e}"
    except asyncio.TimeoutError:
        status = "timeout"
    finally:
        _flush_aborted(gw, ROOT / "logs" / f"pilot-{model}.aborted.jsonl.gz")
    elapsed = time.time() - t0
    # measure from the call logs (complete + aborted)
    from .metrics import read_jsonl_gz
    recs = list(read_jsonl_gz(log)) + list(read_jsonl_gz(ROOT / "logs" / f"pilot-{model}.aborted.jsonl.gz"))
    player = [r for r in recs if r["kind"] in ("declare", "action")]
    muts = [r for r in recs if r["kind"] == "mutate"]
    from . import game
    inv = ref = 0
    for r in player:
        if r["kind"] == "declare":
            p = game.parse_declare(r["response_text"], r["stop_reason"], cfg["game"]["declare_max_words"])
        else:
            p = game.parse_action(r["response_text"], r["stop_reason"])
        inv += (not p["valid"]) or bool(r["error"])
        ref += r["stop_reason"] == "refusal"
    evolving_player = [r for r in player if r["pop"] in ("DARWIN", "LAMARCK")]
    span = (gw.stats["t_last"] or t0) - (gw.stats["t_first"] or t0)
    return {
        "model": model, "status": status, "elapsed_s": round(elapsed, 1),
        "cost_usd": round(budget.spent - spent0, 4),
        "player_calls": len(player), "player_cost_usd": round(sum(r["cost_usd"] for r in player), 4),
        "player_cost_per_call": sum(r["cost_usd"] for r in player) / max(1, len(player)),
        "player_in_tokens_per_call": sum((r["usage"] or {}).get("input_tokens") or 0 for r in player) / max(1, len(player)),
        "player_out_tokens_per_call": sum((r["usage"] or {}).get("output_tokens") or 0 for r in player) / max(1, len(player)),
        "player_calls_per_popgen": len(player) / 3, "evolving_player_calls": len(evolving_player),
        "mutation_calls": len(muts), "mutation_cost_usd": round(sum(r["cost_usd"] for r in muts), 4),
        "mutation_cost_per_child": sum(r["cost_usd"] for r in muts) / 16 if muts else None,
        "invalid": inv, "invalid_rate": inv / max(1, len(player)), "refusals": ref,
        "refusal_rate": ref / max(1, len(player)),
        "calls_per_s": round((len(player) + len(muts)) / span, 2) if span > 0 else None,
        "throttled": gw.stats["throttled"], "api_errors": gw.stats["errors"],
        "max_concurrency_reached": gw.limiter.max_seen,
    }


def cmd_pilot(a):
    cfg = load_cfg()
    base = Budget(cfg["budget"]["total_usd"], cfg["prices_per_mtok"], LEDGER)
    pilot_limit = min(cfg["budget"]["total_usd"], base.spent + cfg["budget"]["pilot_usd"])
    budget = Budget(pilot_limit, cfg["prices_per_mtok"], LEDGER)
    t_start = time.time()
    reports = []
    for model in cfg["player"]["candidates"]:  # haiku first, then sonnet (frozen order)
        left = cfg["budget"]["pilot_minutes"] - (time.time() - t_start) / 60
        try:
            rep = asyncio.run(_pilot_one(cfg, model, budget, left))
        except FatalAPIError as e:
            budget.save()
            print(f"FATAL: {e}", file=sys.stderr)
            return EXIT_FATAL
        reports.append(rep)
        print(json.dumps(rep, indent=1))
    budget.save()
    out = {"config_sha256": cfg_sha256(), "pilot_budget_usd": cfg["budget"]["pilot_usd"],
           "pilot_spent_usd": round(sum(r["cost_usd"] for r in reports), 4),
           "elapsed_min": round((time.time() - t_start) / 60, 2), "reports": reports}
    (ROOT / "results" / "pilot").mkdir(parents=True, exist_ok=True)
    (ROOT / "results" / "pilot" / "pilot_report.json").write_text(json.dumps(out, indent=1))
    return 0


# ---------------------------------------------------------------- decision
def project(cfg, rep_player: dict, rep_any_mut: dict, gens: int) -> dict:
    """Pre-registered projection (see config decision_rule.projection_method)."""
    seeds = len(cfg["seeds"])
    pm = rep_player["model"]
    pin = cfg["prices_per_mtok"][pm]["input"] / 1e6
    calls_pg = rep_player["player_calls_per_popgen"]
    base_call = rep_player["player_cost_per_call"]
    extra = cfg["decision_rule"]["genome_growth_extra_input_tokens"] * pin
    # evolving pops (2 of 3) pay extra input tokens for longer genomes; CONTROL does not
    player = seeds * gens * calls_pg * (3 * base_call + 2 * extra)
    per_child = rep_any_mut.get("mutation_cost_per_child") or 0.0
    mut_extra = cfg["decision_rule"]["genome_growth_extra_input_tokens"] * cfg["prices_per_mtok"][cfg["mutator"]["model"]]["input"] / 1e6
    mutations = seeds * gens * 2 * cfg["n_reproduce"] * (per_child + mut_extra)
    return {"player_usd": round(player, 2), "mutation_usd": round(mutations, 2), "total_usd": round(player + mutations, 2),
            "seeds": seeds, "generations": gens}


def cmd_decide(a):
    cfg = load_cfg()
    rep = json.loads((ROOT / "results" / "pilot" / "pilot_report.json").read_text())
    by = {r["model"]: r for r in rep["reports"]}
    rule = cfg["decision_rule"]
    son, hai = by.get("claude-sonnet-5-5"), by.get("claude-haiku-5-5")
    mut_src = son if son and son.get("mutation_cost_per_child") else hai
    lines = ["# DECISION — player model lock", "",
             f"Pre-registered rule (config/frozen.json, sha256 `{cfg_sha256()}`):", "", f"> {rule['text']}", "",
             f"Projection method: {rule['projection_method']}", "", "## Pilot measurements", "",
             "| model | status | cost USD | player calls | invalid rate | refusal rate | calls/s | USD per player call | in/out tokens per call |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in rep["reports"]:
        lines.append(f"| {r['model']} | {r['status']} | {r['cost_usd']:.4f} | {r['player_calls']} | {r['invalid_rate']:.2%} | "
                     f"{r['refusal_rate']:.2%} | {r['calls_per_s']} | {r['player_cost_per_call']:.6f} | "
                     f"{r['player_in_tokens_per_call']:.0f}/{r['player_out_tokens_per_call']:.0f} |")
    lines.append("")
    if mut_src:
        lines.append(f"Mutation cost per child (mutator {cfg['mutator']['model']}): "
                     f"{(mut_src.get('mutation_cost_per_child') or 0):.5f} USD (from the {mut_src['model']} pilot).")
        lines.append("")
    choice, gens, reason = None, None, None
    if son and son["player_calls"] > 0:
        pj = project(cfg, son, mut_src or son, rule["sonnet"]["generations"])
        lines.append(f"Projected cost with claude-sonnet-5-5 players, {pj['seeds']} seeds x 3 populations x "
                     f"{pj['generations']} generations: players {pj['player_usd']} + mutations {pj['mutation_usd']} = "
                     f"**{pj['total_usd']} USD**.")
        ok_cost = pj["total_usd"] <= rule["sonnet"]["max_projected_usd"]
        ok_inv = son["invalid_rate"] < rule["sonnet"]["max_invalid_rate"]
        if ok_cost and ok_inv:
            choice, gens = "claude-sonnet-5-5", rule["sonnet"]["generations"]
            reason = f"projected {pj['total_usd']} USD <= {rule['sonnet']['max_projected_usd']} and invalid rate {son['invalid_rate']:.2%} < 5%"
        else:
            why = []
            if not ok_cost:
                why.append(f"projected {pj['total_usd']} USD > {rule['sonnet']['max_projected_usd']} USD")
            if not ok_inv:
                why.append(f"Sonnet invalid rate {son['invalid_rate']:.2%} >= 5%")
            reason = "; ".join(why)
    else:
        reason = "Sonnet pilot produced no player calls"
    if choice is None:
        choice, gens = rule["fallback"]["model"], rule["fallback"]["generations"]
        if hai:
            pj = project(cfg, hai, mut_src or hai, gens)
            lines.append(f"Projected cost with claude-haiku-5-5 players, {pj['seeds']} seeds x 3 populations x {gens} "
                         f"generations: players {pj['player_usd']} + mutations {pj['mutation_usd']} = **{pj['total_usd']} USD**.")
    lines += ["", "## Decision", "", f"**Player model: `{choice}`, {gens} generations for every seed.**", "",
              f"Reason: {reason}.", ""]
    (ROOT / "DECISION.md").write_text("\n".join(lines))
    (ROOT / "config" / "locked.json").write_text(json.dumps(
        {"player_model": choice, "generations": gens, "reason": reason, "config_sha256": cfg_sha256(),
         "decided_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, indent=1))
    print("\n".join(lines))
    return 0


# ---------------------------------------------------------------- main run
def cmd_run(a):
    cfg = load_cfg()
    lk = json.loads((ROOT / "config" / "locked.json").read_text())
    assert lk["config_sha256"] == cfg_sha256(), "frozen config changed after the decision"
    budget = Budget(cfg["budget"]["total_usd"], cfg["prices_per_mtok"], LEDGER)
    gw = make_gateway(cfg, real_backend(cfg), budget)
    run = SeedRun(seed=a.seed, cfg=cfg, n_gens=lk["generations"], player_model=lk["player_model"], gateway=gw,
                  out_dir=ROOT / "results" / f"seed-{a.seed}", log_path=ROOT / "logs" / f"seed-{a.seed}.jsonl.gz")
    code = 0
    try:
        for s in asyncio.run(run.run(resume=True, max_gens=a.max_gens)):
            print(json.dumps({k: s[k] for k in ("seed", "gen", "shocked", "elapsed_s", "spent_usd")}), flush=True)
    except BudgetExceeded as e:
        print(f"BUDGET STOP: {e}", file=sys.stderr)
        code = EXIT_BUDGET
    except FatalAPIError as e:
        print(f"FATAL: {e}", file=sys.stderr)
        code = EXIT_FATAL
    except InvalidRateStop as e:
        print(f"INVALID-RATE STOP: {e}", file=sys.stderr)
        code = EXIT_INVALID
    finally:
        _flush_aborted(gw, ROOT / "logs" / f"seed-{a.seed}.aborted.jsonl.gz")
    print(json.dumps({"spent_usd": round(budget.spent, 4), "calls": budget.n_calls,
                      "throttled": gw.stats["throttled"]}), flush=True)
    return code


def cmd_analyze(a):
    from .analyze import analyze
    print(analyze(Path(a.results)))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="promptdna")
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fake-run")
    f.add_argument("--seed", type=int, default=1)
    f.add_argument("--gens", type=int, default=3)
    f.add_argument("--out", default=str(ROOT / "results-fake"))
    f.add_argument("--player", default="claude-haiku-5-5")
    f.add_argument("--budget", type=float, default=180.0)
    f.add_argument("--invalid-prob", type=float, default=0.0)
    f.add_argument("--throttle-prob", type=float, default=0.0)
    sub.add_parser("pilot")
    sub.add_parser("decide")
    r = sub.add_parser("run")
    r.add_argument("--seed", type=int, required=True)
    r.add_argument("--max-gens", type=int, default=None)
    an = sub.add_parser("analyze")
    an.add_argument("--results", default=str(ROOT / "results"))
    sub.add_parser("sha")
    a = ap.parse_args(argv)
    if a.cmd == "fake-run":
        return cmd_fake_run(a) or 0
    if a.cmd == "pilot":
        return cmd_pilot(a)
    if a.cmd == "decide":
        return cmd_decide(a)
    if a.cmd == "run":
        return cmd_run(a)
    if a.cmd == "analyze":
        return cmd_analyze(a)
    if a.cmd == "sha":
        print(cfg_sha256())
        return 0


if __name__ == "__main__":
    sys.exit(main())
