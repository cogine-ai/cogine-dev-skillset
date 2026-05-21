#!/usr/bin/env python3
import json
import shutil
import subprocess
from pathlib import Path


def run(args, cwd):
    return subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def repo_root():
    proc = run(["git", "rev-parse", "--show-toplevel"], Path("."))
    if proc.returncode == 0:
        return Path(proc.stdout.strip())
    return Path(".").resolve()


def command_exists(command):
    return shutil.which(command) is not None


def package_scripts(repo):
    path = repo / "package.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        scripts = data.get("scripts", {})
        return scripts if isinstance(scripts, dict) else {}
    except Exception:
        return {}


def git_files(repo):
    proc = run(["git", "ls-files"], repo)
    if proc.returncode != 0:
        return []
    return proc.stdout.splitlines()


def is_test_file(path):
    lowered = path.lower()
    name = Path(path).name.lower()
    return (
        "/test/" in lowered
        or "/tests/" in lowered
        or lowered.startswith("test/")
        or ".test." in name
        or ".spec." in name
        or name.startswith("test_")
        or name.endswith("_test.go")
        or name.endswith("_test.py")
    )


def main():
    repo = repo_root()
    scripts = package_scripts(repo)
    commands = []
    if scripts:
        for name in ("test", "typecheck", "lint", "build"):
            if name in scripts:
                commands.append({"name": name, "command": "npm test" if name == "test" else f"npm run {name}", "source": "package.json"})
    if (repo / "pyproject.toml").exists() or (repo / "pytest.ini").exists() or (repo / "tests").exists():
        for cmd in ("pytest", "mypy", "ruff check"):
            if command_exists(cmd.split()[0]):
                commands.append({"name": cmd.split()[0], "command": cmd, "source": "python"})
    if (repo / "go.mod").exists():
        commands.append({"name": "go test", "command": "go test ./...", "source": "go.mod"})
    if (repo / "Cargo.toml").exists():
        commands.extend([
            {"name": "cargo test", "command": "cargo test", "source": "Cargo.toml"},
            {"name": "cargo clippy", "command": "cargo clippy", "source": "Cargo.toml"},
        ])
    if (repo / "pom.xml").exists():
        commands.append({"name": "mvn test", "command": "mvn test", "source": "pom.xml"})
    if (repo / "build.gradle").exists() or (repo / "build.gradle.kts").exists():
        commands.append({"name": "gradle test", "command": "./gradlew test", "source": "gradle"})

    tests = sorted(path for path in git_files(repo) if is_test_file(path))
    print(json.dumps({"repo_root": str(repo), "commands": commands, "test_files": tests[:200], "test_file_count": len(tests)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
