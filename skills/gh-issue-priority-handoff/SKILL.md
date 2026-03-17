---
name: gh-issue-priority-handoff
description: Analyze GitHub issues for any repository, rank them by importance and business value, and generate copy-paste issue briefs for delegating work to other coding agents. Use when asked to triage backlog, prioritize issues, or split work across multiple agents.
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
1. Scope: all open issues or selected issue numbers.
2. Exclusions: issues already delegated or in progress.
3. Goal: bugfix focus, growth focus, reliability focus, or balanced.
4. Time horizon: urgent sprint, near-term, or strategic roadmap.

If the user does not provide these, proceed with sensible defaults and state assumptions.

## Branch and Worktree Guardrails

Always follow repository rules before writing handoff instructions:
1. Read local `AGENTS.md` if present.
2. Never recommend direct work on protected branches (`master`, `develop`, or repo-defined equivalents).
3. Require each delegated issue to use a dedicated branch and worktree.
4. Include explicit setup commands in each handoff block, for example:

```bash
git fetch origin develop
git worktree add -b codex/issue-<id>-<slug> /path/to/worktrees/issue-<id> origin/develop
cd /path/to/worktrees/issue-<id>
```

If the repo uses a different base branch, replace `develop` accordingly.

## Workflow

1. Gather issue metadata and content.

Use `gh` first:
```bash
gh issue list --state open --limit 200 --json number,title,labels,createdAt,updatedAt,url
gh issue view <number> --json number,title,body,labels,url
```

2. Inspect codebase state for each issue.
- Verify whether issue is already partially or fully implemented.
- Identify likely touched files and architecture dependencies.

3. Score each issue using this rubric.
- `Importance`: Critical / High / Medium / Low
- `Value`: 1-10 (user impact + business impact + data correctness + risk reduction)
- `Effort`: S / M / L / XL
- `Dependency`: blocked-by or blocks-other-work

Suggested weighting:
- User-visible breakage or data integrity: highest
- Security, abuse, or cost-control risks: highest
- Structural unblockers for many downstream tasks: high
- Nice-to-have channels/features without clear demand: lower

4. Produce ranked list.
- Exclude issues user marked as delegated.
- Sort by importance first, then value, then dependency impact.

5. Produce per-issue paragraph + delegation block.
- Paragraph: what problem it solves, why now, expected value, risk if delayed.
- Delegation block: objective, scope, files, acceptance criteria, branch/worktree setup, validation commands.

## Output Contract

Always return these sections in order:

1. `Priority Table`
- Issue, Importance, Value, Effort, Recommendation, Reason

2. `Issue Analysis`
- One paragraph per issue.

3. `Agent Handoff Blocks`
- One copy-paste block per issue.
- Each block must include:
  - issue id and title
  - goal
  - implementation scope
  - target files or modules
  - acceptance criteria
  - required validation commands
  - worktree/branch setup commands

For handoff block format, use:
- `references/handoff-template.md`

## Quality Bar

- Do not rank by title only. Use issue body + code reality.
- Call out stale/duplicate/outdated issues explicitly.
- Keep recommendations actionable; avoid vague prioritization.
- If uncertain, state assumptions and what evidence is missing.
