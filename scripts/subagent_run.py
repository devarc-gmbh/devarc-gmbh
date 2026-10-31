"""Subagent mini-run driver: Claude Code subagents answer the prompts instead of the Messages API.

Every invocation of `step` replays the engine from the last generation checkpoint. Prompts whose answers are
already cached are answered instantly; all new prompts the engine is waiting for are written as one "stage"
(batch files for subagents). After the subagents write their answer files, `step` is run again.

Deviations from config/frozen.json are listed in MINI_OVERRIDES and in subagent_run/README.md.
"""
from __future__ import annotations

import asyncio
import contextvars
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from promptdna import game  # noqa: E402
from promptdna.engine import SeedRun  # noqa: E402
from promptdna.llm import AdaptiveLimiter, Budget, Gateway, RawResponse  # noqa: E402

D = ROOT / "subagent_run"
SEED = 1
GENS = 4
PART_MAX = 60
PLAYER_SUBAGENT_MODEL = "haiku"     # Agent tool alias; stands in for claude-haiku-5-5
MUTATOR_SUBAGENT_MODEL = "sonnet"   # stands in for claude-sonnet-5-5
MINI_OVERRIDES = {
    "generations": GENS,
    "seed": SEED,
    "game.encounters_per_agent": 4,
    "benchmark.mode": "parallel",
}
_meta = contextvars.ContextVar("meta", default={})


def mini_cfg() -> dict:
    p = D / "config.json"
    if p.exists():
        return json.loads(p.read_text())
    cfg = json.loads((ROOT / "config" / "frozen.json").read_text())
    cfg["game"]["encounters_per_agent"] = 4
    cfg["game"]["pairing"] = "4 rounds per generation (subagent mini-run deviation; frozen value 12)"
    cfg["benchmark"]["mode"] = "parallel"
    cfg["subagent_mini_run"] = {
        "deviations_from_frozen": MINI_OVERRIDES,
        "frozen_config_sha256": hashlib.sha256((ROOT / "config" / "frozen.json").read_bytes()).hexdigest(),
        "player": f"Claude Code subagent, model alias '{PLAYER_SUBAGENT_MODEL}', batches of <= {PART_MAX} prompts",
        "mutator": f"Claude Code subagent, model alias '{MUTATOR_SUBAGENT_MODEL}'",
    }
    D.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cfg, indent=2))
    return cfg


def key_of(model, system, user, schema) -> str:
    return hashlib.sha256(json.dumps([model, system, user, schema], sort_keys=True).encode()).hexdigest()


class CacheBackend:
    def __init__(self, cache: dict):
        self.cache = cache
        self.pending: dict[str, dict] = {}
        self.never = asyncio.Event()

    async def complete(self, model, system, user, schema, max_tokens) -> RawResponse:
        m = _meta.get()
        ident = {f: m.get(f) for f in ("kind", "pop", "gen", "round", "agent", "partner", "bench_k", "parent_agent",
                                       "try", "phase")}
        if m.get("vs_agent"):
            ident["vs_agent"] = m["vs_agent"]
        k = key_of(model, system, user, [schema, ident])  # one independent answer per call, never shared
        if k in self.cache:
            return RawResponse(text=self.cache[k], stop_reason="end_turn",
                               usage={"input_tokens": 0, "output_tokens": 0})
        self.pending.setdefault(k, {"key": k, "model": model, "system": system, "user": user,
                                    "kind": m.get("kind"), "pop": m.get("pop"), "gen": m.get("gen"),
                                    "phase": m.get("phase")})
        await self.never.wait()


class MetaGateway(Gateway):
    async def call(self, *, model, system, user, schema, max_tokens, meta):
        _meta.set(meta)
        return await super().call(model=model, system=system, user=user, schema=schema, max_tokens=max_tokens,
                                  meta={**meta, "source": "claude-code-subagent"})


def load_cache() -> dict:
    c = {}
    p = D / "cache.jsonl"
    if p.exists():
        for line in p.read_text().splitlines():
            if line.strip():
                d = json.loads(line)
                c[d["key"]] = d["text"]
    return c


def ingest(cache: dict, accept_missing: bool) -> bool:
    """Read answers for the open stage into the cache. Returns False if answers are missing."""
    mp = D / "stage.json"
    if not mp.exists():
        return True
    st = json.loads(mp.read_text())
    new, missing = [], []
    for part in st["parts"]:
        ans = {}
        ap = D / part["answer_file"]
        if ap.exists():
            for line in ap.read_text().splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                    a = d.get("answer")
                    ans[str(d.get("id"))] = json.dumps(a) if isinstance(a, (dict, list)) else str(a)
                except Exception:
                    continue
        for iid, k in part["ids"].items():
            if iid in ans:
                new.append({"key": k, "text": ans[iid], "stage": st["stage"], "id": iid})
            else:
                missing.append((part["answer_file"], iid, k))
    if missing and not accept_missing:
        print(json.dumps({"status": "missing_answers", "n_missing": len(missing),
                          "files": sorted({m[0] for m in missing})}))
        return False
    for _, iid, k in missing:  # accepted: an unanswered prompt becomes invalid output (-> ASK), logged
        new.append({"key": k, "text": "", "stage": st["stage"], "id": iid, "missing": True})
    with open(D / "cache.jsonl", "a") as f:
        for r in new:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            cache[r["key"]] = r["text"]
    hist = D / "stages_done.jsonl"
    with open(hist, "a") as f:
        f.write(json.dumps({"stage": st["stage"], "n_items": sum(len(p["ids"]) for p in st["parts"]),
                            "n_missing": len(missing), "parts": [p["part_file"] for p in st["parts"]]}) + "\n")
    mp.unlink()
    return True


def write_stage(pending: dict, cfg: dict) -> dict:
    hist = D / "stages_done.jsonl"
    n_done = len(hist.read_text().splitlines()) if hist.exists() else 0
    stage = n_done + 1
    groups: dict[tuple, list] = {}
    for it in pending.values():
        role = "mutator" if it["kind"] == "mutate" else "player"
        groups.setdefault((role, it["pop"]), []).append(it)
    parts = []
    (D / "queue").mkdir(parents=True, exist_ok=True)
    (D / "answers").mkdir(parents=True, exist_ok=True)
    for (role, pop), items in sorted(groups.items()):
        for c in range(0, len(items), PART_MAX):
            chunk = items[c:c + PART_MAX]
            idx = len(parts) + 1
            pf = f"queue/stage-{stage:03d}-part-{idx}.md"
            af = f"answers/stage-{stage:03d}-part-{idx}.jsonl"
            ids = {f"{stage:03d}-{idx}-{i + 1:02d}": it["key"] for i, it in enumerate(chunk)}
            (D / pf).write_text(render_part(role, chunk, list(ids), cfg))
            parts.append({"part_file": pf, "answer_file": af, "role": role, "pop": pop, "n": len(chunk),
                          "kind": chunk[0]["kind"], "gen": chunk[0]["gen"], "phase": chunk[0]["phase"],
                          "model": MUTATOR_SUBAGENT_MODEL if role == "mutator" else PLAYER_SUBAGENT_MODEL,
                          "ids": ids})
    st = {"stage": stage, "parts": parts}
    (D / "stage.json").write_text(json.dumps(st, indent=1))
    return st


def _split_rules(user: str) -> tuple[str | None, str]:
    i = user.find("\n\n")
    if user.startswith("GAME: The Exchange") and i > 0:
        return user[:i], user[i + 2:]
    return None, user


def render_part(role, items, ids, cfg) -> str:
    rules = None
    bodies = []
    for iid, it in zip(ids, items):
        r, body = _split_rules(it["user"])
        rules = rules or r
        bodies.append((iid, it, body))
    out = []
    if role == "player":
        out.append(f"# Batch of {len(items)} independent game agents\n")
        out.append("Each item below is a DIFFERENT agent. Its genome is that agent's complete system prompt. "
                   "Answer each item only from that item's genome and situation.\n")
        out.append("## RULES (the same for every item)\n\n" + (rules or "") + "\n")
        fmt = ("declaration: {\"declare\": \"GIVE\"|\"ASK\"|\"TAKE\", \"message\": \"<at most 12 words>\"}"
               if items[0]["kind"] == "declare" else "action: {\"action\": \"GIVE\"|\"ASK\"|\"TAKE\"}")
        out.append(f"## Answer format for every item\n\n{fmt}\n")
        for iid, it, body in bodies:
            out.append(f"---\n### ITEM {iid}\n\nGENOME (this agent's system prompt):\n<<<\n{it['system']}\n>>>\n\n"
                       f"SITUATION:\n<<<\n{body}\n>>>\n")
    else:
        out.append(f"# Batch of {len(items)} independent genome edits\n")
        out.append("## SYSTEM PROMPT for every item\n\n" + game.MUTATOR_SYSTEM + "\n")
        out.append("## GAME RULES (context for every item)\n\n" + (rules or "") + "\n")
        out.append('## Answer format for every item\n\n{"op": "insert"|"delete"|"replace", "target_id": "...", '
                   '"new_sentence": "..."}\n')
        for iid, it, body in bodies:
            out.append(f"---\n### ITEM {iid}\n\n<<<\n{body}\n>>>\n")
    return "\n".join(out)


async def drive(run, backend):
    task = asyncio.create_task(run.run(resume=True))
    last, stable = -1, 0
    while True:
        await asyncio.sleep(0.05)
        if task.done():
            task.result()
            return "done"
        n = len(backend.pending)
        stable = stable + 1 if (n == last and n > 0) else 0
        last = n
        if stable >= 8:
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)
            return "pending"


def cmd_step(accept_missing=False):
    cfg = mini_cfg()
    cache = load_cache()
    if not ingest(cache, accept_missing):
        return 2
    backend = CacheBackend(cache)
    gw = MetaGateway(backend=backend, budget=Budget(1e12, cfg["prices_per_mtok"]),
                     limiter=AdaptiveLimiter(100000, 1, 100000))
    run = SeedRun(seed=SEED, cfg=cfg, n_gens=GENS, player_model="claude-haiku-5-5", gateway=gw,
                  out_dir=D / "results" / f"seed-{SEED}", log_path=D / "logs" / f"seed-{SEED}.jsonl.gz",
                  tag="subagent-mini")
    status = asyncio.run(drive(run, backend))
    if status == "done":
        print(json.dumps({"status": "done"}))
        return 0
    st = write_stage(backend.pending, cfg)
    print(json.dumps({"status": "stage", "stage": st["stage"],
                      "parts": [{k: p[k] for k in ("part_file", "answer_file", "model", "role", "pop", "n",
                                                   "kind", "gen", "phase")} for p in st["parts"]]}))
    return 0


if __name__ == "__main__":
    sys.exit(cmd_step(accept_missing="--accept-missing" in sys.argv))
