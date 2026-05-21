#!/usr/bin/env bash
set -euo pipefail

BASE_REF=""
HEAD_REF="HEAD"
OUT_DIR=".local-ultra-review/diff"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --base)
      BASE_REF="${2:-}"
      shift 2
      ;;
    --head)
      HEAD_REF="${2:-HEAD}"
      shift 2
      ;;
    --out)
      OUT_DIR="${2:-}"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

if [ -z "$BASE_REF" ]; then
  if git rev-parse --verify origin/main >/dev/null 2>&1; then
    BASE_REF="origin/main"
  elif git rev-parse --verify main >/dev/null 2>&1; then
    BASE_REF="main"
  else
    BASE_REF="HEAD~1"
  fi
fi

mkdir -p "$OUT_DIR"
git diff --stat "$BASE_REF...$HEAD_REF" > "$OUT_DIR/diff-stat.txt" || git diff --stat "$BASE_REF" "$HEAD_REF" > "$OUT_DIR/diff-stat.txt"
git diff --binary "$BASE_REF...$HEAD_REF" > "$OUT_DIR/diff.patch" || git diff --binary "$BASE_REF" "$HEAD_REF" > "$OUT_DIR/diff.patch"
git diff --name-status "$BASE_REF...$HEAD_REF" > "$OUT_DIR/name-status.txt" || git diff --name-status "$BASE_REF" "$HEAD_REF" > "$OUT_DIR/name-status.txt"

python3 - "$BASE_REF" "$HEAD_REF" "$OUT_DIR" <<'PY'
import json
import sys
from pathlib import Path

base, head, out_dir = sys.argv[1:4]
out = Path(out_dir)
result = {
    "base_ref": base,
    "head_ref": head,
    "out_dir": str(out),
    "files": {
        "diff_stat": str(out / "diff-stat.txt"),
        "patch": str(out / "diff.patch"),
        "name_status": str(out / "name-status.txt"),
    },
}
print(json.dumps(result, indent=2, sort_keys=True))
PY
