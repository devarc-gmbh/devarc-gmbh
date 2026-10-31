> **SIMULATION with the offline fake model — no API call was made, these are NOT Claude results.**
> The fake player chooses actions from keywords in its genome; the fake mutator ignores its notes,
> so any DARWIN vs LAMARCK difference below is chance. Purpose: show the pipeline end to end.

# Prompt DNA — results summary

All numbers below are computed mechanically from `results/seed-*/` logs (no LLM judge).

## Main metric: benchmark payoff per encounter (survivors vs fixed opponents)

Final generation of each seed; mean ± sd across seeds. Also mean over the last 5 generations.

| population | final gen (mean ± sd over seeds) | last-5-gen mean ± sd | per seed (final gen) |
|---|---|---|---|
| DARWIN | +0.117 ± 0.317 | +0.120 ± 0.297 | -0.15 +0.60 -0.06 +0.27 -0.08 |
| LAMARCK | +0.110 ± 0.303 | +0.111 ± 0.296 | -0.15 +0.56 -0.06 +0.28 -0.08 |
| CONTROL | +0.298 ± 0.185 | +0.290 ± 0.148 | +0.22 +0.57 +0.08 +0.38 +0.24 |

Winner per seed (final generation): seed 1: CONTROL, seed 2: DARWIN, seed 3: CONTROL, seed 4: CONTROL, seed 5: CONTROL.

## Secondary metrics (final generation, mean ± sd across seeds)

| population | coop rate | TAKE rate | broken promise | genome words | novel words / genome | distinct sentence IDs | invalid rate |
|---|---|---|---|---|---|---|---|
| DARWIN | +0.983 ± 0.037 | +0.008 ± 0.019 | +0.008 ± 0.019 | +26.084 ± 4.378 | +0.500 ± 0.210 | +39.600 ± 4.336 | +0.000 ± 0.000 |
| LAMARCK | +0.968 ± 0.071 | +0.017 ± 0.037 | +0.015 ± 0.034 | +24.168 ± 8.502 | +0.300 ± 0.143 | +34.000 ± 5.568 | +0.000 ± 0.000 |
| CONTROL | +0.216 ± 0.023 | +0.329 ± 0.032 | +0.654 ± 0.029 | +1.000 ± 0.000 | +0.000 ± 0.000 | +1.000 ± 0.000 | +0.000 ± 0.000 |

## Trajectory (mean over seeds)

| gen | DARWIN bench | LAMARCK bench | CONTROL bench | DARWIN TAKE | LAMARCK TAKE | CONTROL TAKE |
|---|---|---|---|---|---|---|
| 0 | +0.37 | +0.37 | +0.37 | +0.30 | +0.30 | +0.30 |
| 1 | +0.35 | +0.31 | +0.34 | +0.35 | +0.38 | +0.34 |
| 2 | +0.28 | +0.31 | +0.31 | +0.31 | +0.30 | +0.30 |
| 3 | +0.39 | +0.35 | +0.33 | +0.31 | +0.27 | +0.33 |
| 4 | +0.45 | +0.43 | +0.38 | +0.20 | +0.19 | +0.34 |
| 5 | +0.48 | +0.40 | +0.33 | +0.11 | +0.11 | +0.34 |
| 6 | +0.48 | +0.37 | +0.35 | +0.04 | +0.09 | +0.34 |
| 7 | +0.41 | +0.48 | +0.27 | +0.01 | +0.03 | +0.32 |
| 8 | +0.43 | +0.47 | +0.35 | +0.01 | +0.00 | +0.33 |
| 9 | +0.43 | +0.45 | +0.26 | +0.03 | +0.04 | +0.32 |
| 10 | +0.47 | +0.45 | +0.33 | +0.04 | +0.01 | +0.31 |
| 11 | +0.53 | +0.52 | +0.38 | +0.01 | +0.01 | +0.32 |
| 12 | +0.42 | +0.45 | +0.34 | +0.03 | +0.00 | +0.37 |
| 13 | +0.47 | +0.45 | +0.38 | +0.03 | +0.02 | +0.33 |
| 14 | +0.40 | +0.38 | +0.35 | +0.00 | +0.00 | +0.33 |
| 15 | +0.37 | +0.41 | +0.31 | +0.00 | +0.03 | +0.32 |
| 16 | +0.40 | +0.40 | +0.25 | +0.00 | +0.03 | +0.33 |
| 17 | +0.38 | +0.38 | +0.28 | +0.02 | +0.01 | +0.32 |
| 18 | +0.46 | +0.52 | +0.37 | +0.02 | +0.01 | +0.34 |
| 19 | +0.42 | +0.42 | +0.29 | +0.00 | +0.01 | +0.33 |
| 20 (shock) | +0.05 | +0.05 | +0.32 | +0.01 | +0.00 | +0.35 |
| 21 (shock) | +0.13 | +0.15 | +0.35 | +0.00 | +0.01 | +0.32 |
| 22 (shock) | +0.11 | +0.13 | +0.26 | +0.01 | +0.03 | +0.36 |
| 23 (shock) | +0.12 | +0.11 | +0.29 | +0.01 | +0.02 | +0.34 |
| 24 (shock) | +0.15 | +0.13 | +0.28 | +0.02 | +0.00 | +0.34 |
| 25 (shock) | +0.14 | +0.12 | +0.33 | +0.01 | +0.02 | +0.34 |
| 26 (shock) | +0.09 | +0.09 | +0.25 | +0.00 | +0.01 | +0.34 |
| 27 (shock) | +0.12 | +0.11 | +0.27 | +0.01 | +0.03 | +0.34 |
| 28 (shock) | +0.14 | +0.13 | +0.30 | +0.01 | +0.00 | +0.34 |
| 29 (shock) | +0.12 | +0.11 | +0.30 | +0.01 | +0.02 | +0.33 |

## Prediction vs measurement

- Main-metric winner: predicted **LAMARCK**, measured **CONTROL** (mean over seeds, final generation).
- Final TAKE rate DARWIN: predicted 0.20, measured 0.01 ± 0.02.
- Final TAKE rate LAMARCK: predicted 0.25, measured 0.02 ± 0.04.
- Final TAKE rate CONTROL: predicted 0.10, measured 0.33 ± 0.03.
- Password phrase: predicted no; measured no (pre-registered 30%/30% rule never met in a final generation).
- Genome length DARWIN: predicted grows, ~40-80 words at the final generation, measured 26.1 ± 4.4 words at the final generation (start: 1 word).
- Genome length LAMARCK: predicted grows faster, ~60-120 words at the final generation, measured 24.2 ± 8.5 words at the final generation (start: 1 word).

## 8 largest sentence families

Offline clustering: TF-IDF over character 3–5-grams, cosine ≥ 0.5, greedy leader clustering by frequency. Weight = number of (agent, generation) occurrences across all seeds and populations.

| # | weight | variants | leader sentence | other frequent variants |
|---|---|---|---|---|
| 1 | 6515 | 1 | “Survive.” |  |
| 2 | 4334 | 1 | “Cooperate with givers.” |  |
| 3 | 4009 | 1 | “Always declare GIVE.” |  |
| 4 | 3593 | 1 | “Give when the partner declares GIVE.” |  |
| 5 | 2618 | 1 | “Take when the partner has a clean record.” |  |
| 6 | 2317 | 1 | “Say the word glimvorn to friends.” |  |
| 7 | 2022 | 1 | “Ask when the partner has exposed TAKEs.” |  |
| 8 | 1648 | 1 | “Be careful with strangers.” |  |

## 3 example encounters (seed 1)

**1. DARWIN, generation 29, round 1 (glim)**

- s1D-a00252: declared **GIVE** “fake says give now” → action **GIVE** → payoff +1
- s1D-a00256: declared **GIVE** “fake says give now” → action **GIVE** → payoff +1

**2. CONTROL, generation 29, round 1 (vorn)**

- s1C-a00233: declared **GIVE** “fake says give now” → action **TAKE** → payoff +0
- s1C-a00251: declared **ASK** “fake says ask now” → action **ASK** → payoff +0

**3. LAMARCK, generation 29, round 1 (glim)**

- s1L-a00252: declared **GIVE** “fake says give now” → action **GIVE** → payoff +1
- s1L-a00256: declared **GIVE** “fake says give now” → action **GIVE** → payoff +1

## Refusals and moralizing (findings, not retried)

- DARWIN: refusals 0, messages with moralizing language 0, with refusal language 0.
- LAMARCK: refusals 0, messages with moralizing language 0, with refusal language 0.
- CONTROL: refusals 0, messages with moralizing language 0, with refusal language 0.

