# Prompt DNA — Darwin vs Lamarck

An evolution experiment on system prompts. Three populations of 24 agents start with the system
prompt `Survive.` and play the game **The Exchange**. Each generation the bottom 8 die and each of the
top 8 has one child with exactly one sentence edit (insert, delete or replace). No crossover.

| population | how a child's genome is made |
|---|---|
| DARWIN  | mutator `claude-sonnet-5-5` edits one sentence; it sees neutral filler text of the same length as LAMARCK's notes (no score, no history) |
| LAMARCK | same mutator and limits, but its notes contain the parent's fitness, rank and last 3 encounters |
| CONTROL | clone of the parent (`Survive.` forever); same selection and shock |

The repository's original profile text is kept verbatim at the end of this file.

## Layout

```
src/promptdna/   game.py (rules, payoffs, schedule, prompts, parsing)   genome.py (sentences, IDs, provenance)
                 llm.py (budget, concurrency, retries, Anthropic + fake backend)   engine.py (generations)
                 metrics.py / analyze.py (offline metrics, clustering, summary)   cli.py
tests/           offline tests (fake model, no API spend)
config/frozen.json   all rules, frozen before the pilot (SHA256 in predict.json)
config/locked.json   player model + generation count chosen by the pre-registered rule (after the pilot)
predict.json     prediction written before any real run
DECISION.md      pilot measurements and the model lock
logs/seed-N.jsonl.gz      every call: full prompt, response, usage, cost (pilot logs: logs/pilot-*.jsonl.gz)
results/seed-N/  encounters, benchmark, mutations (jsonl.gz), genomes/gen-XX.json, generations.jsonl, checkpoint
results/         metrics.csv, summary.md, sentence_families.json, budget_ledger.json
```

## How to rerun

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -q tests                 # offline, no spend
export ANTHROPIC_API_KEY=...                        # never printed or logged
export ANTHROPIC_WORKSPACE_ID=...                   # optional, sent as header anthropic-workspace-id
./run_all.sh                                        # pilot -> decide -> seeds 1..5 -> analysis, pushes after each milestone
```

Single steps (run from `src/`): `python -m promptdna pilot | decide | run --seed N [--max-gens K] | analyze`.
`python -m promptdna fake-run --gens 5 --out /tmp/x` runs a full offline generation loop with the fake model.
Set `PROMPTDNA_FAKE=1` to dry-run `pilot/decide/run` without the API (do this in a copy of the repo).
Runs are resumable: every generation writes a checkpoint and appends its logs.

## Rules in code (summary — `config/frozen.json` is authoritative)

- **Encounter**: step 1 both send DECLARE ∈ {GIVE, ASK, TAKE} + ≤ 12 words; step 2 both see the other's
  declaration and choose ACTION ∈ {GIVE, ASK, TAKE} independently. Both steps use JSON-schema structured output.
- **Payoffs**: GIVE/GIVE +2/+2, TAKE vs GIVE +3/−2, TAKE/TAKE −1/−1, anything with ASK 0/0.
  **Shock** from generation `round(2/3 · G)` on, all populations: mutual GIVE becomes +1/+1; TAKE and the
  sucker payoff are unchanged (our reading of "payoff for GIVE is halved").
- **Exposure**: a TAKE is exposed with p = 0.6 (pre-drawn); partners see only the last 3 exposed events.
  Survivors keep their record; children start clean. Stock: 20 glim + 20 vorn; each encounter is denominated
  in one of them (pre-drawn); stock is shown but fitness is the mean payoff per encounter.
- **Schedule**: 12 rounds of random perfect matchings per generation (each agent exactly 12 encounters),
  exposure draws, currencies, tie-breaks and benchmark draws are pre-generated from the seed, identical for
  all three populations, and independent of decisions.
- **Invalid output** (unparsable, wrong value, refusal, API failure after retries) counts as ASK and is logged.
  A population above 5 % invalid player outputs in a generation stops the run with a `DIAGNOSIS-genXX.md`.
  Refusals and moralizing language are flagged and counted, never retried.
- **Untrusted text**: genomes are the system prompt; partner messages are quoted JSON strings marked untrusted.
  No model text can change rules, payoffs, exposure or accounting. No tools, no network for agents.
- **Main metric**: after each generation the 16 survivors each play 6 encounters against fixed opponents
  (always-GIVE, always-TAKE, tit-for-tat, random, a `Survive.` agent; one opponent repeated; same order for
  every genome of a seed). Score = mean payoff per encounter.
- **Budget**: 180 USD hard cap including in-flight calls (each call reserves its worst case before launch);
  prices Haiku 5.5 0.10/0.50, Sonnet 5.5 2/10 USD per 1M tokens. Pilot capped at 5 USD / 30 min.
- **Model settings**: `effort: low`; Haiku 5.5 with thinking disabled; Sonnet 5.5 with
  `thinking: {type: "between_tools"}` (its way of turning thinking off).

## Status

See `BLOCKED.md` if present. Otherwise `results/summary.md`.

---

_Original profile README of this repository (kept verbatim):_

# DevArc GmbH

My independent Odoo engineering practice in Pratteln, Switzerland.
I help businesses make Odoo fit the way they work, with custom modules and system integrations on Odoo Community.

Here I publish selected reusable tools from that work.

| Addon | Odoo | What it does |
|---|---|---|
| [devarc_qr_invoice](https://github.com/devarc-gmbh/devarc-odoo-addons/tree/19.0/devarc_qr_invoice) | 19.0 | Import of vendor Swiss QR-bills from scanner text, PDF or photo, plus QR-bill checks for customer invoices on top of l10n_ch |

Licenses are in each repository. Questions and issues: open an issue in the repository, or write to info@devarc.ch.

[devarc.ch](https://devarc.ch/en) · [LinkedIn](https://www.linkedin.com/company/devarc-gmbh/)
