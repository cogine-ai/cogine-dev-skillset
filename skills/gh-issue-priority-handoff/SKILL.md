---
name: gh-issue-priority-handoff
description: Use when the user asks to triage GitHub issues, prioritize backlog work, decide which issues are still valid, or generate delegation-ready issue briefs for coding agents.
---

# GH Issue Priority Handoff

## Trigger

Use this skill when the user asks to:
- analyze open GitHub issues
- rank issues by priority, impact, or value
- generate delegation-ready instructions for other coding agents
- create a backlog execution sequence

## Inputs to Clarify

Collect these before scoring:
1. Repository: local checkout, `owner/repo`, or current directory.
2. Scope: all open issues, selected issue numbers, labels, milestone, or search query.
3. Exclusions: issues already delegated, in progress, intentionally deferred, or out of scope.
4. Goal: bugfix focus, growth focus, reliability focus, cost/security focus, or balanced.
5. Time horizon: urgent sprint, near-term, or strategic roadmap.

If the user does not provide these, proceed with sensible defaults and state assumptions.

## Freshness and Repo Guardrails

Before ranking or writing handoff instructions:
1. Read local `AGENTS.md` and repo docs if present.
2. Identify the repo default/base branch. Prefer `gh repo view --json defaultBranchRef`, then `git symbolic-ref --short refs/remotes/origin/HEAD`, then the current branch.
3. Fetch the base branch when a remote exists. If the repo has no remote or fetch fails, say that freshness is limited to local state.
4. Check whether the current checkout is dirty. Do not ask delegated agents to build on unrelated local changes unless the user explicitly requests it.
5. Never recommend direct work on protected branches (`main`, `master`, `develop`, release branches, or repo-defined equivalents).
6. Default each delegated issue to a dedicated branch and worktree.
7. Include explicit setup commands in each handoff block using the detected base branch, for example:

```bash
BASE_BRANCH=<detected-base-branch>
git fetch origin "$BASE_BRANCH"
git worktree add -b codex/issue-<id>-<slug> /path/to/worktrees/issue-<id> "origin/$BASE_BRANCH"
cd /path/to/worktrees/issue-<id>
```

If there is no usable remote, replace `origin/$BASE_BRANCH` with the best local base ref and state the limitation.

## Workflow

1. Gather issue metadata, body, comments, and linked closure context.

Use `gh` first:
```bash
gh issue list --state open --limit 200 --json number,title,labels,assignees,createdAt,updatedAt,url,state
gh issue view <number> --comments --json number,title,body,labels,comments,assignees,closedByPullRequestsReferences,createdAt,updatedAt,url,state
```

2. Inspect codebase state for each issue.
- Treat each issue as a claim to verify against current code, not as an instruction to apply blindly.
- Verify whether the issue is still reproducible, already partially implemented, fully fixed, duplicated, or superseded.
- Identify likely touched files, architecture dependencies, and existing tests or validation commands.

3. Classify handoff readiness before scoring.
- `Hand off now`: valid, bounded, agent-executable, and valuable.
- `Needs human/product`: valid problem but acceptance criteria or direction is missing.
- `Defer`: valid but low value, high opportunity cost, or blocked by another issue.
- `Close/skip`: stale, duplicate, already fixed, invalid, or not worth agent time.

4. Score valid issues using this rubric.
- `Importance`: Critical / High / Medium / Low
- `Value`: 1-10 (user impact + business impact + data correctness + risk reduction)
- `Effort`: S / M / L / XL
- `Dependency`: blocked-by or blocks-other-work

Suggested weighting:
- User-visible breakage or data integrity: highest
- Security, abuse, or cost-control risks: highest
- Structural unblockers for many downstream tasks: high
- Nice-to-have channels/features without clear demand: lower

5. Produce ranked list.
- Exclude issues user marked as delegated or in progress.
- Sort handoff-ready issues by importance first, then value, then dependency impact.
- Keep skipped/deferred issues visible with a brief reason instead of silently dropping them.

6. Produce per-issue paragraph + delegation block for handoff-ready issues only.
- Paragraph: what problem it solves, why now, expected value, risk if delayed, and what evidence was checked.
- Delegation block: objective, scope, non-goals, files, acceptance criteria, branch/worktree setup, validation commands.

## Output Contract

Always return these sections in order:

1. `Freshness and Assumptions`
- Repo/ref checked, issue scope, base branch, fetch status, and any freshness caveat.

2. `Priority Table`
- Issue, Status, Importance, Value, Effort, Recommendation, Reason

3. `Issue Analysis`
- One paragraph per issue, including skipped/deferred issues.

4. `Agent Handoff Blocks`
- One copy-paste block per handoff-ready issue.
- Each block must include:
  - issue id and title
  - URL
  - goal
  - implementation scope
  - non-goals
  - target files or modules
  - acceptance criteria
  - required validation commands
  - worktree/branch setup commands
- If no issues are handoff-ready, say so and do not fabricate blocks.

5. `Skipped or Needs Follow-up`
- Issues not handed off, with one-line reasons.

For handoff block format, use:
- `references/handoff-template.md`

## Quality Bar

- Do not rank by title only. Use issue body + code reality.
- Check comments and linked closing PR references when available.
- Call out stale, duplicate, outdated, already-fixed, or not-agent-ready issues explicitly.
- Use repo-specific validation commands from package scripts, test config, Makefiles, CI config, or docs. Do not default to `pnpm` unless the repo actually uses it.
- Keep recommendations actionable; avoid vague prioritization.
- Keep handoff blocks self-contained enough for another coding agent to start without rereading this analysis.
- If uncertain, state assumptions and what evidence is missing.
