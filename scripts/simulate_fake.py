"""Offline simulation of the full experiment with the deterministic FAKE model (no API calls, no spend).

Output goes to sim/ and is NOT an experimental result: the fake model picks actions from keywords in the
genome and its 'mutator' ignores the notes, so DARWIN vs LAMARCK differences here are pure chance.
It exercises the whole pipeline (game, selection, mutation bookkeeping, benchmark, metrics, analysis).
"""
import asyncio
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from promptdna.engine import SeedRun  # noqa: E402
from promptdna.llm import AdaptiveLimiter, Budget, FakeBackend, Gateway  # noqa: E402

GENS = int(sys.argv[1]) if len(sys.argv) > 1 else 30
OUT = ROOT / "sim"
cfg = json.loads((ROOT / "config" / "frozen.json").read_text())
if OUT.exists():
    shutil.rmtree(OUT)
budget = Budget(1e9, cfg["prices_per_mtok"])  # fake 'cost' is bookkeeping only; nothing is billed
for seed in cfg["seeds"]:
    gw = Gateway(backend=FakeBackend(seed=seed), budget=budget, limiter=AdaptiveLimiter(16))
    run = SeedRun(seed=seed, cfg=cfg, n_gens=GENS, player_model="claude-haiku-5-5", gateway=gw,
                  out_dir=OUT / "results" / f"seed-{seed}", log_path=OUT / "logs" / f"seed-{seed}.jsonl.gz")
    s = asyncio.run(run.run(resume=False))
    print(f"seed {seed}: {len(s)} generations, fake calls so far {budget.n_calls}", flush=True)

from promptdna.analyze import analyze  # noqa: E402
text = analyze(OUT / "results")
banner = ("> **SIMULATION with the offline fake model — no API call was made, these are NOT Claude results.**\n"
          "> The fake player chooses actions from keywords in its genome; the fake mutator ignores its notes,\n"
          "> so any DARWIN vs LAMARCK difference below is chance. Purpose: show the pipeline end to end.\n\n")
(OUT / "results" / "summary.md").write_text(banner + text)
print("done")
