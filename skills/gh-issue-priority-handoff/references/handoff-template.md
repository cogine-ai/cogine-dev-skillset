# Issue Handoff Template

Use this template for each delegated issue.

```text
Issue: #<id> <title>
URL: <url>

Setup (must use dedicated worktree + branch):
git fetch origin develop
git worktree add -b codex/issue-<id>-<slug> /path/to/worktrees/issue-<id> origin/develop
cd /path/to/worktrees/issue-<id>

Objective:
<one clear sentence>

Scope:
- <change 1>
- <change 2>
- <change 3>

Target files/modules:
- <path 1>
- <path 2>

Acceptance criteria:
- [ ] <observable result 1>
- [ ] <observable result 2>
- [ ] <observable result 3>

Validation:
- pnpm lint
- pnpm test
- pnpm build

Notes:
- Do not push to protected branches.
- If blocked, report exact blocker and attempted fix.
```
