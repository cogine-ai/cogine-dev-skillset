#!/usr/bin/env bash
set -u

if ! command -v python3 >/dev/null 2>&1; then
  printf '{"ok":false,"error":"python3 is required","checks":{"python3":false}}\n'
  exit 2
fi

python3 - "$@" <<'PY'
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(args, cwd=None, check=False):
    proc = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "command failed")
    return proc


def command_exists(name):
    return shutil.which(name) is not None


def git_output(args, cwd=None):
    return run(["git", *args], cwd=cwd, check=True).stdout.strip()


def detect_default_base(repo):
    candidates = []
    proc = run(["git", "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"], cwd=repo)
    if proc.returncode == 0 and proc.stdout.strip():
        candidates.append(proc.stdout.strip().replace("origin/", "origin/", 1))
    candidates.extend(["origin/main", "origin/master", "main", "master"])
    seen = set()
    for ref in candidates:
        if ref in seen:
            continue
        seen.add(ref)
        if run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"], cwd=repo).returncode == 0:
            return ref
    return ""


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


result = {
    "ok": False,
    "arguments": " ".join(sys.argv[1:]),
    "checks": {
        "git": command_exists("git"),
        "python3": True,
        "jq": command_exists("jq"),
        "gh": command_exists("gh"),
    },
}

if not result["checks"]["git"]:
    result["error"] = "git is required"
    print(json.dumps(result, indent=2, sort_keys=True))
    sys.exit(2)

try:
    repo_root = git_output(["rev-parse", "--show-toplevel"])
except Exception as exc:
    result["error"] = f"not a git repository: {exc}"
    print(json.dumps(result, indent=2, sort_keys=True))
    sys.exit(2)

repo = Path(repo_root)
branch_proc = run(["git", "branch", "--show-current"], cwd=repo)
head = git_output(["rev-parse", "--short", "HEAD"], cwd=repo)
status = run(["git", "status", "--porcelain=v1"], cwd=repo, check=True).stdout.splitlines()
untracked = [line for line in status if line.startswith("?? ")]
default_base = detect_default_base(repo)

test_commands = []
package_json = repo / "package.json"
if package_json.exists():
    data = read_json(package_json)
    scripts = (data or {}).get("scripts", {}) if isinstance(data, dict) else {}
    for name in ("test", "typecheck", "lint", "build"):
        if name in scripts:
            test_commands.append(f"npm run {name}" if name != "test" else "npm test")
if (repo / "pyproject.toml").exists() or (repo / "pytest.ini").exists() or (repo / "tests").exists():
    for cmd in ("pytest", "mypy", "ruff check"):
        if command_exists(cmd.split()[0]):
            test_commands.append(cmd)
if (repo / "go.mod").exists():
    test_commands.append("go test ./...")
if (repo / "Cargo.toml").exists():
    test_commands.extend(["cargo test", "cargo clippy"])
if (repo / "pom.xml").exists():
    test_commands.append("mvn test")
if (repo / "build.gradle").exists() or (repo / "build.gradle.kts").exists():
    test_commands.append("./gradlew test")

instruction_files = []
for name in ("REVIEW.md", "AGENTS.md", "CLAUDE.md", "README.md"):
    if (repo / name).exists():
        instruction_files.append(name)

result.update({
    "ok": True,
    "repo_root": str(repo),
    "branch": branch_proc.stdout.strip() or "(detached)",
    "head": head,
    "default_base": default_base,
    "base_exists": bool(default_base),
    "working_tree_dirty": bool(status),
    "status_entries": len(status),
    "untracked_entries": len(untracked),
    "include_untracked_default": False,
    "test_commands": test_commands,
    "instruction_files": instruction_files,
})

summary = [
    "Local Ultra Review preflight",
    f"- repo: {repo}",
    f"- branch: {result['branch']}",
    f"- head: {head}",
    f"- default base: {default_base or '(not found)'}",
    f"- dirty entries: {len(status)}",
    f"- untracked entries: {len(untracked)}",
    f"- tools: git={result['checks']['git']} python3=True jq={result['checks']['jq']} gh={result['checks']['gh']}",
    f"- test commands: {', '.join(test_commands) if test_commands else '(none detected)'}",
    f"- instructions: {', '.join(instruction_files) if instruction_files else '(none found)'}",
]
print("\n".join(summary), file=sys.stderr)
print(json.dumps(result, indent=2, sort_keys=True))
PY
