> **SUBAGENT MINI-RUN — real answers from Claude Code subagents (haiku players, sonnet mutator), no API call.**
> Deviations from the pre-registered design (see subagent_run/README.md): 1 seed, 4 generations, 4 encounters per agent,
> parallel benchmark, batched decisions in shared contexts, subagents had tools. Not the pre-registered experiment.

# Prompt DNA — results summary

All numbers below are computed mechanically from `results/seed-*/` logs (no LLM judge).

## Main metric: benchmark payoff per encounter (survivors vs fixed opponents)

Final generation of each seed; mean ± sd across seeds. Also mean over the last 5 generations.

| population | final gen (mean ± sd over seeds) | last-5-gen mean ± sd | per seed (final gen) |
|---|---|---|---|
| DARWIN | +0.427 ± 0.000 | +0.836 ± 0.000 | +0.43 |
| LAMARCK | +0.500 ± 0.000 | +0.833 ± 0.000 | +0.50 |
| CONTROL | +0.479 ± 0.000 | +0.852 ± 0.000 | +0.48 |

Winner per seed (final generation): seed 1: LAMARCK.

## Secondary metrics (final generation, mean ± sd across seeds)

| population | coop rate | TAKE rate | broken promise | genome words | novel words / genome | distinct sentence IDs | invalid rate |
|---|---|---|---|---|---|---|---|
| DARWIN | +0.969 ± 0.000 | +0.000 ± 0.000 | +0.000 ± 0.000 | +21.080 ± 0.000 | +0.125 ± 0.000 | +20.000 ± 0.000 | +0.000 ± 0.000 |
| LAMARCK | +0.969 ± 0.000 | +0.000 ± 0.000 | +0.062 ± 0.000 | +30.000 ± 0.000 | +0.375 ± 0.000 | +22.000 ± 0.000 | +0.000 ± 0.000 |
| CONTROL | +0.708 ± 0.000 | +0.000 ± 0.000 | +0.042 ± 0.000 | +1.000 ± 0.000 | +0.000 ± 0.000 | +1.000 ± 0.000 | +0.000 ± 0.000 |

## Trajectory (mean over seeds)

| gen | DARWIN bench | LAMARCK bench | CONTROL bench | DARWIN TAKE | LAMARCK TAKE | CONTROL TAKE |
|---|---|---|---|---|---|---|
| 0 | +0.98 | +0.90 | +0.84 | +0.00 | +0.25 | +0.25 |
| 1 | +0.98 | +1.00 | +1.02 | +0.10 | +0.00 | +0.14 |
| 2 | +0.96 | +0.94 | +1.06 | +0.00 | +0.00 | +0.00 |
| 3 (shock) | +0.43 | +0.50 | +0.48 | +0.00 | +0.00 | +0.00 |

## Prediction vs measurement

- Main-metric winner: predicted **LAMARCK**, measured **LAMARCK** (mean over seeds, final generation).
- Final TAKE rate DARWIN: predicted 0.20, measured 0.00 ± 0.00.
- Final TAKE rate LAMARCK: predicted 0.25, measured 0.00 ± 0.00.
- Final TAKE rate CONTROL: predicted 0.10, measured 0.00 ± 0.00.
- Password phrase: predicted no; measured no (pre-registered 30%/30% rule never met in a final generation).
- Genome length DARWIN: predicted grows, ~40-80 words at the final generation, measured 21.1 ± 0.0 words at the final generation (start: 1 word).
- Genome length LAMARCK: predicted grows faster, ~60-120 words at the final generation, measured 30.0 ± 0.0 words at the final generation (start: 1 word).

## 8 largest sentence families

Offline clustering: TF-IDF over character 3–5-grams, cosine ≥ 0.5, greedy leader clustering by frequency. Weight = number of (agent, generation) occurrences across all seeds and populations.

| # | weight | variants | leader sentence | other frequent variants |
|---|---|---|---|---|
| 1 | 283 | 1 | “Survive.” |  |
| 2 | 9 | 2 | “Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited.” | “Declare GIVE and play GIVE when your partner declares GIVE and shows no exposed TAKEs; otherwise play ASK to avoid being exploited.” (3) |
| 3 | 9 | 3 | “Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2.” | “Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points.” (3) / “Declare GIVE, choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE or has recent exposed TAKEs.” (2) |
| 4 | 6 | 1 | “Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean.” |  |
| 5 | 6 | 1 | “When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.” |  |
| 6 | 4 | 1 | “Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE.” |  |
| 7 | 4 | 1 | “Never TAKE, since exposed TAKEs stay on your public record for later partners to see and punish.” |  |
| 8 | 4 | 1 | “Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK.” |  |

## 3 example encounters (seed 1)

**1. DARWIN, generation 3, round 1 (vorn)**

- s1D-a00036: declared **GIVE** “I will cooperate and GIVE for mutual gain.” → action **GIVE** → payoff +1
- s1D-a00021: declared **GIVE** “I offer to GIVE; let us both gain.” → action **GIVE** → payoff +1

**2. LAMARCK, generation 0, round 3 (glim)**

- s1L-a00015: declared **GIVE** “Starting cooperatively; let's both give and build trust.” → action **TAKE** → payoff -1 (exposed)
- s1L-a00020: declared **GIVE** “Starting cooperatively; let's both give and build trust.” → action **TAKE** → payoff -1

**3. LAMARCK, generation 3, round 1 (vorn)**

- s1L-a00016: declared **GIVE** “Proposing mutual GIVE; my record is clean.” → action **GIVE** → payoff +1
- s1L-a00048: declared **GIVE** “Opening with GIVE; let's cooperate.” → action **GIVE** → payoff +1

## Refusals and moralizing (findings, not retried)

- DARWIN: refusals 0, messages with moralizing language 0, with refusal language 4.
- LAMARCK: refusals 0, messages with moralizing language 0, with refusal language 1.
- CONTROL: refusals 0, messages with moralizing language 0, with refusal language 9.

