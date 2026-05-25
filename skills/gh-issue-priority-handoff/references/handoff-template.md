# Issue Handoff Template

Use this template for each delegated issue.

```text
Issue: #<id> <title>
URL: <url>
Repository: <owner/repo or local path>
Base ref: <origin/main, origin/develop, or local ref with caveat>

Evidence checked:
- <issue body/comment/linked PR detail>
- <current code or doc path checked>
- <test/validation surface checked>

Setup (must use dedicated worktree + branch):
BASE_BRANCH=<detected-base-branch>
git fetch origin "$BASE_BRANCH"
git worktree add -b codex/issue-<id>-<slug> /path/to/worktrees/issue-<id> "origin/$BASE_BRANCH"
cd /path/to/worktrees/issue-<id>

Objective:
<one clear sentence>

Scope:
- <change 1>
- <change 2>
- <change 3>

Non-goals:
- <what the agent should not change>

Target files/modules:
- <path 1>
- <path 2>

Acceptance criteria:
- [ ] <observable result 1>
- [ ] <observable result 2>
- [ ] <observable result 3>

Validation:
- <repo-specific lint/typecheck command>
- <repo-specific test command>
- <repo-specific build or smoke command>

Notes:
- Do not push to protected branches.
- Replace placeholders with actual repo paths, branch names, and commands before delegating.
- If blocked, report exact blocker and attempted fix.
```
