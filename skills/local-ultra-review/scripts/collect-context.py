#!/usr/bin/env python3
import argparse
import datetime as dt
import fnmatch
import json
import os
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_IGNORE_PATTERNS = [
    "**/*.lock",
    "**/dist/**",
    "**/build/**",
    "**/generated/**",
    "**/.next/**",
    "**/coverage/**",
    "**/node_modules/**",
    "**/vendor/**",
    "**/__generated__/**",
    "**/*.min.js",
    "**/*.map",
]

INSTRUCTION_FILES = ["REVIEW.md", "AGENTS.md", "CLAUDE.md", "README.md"]
TEST_MARKERS = [".test.", ".spec.", "_test.", "test_", "_test"]


def run(args, cwd, check=False):
    proc = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "command failed")
    return proc


def git(cwd, *args, check=False):
    return run(["git", *args], cwd=cwd, check=check)


def git_text(cwd, *args):
    return git(cwd, *args, check=True).stdout


def detect_repo_root(start):
    return Path(git_text(start, "rev-parse", "--show-toplevel").strip())


def ref_exists(repo, ref):
    return git(repo, "rev-parse", "--verify", f"{ref}^{{commit}}").returncode == 0


def detect_default_base(repo):
    candidates = []
    proc = git(repo, "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD")
    if proc.returncode == 0 and proc.stdout.strip():
        candidates.append(proc.stdout.strip())
    candidates.extend(["origin/main", "origin/master", "main", "master"])
    seen = set()
    for ref in candidates:
        if ref not in seen and ref_exists(repo, ref):
            return ref
        seen.add(ref)
    return "HEAD~1"


def load_ignore_patterns(skill_dir):
    if not skill_dir:
        return DEFAULT_IGNORE_PATTERNS
    path = Path(skill_dir) / "config" / "ignore.yaml"
    if not path.exists():
        return DEFAULT_IGNORE_PATTERNS
    patterns = []
    in_paths = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line == "paths:":
            in_paths = True
            continue
        if line and not raw.startswith(" ") and not raw.startswith("-"):
            in_paths = False
        if in_paths and line.startswith("- "):
            patterns.append(line[2:].strip().strip('"').strip("'"))
    return patterns or DEFAULT_IGNORE_PATTERNS


def ignored(path, patterns):
    normalized = path.replace(os.sep, "/")
    base_variants = {normalized, f"./{normalized}"}
    basename = Path(normalized).name
    for pattern in patterns:
        variants = set(base_variants)
        if "/" not in pattern:
            variants.add(basename)
        if any(fnmatch.fnmatch(variant, pattern) for variant in variants):
            return True
    return False


def parse_name_status(text, source):
    rows = []
    for line in text.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R") or status.startswith("C"):
            path = parts[-1]
            old_path = parts[1] if len(parts) > 2 else ""
        else:
            path = parts[-1]
            old_path = ""
        rows.append({"path": path, "status": status, "old_path": old_path, "source": source})
    return rows


def changed_files(repo, base, head):
    entries = []
    committed = git(repo, "diff", "--name-status", f"{base}...{head}")
    if committed.returncode != 0:
        committed = git(repo, "diff", "--name-status", base, head)
    entries.extend(parse_name_status(committed.stdout, "committed"))
    entries.extend(parse_name_status(git_text(repo, "diff", "--cached", "--name-status"), "staged"))
    entries.extend(parse_name_status(git_text(repo, "diff", "--name-status"), "unstaged"))

    by_path = {}
    for row in entries:
        item = by_path.setdefault(row["path"], {"path": row["path"], "status": row["status"], "old_path": row["old_path"], "sources": []})
        if row["source"] not in item["sources"]:
            item["sources"].append(row["source"])
        if item["status"] == "":
            item["status"] = row["status"]
    return list(by_path.values())


def truncate(text, limit):
    if len(text) <= limit:
        return text, False
    return text[:limit] + "\n[truncated]\n", True


def patch_for(repo, base, head, path, max_chars):
    sections = []
    commands = [
        ("committed", ["diff", "--binary", f"{base}...{head}", "--", path]),
        ("staged", ["diff", "--cached", "--binary", "--", path]),
        ("unstaged", ["diff", "--binary", "--", path]),
    ]
    for source, args in commands:
        proc = git(repo, *args)
        if source == "committed" and proc.returncode != 0:
            proc = git(repo, "diff", "--binary", base, head, "--", path)
        if proc.returncode == 0 and proc.stdout.strip():
            text, was_truncated = truncate(proc.stdout, max_chars)
            sections.append({"source": source, "patch": text, "truncated": was_truncated})
    return sections


def parse_hunk_lines(patch):
    lines = []
    for raw in patch.splitlines():
        if raw.startswith("@@"):
            marker = raw.split("@@")[1].strip()
            plus = [part for part in marker.split() if part.startswith("+")]
            if plus:
                start = plus[0][1:].split(",", 1)[0]
                try:
                    lines.append(max(1, int(start)))
                except ValueError:
                    pass
    return lines[:5]


def nearby_context(repo, file_path, patch_sections, radius=35, max_chars=20000):
    path = repo / file_path
    if not path.exists() or not path.is_file():
        return []
    try:
        content = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return []
    starts = []
    for section in patch_sections:
        starts.extend(parse_hunk_lines(section.get("patch", "")))
    snippets = []
    seen = set()
    used = 0
    for start in starts:
        lo = max(1, start - radius)
        hi = min(len(content), start + radius)
        key = (lo, hi)
        if key in seen:
            continue
        seen.add(key)
        numbered = "\n".join(f"{idx}: {content[idx - 1]}" for idx in range(lo, hi + 1))
        if used + len(numbered) > max_chars:
            numbered = numbered[: max(0, max_chars - used)] + "\n[truncated]\n"
        used += len(numbered)
        snippets.append({"file": file_path, "start_line": lo, "end_line": hi, "content": numbered})
        if used >= max_chars:
            break
    return snippets


def read_instruction_files(repo, max_chars=30000):
    results = []
    for name in INSTRUCTION_FILES:
        path = repo / name
        if path.exists() and path.is_file():
            text, was_truncated = truncate(path.read_text(encoding="utf-8", errors="replace"), max_chars)
            results.append({"path": name, "content": text, "truncated": was_truncated})
    return results


def git_ls_files(repo):
    proc = git(repo, "ls-files")
    if proc.returncode != 0:
        return []
    return [line for line in proc.stdout.splitlines() if line.strip()]


def is_test_file(path):
    name = Path(path).name.lower()
    lowered = path.lower()
    return any(marker in name for marker in TEST_MARKERS) or "/test/" in lowered or "/tests/" in lowered or lowered.startswith("test/")


def related_tests(all_files, changed):
    tests = [path for path in all_files if is_test_file(path)]
    changed_stems = {Path(item["path"]).stem.replace(".test", "").replace(".spec", "") for item in changed}
    selected = []
    for test in tests:
        stem = Path(test).stem.replace(".test", "").replace(".spec", "")
        if stem in changed_stems or any(part and part in test for part in changed_stems):
            selected.append(test)
    return sorted(set(selected))[:100]


def package_scripts(repo):
    scripts = {}
    path = repo / "package.json"
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data.get("scripts"), dict):
                scripts["package.json"] = data["scripts"]
        except Exception:
            scripts["package.json"] = {"_error": "failed to parse package.json"}
    return scripts


def detect_languages(files):
    ext_counter = Counter(Path(path).suffix.lower() or "(none)" for path in files)
    languages = []
    mapping = {
        ".js": "javascript",
        ".jsx": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".py": "python",
        ".go": "go",
        ".rs": "rust",
        ".java": "java",
        ".kt": "kotlin",
        ".rb": "ruby",
        ".php": "php",
        ".cs": "csharp",
        ".sql": "sql",
        ".swift": "swift",
    }
    for ext, count in ext_counter.most_common():
        if ext in mapping:
            languages.append({"language": mapping[ext], "extension": ext, "changed_files": count})
    return languages


def detect_frameworks(repo):
    frameworks = []
    package = repo / "package.json"
    if package.exists():
        try:
            data = json.loads(package.read_text(encoding="utf-8"))
            deps = {}
            deps.update(data.get("dependencies", {}) or {})
            deps.update(data.get("devDependencies", {}) or {})
            for name, label in {
                "next": "nextjs",
                "react": "react",
                "vue": "vue",
                "svelte": "svelte",
                "express": "express",
                "fastify": "fastify",
                "prisma": "prisma",
                "drizzle-orm": "drizzle",
                "jest": "jest",
                "vitest": "vitest",
                "playwright": "playwright",
            }.items():
                if name in deps:
                    frameworks.append(label)
        except Exception:
            pass
    if (repo / "pyproject.toml").exists():
        text = (repo / "pyproject.toml").read_text(encoding="utf-8", errors="replace").lower()
        for needle, label in [("fastapi", "fastapi"), ("django", "django"), ("pytest", "pytest"), ("ruff", "ruff"), ("mypy", "mypy")]:
            if needle in text:
                frameworks.append(label)
    if (repo / "go.mod").exists():
        frameworks.append("go")
    if (repo / "Cargo.toml").exists():
        frameworks.append("rust")
    return sorted(set(frameworks))


def diff_stats(repo, base, head):
    stats = {"files": 0, "additions": 0, "deletions": 0}
    sources = [
        git(repo, "diff", "--numstat", f"{base}...{head}"),
        git(repo, "diff", "--cached", "--numstat"),
        git(repo, "diff", "--numstat"),
    ]
    if sources[0].returncode != 0:
        sources[0] = git(repo, "diff", "--numstat", base, head)
    seen_files = set()
    for proc in sources:
        if proc.returncode != 0:
            continue
        for line in proc.stdout.splitlines():
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            add, delete, path = parts[0], parts[1], parts[-1]
            seen_files.add(path)
            if add.isdigit():
                stats["additions"] += int(add)
            if delete.isdigit():
                stats["deletions"] += int(delete)
    stats["files"] = len(seen_files)
    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--out", required=True)
    parser.add_argument("--skill-dir", default="")
    parser.add_argument("--max-patch-chars", type=int, default=60000)
    args = parser.parse_args()

    repo = detect_repo_root(Path(args.repo))
    base = args.base or detect_default_base(repo)
    head = args.head
    ignore_patterns = load_ignore_patterns(args.skill_dir)
    changed = changed_files(repo, base, head)
    for item in changed:
        item["ignored"] = ignored(item["path"], ignore_patterns)

    patches = []
    contexts = []
    for item in changed:
        if item["ignored"]:
            continue
        sections = patch_for(repo, base, head, item["path"], args.max_patch_chars)
        if sections:
            patches.append({"file": item["path"], "sections": sections})
            contexts.extend(nearby_context(repo, item["path"], sections))

    all_files = git_ls_files(repo)
    changed_paths = [item["path"] for item in changed]
    bundle = {
        "schema_version": "1.0",
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "repo_root": str(repo),
        "base_ref": base,
        "head_ref": git_text(repo, "rev-parse", head).strip(),
        "changed_files": changed,
        "diff_stats": diff_stats(repo, base, head),
        "patches": patches,
        "nearby_context": contexts,
        "related_tests": related_tests(all_files, changed),
        "project_instructions": read_instruction_files(repo),
        "ignored_paths": [item["path"] for item in changed if item["ignored"]],
        "ignore_patterns": ignore_patterns,
        "detected": {
            "languages": detect_languages(changed_paths),
            "frameworks": detect_frameworks(repo),
            "package_scripts": package_scripts(repo),
            "config_files": [path for path in ["package.json", "pyproject.toml", "go.mod", "Cargo.toml", "pom.xml", "build.gradle", "build.gradle.kts"] if (repo / path).exists()],
        },
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(bundle, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "out": str(out), "changed_files": len(changed), "patches": len(patches)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
