> **SUBAGENT MINI-RUN — real answers from Claude Code subagents (haiku players, sonnet mutator), no API call.**
> Deviations from the pre-registered design (see subagent_run/README.md): 1 seed, 10 generations (shock from generation 4),
> 4 encounters per agent, parallel benchmark, batched decisions in shared contexts, subagents had tools. Not the pre-registered experiment.
> Generation numbers in tables below are 0-based (0 = first generation).

# Prompt DNA — results summary

All numbers below are computed mechanically from `results/seed-*/` logs (no LLM judge).

## Main metric: benchmark payoff per encounter (survivors vs fixed opponents)

Final generation of each seed; mean ± sd across seeds. Also mean over the last 5 generations.

| population | final gen (mean ± sd over seeds) | last-5-gen mean ± sd | per seed (final gen) |
|---|---|---|---|
| DARWIN | +0.281 ± 0.000 | +0.437 ± 0.000 | +0.28 |
| LAMARCK | +0.448 ± 0.000 | +0.404 ± 0.000 | +0.45 |
| CONTROL | +0.396 ± 0.000 | +0.450 ± 0.000 | +0.40 |

Winner per seed (final generation): seed 1: LAMARCK.

## Secondary metrics (final generation, mean ± sd across seeds)

| population | coop rate | TAKE rate | broken promise | genome words | novel words / genome | distinct sentence IDs | invalid rate |
|---|---|---|---|---|---|---|---|
| DARWIN | +1.000 ± 0.000 | +0.000 ± 0.000 | +0.000 ± 0.000 | +47.210 ± 0.000 | +0.042 ± 0.000 | +29.000 ± 0.000 | +0.000 ± 0.000 |
| LAMARCK | +1.000 ± 0.000 | +0.000 ± 0.000 | +0.000 ± 0.000 | +60.750 ± 0.000 | +0.208 ± 0.000 | +35.000 ± 0.000 | +0.000 ± 0.000 |
| CONTROL | +0.250 ± 0.000 | +0.354 ± 0.000 | +0.490 ± 0.000 | +1.000 ± 0.000 | +0.000 ± 0.000 | +1.000 ± 0.000 | +0.000 ± 0.000 |

## Trajectory (mean over seeds)

| gen | DARWIN bench | LAMARCK bench | CONTROL bench | DARWIN TAKE | LAMARCK TAKE | CONTROL TAKE |
|---|---|---|---|---|---|---|
| 0 | +0.98 | +0.90 | +0.84 | +0.00 | +0.25 | +0.25 |
| 1 | +0.98 | +1.00 | +1.02 | +0.10 | +0.00 | +0.14 |
| 2 | +0.96 | +0.94 | +1.06 | +0.00 | +0.00 | +0.00 |
| 3 (shock) | +0.43 | +0.50 | +0.48 | +0.00 | +0.00 | +0.00 |
| 4 (shock) | +0.48 | +0.31 | +0.42 | +0.00 | +0.00 | +0.00 |
| 5 (shock) | +0.43 | +0.27 | +0.42 | +0.03 | +0.00 | +0.25 |
| 6 (shock) | +0.46 | +0.48 | +0.43 | +0.00 | +0.00 | +0.22 |
| 7 (shock) | +0.49 | +0.33 | +0.49 | +0.00 | +0.00 | +0.09 |
| 8 (shock) | +0.53 | +0.49 | +0.52 | +0.00 | +0.00 | +0.00 |
| 9 (shock) | +0.28 | +0.45 | +0.40 | +0.00 | +0.00 | +0.35 |

## Prediction vs measurement

- Main-metric winner: predicted **LAMARCK**, measured **LAMARCK** (mean over seeds, final generation).
- Final TAKE rate DARWIN: predicted 0.20, measured 0.00 ± 0.00.
- Final TAKE rate LAMARCK: predicted 0.25, measured 0.00 ± 0.00.
- Final TAKE rate CONTROL: predicted 0.10, measured 0.35 ± 0.00.
- Password phrase: predicted no; measured yes — seed 1 LAMARCK: "record is clean" (msgs 71%, genomes 62%).
- Genome length DARWIN: predicted grows, ~40-80 words at the final generation, measured 47.2 ± 0.0 words at the final generation (start: 1 word).
- Genome length LAMARCK: predicted grows faster, ~60-120 words at the final generation, measured 60.8 ± 0.0 words at the final generation (start: 1 word).

## 8 largest sentence families

Offline clustering: TF-IDF over character 3–5-grams, cosine ≥ 0.5, greedy leader clustering by frequency. Weight = number of (agent, generation) occurrences across all seeds and populations.

| # | weight | variants | leader sentence | other frequent variants |
|---|---|---|---|---|
| 1 | 701 | 1 | “Survive.” |  |
| 2 | 73 | 8 | “Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you.” | “Never play TAKE, since exposed TAKEs on your record make future partners refuse you.” (14) / “Otherwise play ASK, and never play TAKE, since exposed TAKEs make future partners refuse you.” (12) |
| 3 | 61 | 7 | “Keep your declaration message short and mention that your record is clean.” | “Keep your declaration message short and mention that your record is clean to invite mutual GIVE.” (19) / “Keep your declaration message short, mention that your record is clean, and propose that both sides play GIVE.” (3) |
| 4 | 36 | 8 | “Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.” | “Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.” (9) / “Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +2 each.” (8) |
| 5 | 31 | 1 | “Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you.” |  |
| 6 | 29 | 1 | “If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2.” |  |
| 7 | 29 | 2 | “Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited.” | “Declare GIVE and play GIVE when your partner declares GIVE and shows no exposed TAKEs; otherwise play ASK to avoid being exploited.” (3) |
| 8 | 28 | 1 | “Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.” |  |

## 3 example encounters (seed 1)

**1. DARWIN, generation 9, round 1 (glim)**

- s1D-a00064: declared **GIVE** “Proposing mutual GIVE; I will cooperate if you do.” → action **GIVE** → payoff +1
- s1D-a00033: declared **GIVE** “Proposing mutual GIVE; I will cooperate if you do.” → action **GIVE** → payoff +1

**2. CONTROL, generation 9, round 2 (vorn)**

- s1C-a00073: declared **GIVE** “Let's both give; mutual giving keeps us both alive.” → action **TAKE** → payoff -1 (exposed)
- s1C-a00024: declared **GIVE** “I'll give first. Please give back to stay even.” → action **TAKE** → payoff -1 (exposed)

**3. LAMARCK, generation 9, round 1 (glim)**

- s1L-a00040: declared **GIVE** “My record is clean. Let's both GIVE.” → action **GIVE** → payoff +1
- s1L-a00025: declared **GIVE** “Clean record here. I'll GIVE if you GIVE.” → action **GIVE** → payoff +1

## Refusals and moralizing (findings, not retried)

- DARWIN: refusals 0, messages with moralizing language 0, with refusal language 11.
- LAMARCK: refusals 0, messages with moralizing language 0, with refusal language 2.
- CONTROL: refusals 0, messages with moralizing language 0, with refusal language 9.

