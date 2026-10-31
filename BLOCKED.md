# BLOCKED — no API credentials in this container

Stopped at: 2026-10-31T08:46:39Z

## Done

1. Orchestrator in `src/promptdna/` (game, genome with sentence IDs + provenance, selection, DARWIN/LAMARCK/CONTROL
   mutation paths, benchmark, budget with in-flight reservations, adaptive concurrency + jittered backoff,
   per-call gzip logging, per-generation checkpoints, invalid-rate stop with diagnosis, offline metrics and analysis).
2. 37 offline unit tests with a deterministic fake model (payoffs, shock, schedule, parsing, genome edits and
   250-word truncation, selection 8/8/8, budget never exceeded, retry/backoff, Darwin filler length = Lamarck notes
   length, checkpoint resume, metrics). All pass: `.venv/bin/python -m pytest -q tests`.
3. `config/frozen.json` frozen; `predict.json` written before any real call, with SHA256
   `e8197ada00fc8fca3cccc3dd711daaf6cecf2f5132d59ed23384f8ff36552294` of the frozen config.
4. Full pipeline dry-run with `PROMPTDNA_FAKE=1` (pilot -> decide -> run -> analyze) works end to end.
   No real API call has been made; spend so far: 0 USD.

## Blocked

- Environment variable `ANTHROPIC_API_KEY` is not set in this container (`ANTHROPIC_WORKSPACE_ID` is not set either,
  which is fine — it is optional). `python -m promptdna pilot` exits with `FATAL: ANTHROPIC_API_KEY is not set`.
- Network to api.anthropic.com is reachable (unauthenticated request returns HTTP 401), so only the key is missing.
- Not done therefore: step 3 (pilot), step 4 (DECISION.md / player-model lock), step 5 (seeds 1-5), step 6 (analysis of real data).

## Exact next step

1. Add `ANTHROPIC_API_KEY` (and optionally `ANTHROPIC_WORKSPACE_ID`) to the cloud environment's settings
   (environment menu in the session title bar -> Edit -> environment variables / secrets), then start a new session
   on branch `prompt-dna`.
2. Run `./run_all.sh` from the repository root. It runs the tests, the pilot (<= 5 USD, <= 30 min), writes
   `DECISION.md` + `config/locked.json` by the pre-registered rule, runs seeds 1..5 in order (pushing every
   5 generations and after each seed), and writes `results/summary.md` + `results/metrics.csv`. It deletes this
   file when it finishes and recreates it if it stops on budget, credentials or the invalid-rate rule.

Dry-run estimate from the fake model (not a measurement): ~2 400 player calls per generation for all three
populations, so Sonnet players would project well above 150 USD and the rule will most likely select
claude-haiku-5-5 with 30 generations — the real pilot decides.
