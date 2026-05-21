#!/usr/bin/env bash
set -u

RUN="false"
OUT_DIR=".local-ultra-review/checks"
TIMEOUT_SECONDS="300"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --run)
      RUN="true"
      shift
      ;;
    --dry-run)
      RUN="false"
      shift
      ;;
    --out)
      OUT_DIR="${2:-}"
      shift 2
      ;;
    --timeout)
      TIMEOUT_SECONDS="${2:-300}"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

python3 - "$RUN" "$OUT_DIR" "$TIMEOUT_SECONDS" <<'PY'
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


run_checks = sys.argv[1] == "true"
out_dir = Path(sys.argv[2])
timeout = int(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)
logs_dir = out_dir / "logs"
logs_dir.mkdir(exist_ok=True)


def command_exists(command):
    return shutil.which(command) is not None


def detect_commands(repo):
    commands = []
    package = repo / "package.json"
    if package.exists():
        try:
            data = json.loads(package.read_text(encoding="utf-8"))
            scripts = data.get("scripts", {}) or {}
            for name in ("typecheck", "test", "lint", "build"):
                if name in scripts:
                    commands.append({"name": name, "command": "npm test" if name == "test" else f"npm run {name}", "source": "package.json"})
        except Exception:
            pass
    if (repo / "pyproject.toml").exists() or (repo / "pytest.ini").exists() or (repo / "tests").exists():
        for name, cmd in [("pytest", "pytest"), ("mypy", "mypy"), ("ruff", "ruff check")]:
            if command_exists(cmd.split()[0]):
                commands.append({"name": name, "command": cmd, "source": "python"})
    if (repo / "go.mod").exists():
        commands.append({"name": "go-test", "command": "go test ./...", "source": "go.mod"})
    if (repo / "Cargo.toml").exists():
        commands.append({"name": "cargo-test", "command": "cargo test", "source": "Cargo.toml"})
        commands.append({"name": "cargo-clippy", "command": "cargo clippy", "source": "Cargo.toml"})
    if (repo / "pom.xml").exists():
        commands.append({"name": "mvn-test", "command": "mvn test", "source": "pom.xml"})
    if (repo / "build.gradle").exists() or (repo / "build.gradle.kts").exists():
        commands.append({"name": "gradle-test", "command": "./gradlew test", "source": "gradle"})
    return commands


repo_proc = subprocess.run(["git", "rev-parse", "--show-toplevel"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
repo = Path(repo_proc.stdout.strip()) if repo_proc.returncode == 0 else Path.cwd()
commands = detect_commands(repo)
results = []

for item in commands:
    log_path = logs_dir / f"{item['name']}.log"
    if not run_checks:
        results.append({**item, "status": "planned", "log": str(log_path)})
        continue
    try:
        proc = subprocess.run(item["command"], cwd=repo, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        log_path.write_text(proc.stdout, encoding="utf-8", errors="replace")
        results.append({**item, "status": "passed" if proc.returncode == 0 else "failed", "exit_code": proc.returncode, "log": str(log_path)})
    except subprocess.TimeoutExpired as exc:
        log_path.write_text(exc.stdout or "", encoding="utf-8", errors="replace")
        results.append({**item, "status": "timeout", "exit_code": 124, "log": str(log_path)})

summary = {"ok": True, "dry_run": not run_checks, "repo_root": str(repo), "timeout_seconds": timeout, "commands": results}
(out_dir / "checks.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2, sort_keys=True))
PY
