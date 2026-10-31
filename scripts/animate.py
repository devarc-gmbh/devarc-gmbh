"""Render an MP4 animation of a Prompt DNA results directory (offline, no API).

usage: python scripts/animate.py <results_dir> <out.mp4> [--title-note TEXT] [--story-seed N]
"""
import argparse
import csv
import gzip
import json
import textwrap
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.animation import FFMpegWriter  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

# reference dark palette (validated: categorical slots 1-3 on surface #1a1a19, all checks pass)
SURFACE, TEXT1, TEXT2, MUTED, GRID = "#1a1a19", "#f0efec", "#c3c2b7", "#8a8980", "#33332f"
POP_COLOR = {"DARWIN": "#3987e5", "LAMARCK": "#d95926", "CONTROL": "#199e70"}
POPS = ["DARWIN", "LAMARCK", "CONTROL"]
TAKE_CMAP = LinearSegmentedColormap.from_list("take", ["#2b2a3a", "#9085e9", "#e3e0ff"])  # one hue, dim -> bright

ap = argparse.ArgumentParser()
ap.add_argument("results")
ap.add_argument("out")
ap.add_argument("--title-note", default="")
ap.add_argument("--story-seed", type=int, default=1)
ap.add_argument("--fps", type=int, default=24)
ap.add_argument("--frames-per-gen", type=int, default=12)
ap.add_argument("--metrics", default="bench_mean,take_rate,genome_words_mean")
a = ap.parse_args()
R = Path(a.results)

# ------------------------------------------------------------------ data
rows = list(csv.DictReader(open(R / "metrics.csv")))
gens = sorted({int(r["generation"]) for r in rows})
G = len(gens)
seeds = sorted({int(r["seed"]) for r in rows})
shock_gen = next((int(r["generation"]) for r in sorted(rows, key=lambda r: int(r["generation"]))
                  if r["shocked"] == "True"), None)
METRIC_LABELS = {
    "bench_mean": ("Benchmark skóre — hlavná metrika", "payoff / stretnutie"),
    "fitness_mean": ("Priemerný zisk v hre (fitness)", "payoff / stretnutie"),
    "take_rate": ("TAKE rate v hre", "podiel akcií"),
    "ask_rate": ("ASK rate v hre (odmietnutie výmeny)", "podiel akcií"),
    "broken_promise_rate": ("Porušené sľuby (deklarácia ≠ akcia)", "podiel"),
    "genome_words_mean": ("Dĺžka genómu", "slová (priemer)"),
}
METRICS = [(m, *METRIC_LABELS[m]) for m in a.metrics.split(",")]
series = {}  # (metric, pop) -> array [seed, gen]
for m, _, _ in METRICS:
    for p in POPS:
        arr = np.full((len(seeds), G), np.nan)
        for r in rows:
            if r["population"] == p and r[m] not in ("", "None"):
                arr[seeds.index(int(r["seed"])), int(r["generation"])] = float(r[m])
        series[(m, p)] = arr

story = R / f"seed-{a.story_seed}"
take_share = defaultdict(lambda: [0, 0])  # (pop, gen, agent) -> [takes, n]
with gzip.open(story / "encounters.jsonl.gz", "rt") as f:
    for line in f:
        e = json.loads(line)
        for s in ("a", "b"):
            k = (e["pop"], e["gen"], e[s]["agent"])
            take_share[k][0] += e[s]["action"] == "TAKE"
            take_share[k][1] += 1
genomes = {g: json.loads((story / "genomes" / f"gen-{g:02d}.json").read_text()) for g in gens}

# ------------------------------------------------------------------ figure
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": TEXT1, "axes.labelcolor": TEXT2,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.edgecolor": GRID})
fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=SURFACE)
gs = fig.add_gridspec(3, 2, left=0.055, right=0.985, top=0.86, bottom=0.07, wspace=0.12, hspace=0.42,
                      width_ratios=[1.05, 1])
line_axes = [fig.add_subplot(gs[i, 0]) for i in range(3)]
pop_axes = [fig.add_subplot(gs[i, 1]) for i in range(3)]

fig.text(0.055, 0.945, "Prompt DNA — Darwin vs Lamarck", fontsize=22, weight="bold", color=TEXT1)
if a.title_note:
    fig.text(0.055, 0.905, a.title_note, fontsize=11.5, color="#e8b04a")
gen_txt = fig.text(0.985, 0.945, "", fontsize=20, ha="right", color=TEXT1, weight="bold")
shock_txt = fig.text(0.985, 0.905, "", fontsize=11.5, ha="right", color=TEXT2)

limits = {}
for (m, title, ylab), ax in zip(METRICS, line_axes):
    allv = np.concatenate([series[(m, p)].ravel() for p in POPS])
    lo, hi = np.nanmin(allv), np.nanmax(allv)
    pad = (hi - lo) * 0.12 or 0.5
    limits[m] = (lo - pad, hi + pad)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0, G - 1 + (3.2 if G > 10 else 1.4))
    ax.set_ylim(*limits[m])
    ax.set_title(title, loc="left", fontsize=13, color=TEXT1, pad=6)
    ax.set_ylabel(ylab, fontsize=9.5)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=9)
    step = 1 if G <= 10 else 5
    ax.set_xticks([t for t in range(0, G, step)] + ([G - 1] if (G - 1) % step else []))
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{int(x) + 1}"))  # 1-based gens
    if shock_gen is not None:
        ax.axvline(shock_gen - 0.5, color=MUTED, linestyle=(0, (3, 3)), linewidth=1)
        ax.text(shock_gen - 0.35, limits[m][1], "šok: GIVE+GIVE ½", fontsize=8.5, color=MUTED, va="top")
line_axes[-1].set_xlabel("generácia", fontsize=10)
line_axes[0].text(1.0, 1.06, (f"čiara = priemer {len(seeds)} seedov, pás = min–max" if len(seeds) > 1 else f"seed {seeds[0]}"), transform=line_axes[0].transAxes,
                  fontsize=9, color=MUTED, ha="right")

artists = {}
for (m, _, _), ax in zip(METRICS, line_axes):
    for p in POPS:
        ln, = ax.plot([], [], color=POP_COLOR[p], linewidth=2.2, solid_capstyle="round")
        dot, = ax.plot([], [], "o", color=POP_COLOR[p], markersize=8, markeredgecolor=SURFACE, markeredgewidth=2)
        lab = ax.text(0, 0, "", fontsize=9.5, color=TEXT1, va="center")
        artists[(m, p)] = (ln, dot, lab, [None])

# population panels: 24-agent grid (4 x 6) + best genome text
cells = {}
for p, ax in zip(POPS, pop_axes):
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.add_patch(Rectangle((0, 3.72), 0.18, 0.28, color=POP_COLOR[p], clip_on=False))
    ax.text(0.3, 3.86, p, fontsize=13, weight="bold", color=TEXT1, va="center")
    sub = {"DARWIN": "mutátor bez spätnej väzby", "LAMARCK": "mutátor vidí fitness + históriu",
           "CONTROL": "klony „Survive.“"}[p]
    ax.text(0.3 + 0.17 * len(p) + 0.5, 3.86, sub, fontsize=9.5, color=TEXT2, va="center")
    cs = []
    for slot in range(24):
        r, c = divmod(slot, 6)
        x, y = c * 0.62, 2.85 - r * 0.78
        rect = Rectangle((x, y), 0.54, 0.7, facecolor=TAKE_CMAP(0), edgecolor=SURFACE, linewidth=2)
        ax.add_patch(rect)
        mark = ax.text(x + 0.27, y + 0.35, "", fontsize=13, ha="center", va="center", color=TEXT1, weight="bold")
        cs.append((rect, mark))
    best = ax.text(3.95, 3.45, "", fontsize=9.2, color=TEXT1, va="top", family="DejaVu Sans Mono", linespacing=1.25)
    meta = ax.text(3.95, 0.1, "", fontsize=9, color=TEXT2, va="bottom")
    cells[p] = (cs, best, meta)
pop_axes[0].text(0, 4.42, f"seed {a.story_seed}: 24 agentov (farba = ich podiel TAKE, rám = nový potomok, × = zomiera)",
                 fontsize=9, color=MUTED)
# colorbar legend for the agent grid
cax = fig.add_axes([0.72, 0.025, 0.2, 0.012])
cax.imshow(np.linspace(0, 1, 256)[None, :], cmap=TAKE_CMAP, aspect="auto", extent=(0, 1, 0, 1))
cax.set_yticks([])
cax.set_xticks([0, 0.5, 1], ["0 % TAKE", "50 %", "100 %"], fontsize=8.5, color=MUTED)
for s in cax.spines.values():
    s.set_visible(False)


def draw(t):
    g = min(int(t), G - 1)
    frac = t - int(t)
    gen_txt.set_text(f"generácia {g + 1} / {G}")
    shock_txt.set_text("šok aktívny: vzájomné GIVE dáva len +1" if shock_gen is not None and g >= shock_gen
                       else (f"šok od generácie {shock_gen + 1}" if shock_gen is not None else ""))
    for (m, _, _), ax in zip(METRICS, line_axes):
        lo, hi = limits[m]
        # end labels, nudged apart so they never collide
        ends = []
        for p in POPS:
            arr = series[(m, p)]
            mean = np.nanmean(arr, axis=0)
            xs = list(range(g + 1))
            ys = list(mean[: g + 1])
            if frac > 0 and g + 1 < G:
                xs.append(g + frac)
                ys.append(mean[g] + (mean[g + 1] - mean[g]) * frac)
            ln, dot, lab, band = artists[(m, p)]
            ln.set_data(xs, ys)
            dot.set_data([xs[-1]], [ys[-1]])
            if band[0] is not None:
                band[0].remove()
            n = g + 1
            band[0] = ax.fill_between(range(n), np.nanmin(arr, axis=0)[:n], np.nanmax(arr, axis=0)[:n],
                                      color=POP_COLOR[p], alpha=0.13, linewidth=0)
            ends.append([ys[-1], p, xs[-1]])
        ends.sort()
        gap = (hi - lo) * 0.11
        for i in range(1, len(ends)):
            ends[i][0] = max(ends[i][0], ends[i - 1][0] + gap)
        for y, p, x in ends:
            lab = artists[(m, p)][2]
            raw = [e for e in ends if e[1] == p][0]
            val = np.interp(x, range(G), np.nanmean(series[(m, p)], axis=0))
            lab.set_position((x + (0.6 if G > 10 else 0.12), y))
            lab.set_text(f"{p}  {val:.2f}" if m != "genome_words_mean" else f"{p}  {val:.0f}")
    for p in POPS:
        cs, best, meta = cells[p]
        rows_g = genomes[g][p]
        by_slot = {r["slot"]: r for r in rows_g}
        for slot, (rect, mark) in enumerate(cs):
            r = by_slot[slot]
            tk, n = take_share.get((p, g, r["agent"]), (0, 1))
            rect.set_facecolor(TAKE_CMAP(tk / max(1, n)))
            newborn = r["born_gen"] == g and g > 0
            rect.set_edgecolor(TEXT1 if newborn else SURFACE)
            rect.set_linewidth(2.2 if newborn else 2)
            mark.set_text("×" if r["fate"] == "dies" else "")
            mark.set_color("#1a1a19" if tk / max(1, n) > 0.6 else TEXT1)
        top = rows_g[0]
        txt = top["genome"]["text"]
        wrapped = textwrap.wrap(txt, 52)
        if len(wrapped) > 9:
            wrapped = wrapped[:9]
            wrapped[-1] = wrapped[-1][:49] + "…"
        best.set_text("najlepší genóm:\n" + "\n".join(wrapped))
        meta.set_text(f"fitness {top['fitness']:+.2f} · {top['genome']['n_words']} slov · "
                      f"{len(top['genome']['sentences'])} viet · edit: {top['genome']['edit']['op']}")


fpg = a.frames_per_gen
times = [i / fpg for i in range((G - 1) * fpg + 1)] + [G - 1] * (a.fps * 4)  # hold last frame 4 s
writer = FFMpegWriter(fps=a.fps, codec="libx264", bitrate=6000, extra_args=["-pix_fmt", "yuv420p"])
with writer.saving(fig, a.out, dpi=120):
    for t in times:
        draw(t)
        writer.grab_frame(facecolor=SURFACE)
fig.savefig(Path(a.out).with_suffix(".png"), facecolor=SURFACE)
print(f"wrote {a.out} ({len(times)} frames)")
