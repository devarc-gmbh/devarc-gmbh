# Offline simulation (fake model) — NOT experimental results

Made without any API call: `scripts/simulate_fake.py 30` runs 5 seeds x 3 populations x 30 generations with the
deterministic fake model from `src/promptdna/llm.py`, then `scripts/animate.py sim/results sim/video/prompt-dna-simulation.mp4`
renders the video.

The fake player picks GIVE/TAKE/ASK from keywords in its genome; the fake mutator picks an edit from a
fixed sentence list by hash and ignores its notes. So the DARWIN vs LAMARCK difference here is chance, and
nothing here says anything about how Claude behaves. It shows that the full pipeline (game, selection,
mutation bookkeeping, benchmark, metrics, clustering, summary, video) works end to end.
The fake "cost" in the bookkeeping is not real spend; real spend is 0 USD.
