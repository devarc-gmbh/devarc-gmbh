#!/usr/bin/env bash
# Full Prompt DNA pipeline: tests -> pilot -> decision -> seeds 1..5 -> analysis.
# Commits and pushes to branch prompt-dna after every milestone. Resumable: re-run after a crash.
set -uo pipefail
cd "$(dirname "$0")"
BR=prompt-dna
PY="$PWD/.venv/bin/python"
if [ ! -x "$PY" ]; then python3 -m venv .venv && .venv/bin/pip install -q --upgrade pip -r requirements.txt; fi
TRAILER=$'\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_019THkovUT33xNb1qyFian8W'

push() {  # $1 = commit message
  git add -A && git commit -q -m "$1$TRAILER" || true
  for d in 2 4 8 16; do git push -q -u origin "$BR" && return 0; sleep "$d"; done
  git push -u origin "$BR"
}
blocked() {  # $1 = reason
  {
    echo "# BLOCKED"; echo; echo "Stopped at: $(date -u +%FT%TZ)"; echo; echo "Reason: $1"; echo
    echo "Done so far: see git log, results/, DECISION.md."; echo
    echo "Next step: fix the reason above, then run \`./run_all.sh\` again (it resumes from checkpoints)."
  } > BLOCKED.md
  push "BLOCKED: $1"; exit 1
}
mod() { (cd src && "$PY" -m promptdna "$@"); }

"$PY" -m pytest -q tests || blocked "offline tests fail"
[ -n "${ANTHROPIC_API_KEY:-}" ] || blocked "ANTHROPIC_API_KEY is not set"

if [ ! -f results/pilot/pilot_report.json ]; then
  mod pilot; rc=$?
  [ $rc -eq 0 ] || blocked "pilot failed with exit code $rc"
  push "Pilot: 1 generation x 3 populations with Haiku and Sonnet players"
fi
if [ ! -f config/locked.json ]; then
  mod decide || blocked "decision step failed"
  push "Lock player model by pre-registered rule (DECISION.md)"
fi
seed_done() {  # 0 if seed $1 has all locked generations
  "$PY" - "$1" <<'PYEOF'
import json, sys, pathlib
lk = json.loads(pathlib.Path("config/locked.json").read_text())
ck = pathlib.Path(f"results/seed-{sys.argv[1]}/checkpoint.json")
sys.exit(0 if ck.exists() and json.loads(ck.read_text())["next_gen"] >= lk["generations"] else 1)
PYEOF
}
for s in 1 2 3 4 5; do   # fixed order, seed 1 = main story seed; never skipped by outcome
  while ! seed_done "$s"; do
    mod run --seed "$s" --max-gens 5; rc=$?
    mod analyze > /dev/null
    case $rc in
      0) push "Seed $s: progress checkpoint" ;;
      3) push "Seed $s stopped at budget limit"; blocked "budget limit reached during seed $s" ;;
      4) push "Seed $s fatal API error"; blocked "fatal API error (credentials/billing) during seed $s" ;;
      5) push "Seed $s stopped: invalid rate above 5%"; blocked "invalid-rate stop in seed $s, see results/seed-$s/DIAGNOSIS-*.md" ;;
      *) push "Seed $s interrupted (exit $rc)"; blocked "seed $s exited with code $rc" ;;
    esac
  done
  push "Seed $s complete"
done
mod analyze > /dev/null
rm -f BLOCKED.md
push "Analysis: summary.md, metrics.csv, sentence families"
