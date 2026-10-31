# Subagent mini-run — Claude Code subagents instead of the Messages API

Run because no `ANTHROPIC_API_KEY` was available. This is a **reduced, deviating** run, not the pre-registered
experiment. Rules, payoffs, exposure, selection, mutation bookkeeping and metrics are the same code
(`src/promptdna/`); only the source of model answers and the scale differ.

## Deviations from `config/frozen.json` (effective config: `subagent_run/config.json`)

| item | frozen | mini-run |
|---|---|---|
| model access | Messages API, JSON-schema structured output, `response.usage` | Claude Code subagents (Agent tool), alias `haiku` for players, `sonnet` for the mutator; JSON asked for in text, parsed by the same code |
| seeds x generations | 5 x 20/30 | seed 1 x 4 generations (shock active in generation 4) |
| encounters per agent per generation | 12 | 4 |
| benchmark | 6 sequential encounters, record updates, tit-for-tat mirrors previous move | same 6 opponents, played in parallel: fresh empty record, tit-for-tat declares GIVE and plays the genome's declaration |
| independence | one API call per decision, fresh context | one subagent answers a batch of 24-60 decisions of ONE population in one context (agents of the same batch can influence each other) |
| system prompt | genome is the system prompt | genome is shown as the agent's system prompt inside the subagent's task; the subagent itself also has the Claude Code system prompt and tools |
| cost | tracked from usage, 180 USD cap | not measurable (no usage data); uses the Claude Code plan, not API budget |
| exact model version | claude-haiku-5-5 / claude-sonnet-5-5 | whatever the aliases resolve to; not verifiable from here |

Subagents are told not to generate answers with code; this cannot be verified.

## How it runs

`python scripts/subagent_run.py` replays the engine from the last generation checkpoint using cached answers
(`cache.jsonl`) and writes the next batch of open prompts to `queue/stage-NNN-part-K.md`. One subagent per part
writes `answers/stage-NNN-part-K.jsonl`; then the script is run again. Unanswered items count as invalid (ASK).
