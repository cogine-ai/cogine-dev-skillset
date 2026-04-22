---
name: peer-review
description: "Independent second-opinion code review using Codex CLI. Use when: wanting an external AI reviewer's perspective, cross-validating before push, getting a second pair of eyes. Triggers on: '/peer-review', 'codex review', 'second opinion', 'peer review my changes'."
allowed-tools: Bash, Read, Grep, Glob
argument-hint: "[--base <branch>] [--uncommitted] [--commit <sha>] [--model <model>] [--focus <area>]"
---

# Peer Review via Codex CLI

Independent code review using OpenAI Codex CLI as a second reviewer agent. Codex runs in a read-only sandbox - it cannot modify any files.

## Why a Second Reviewer

Different model families (Claude vs GPT) have different blind spots. A peer review from a separate agent catches issues that self-review misses, similar to how a human teammate provides a fresh perspective.

## Prerequisites

Codex CLI must be installed and authenticated:
- `codex --version` should return a version
- Codex handles its own auth via `codex login` or config

If not available, inform the user and stop.

## Arguments

- `--base <branch>`: Review changes against a specific base branch
- `--uncommitted`: Review staged, unstaged, and untracked changes
- `--commit <sha>`: Review a specific commit
- `--model <model>`: Override Codex model (default: uses Codex config default)
- `--focus <area>`: Custom focus area passed as review instructions (for example, `security`, `performance`, or `error handling`)

No arguments: auto-detect - if on a feature branch, review against base; otherwise review uncommitted changes.

## Step 0: Preflight

```bash
# Verify Codex CLI is available
codex --version

# Detect review target
BASE=$(gh pr view --json baseRefName -q .baseRefName 2>/dev/null || git rev-parse --verify main 2>/dev/null && echo main || echo master)
```

Determine review mode:
1. If `--uncommitted`, use `--uncommitted`
2. If `--commit <sha>`, use `--commit <sha>`
3. If `--base <branch>`, use `--base <branch>`
4. If on a feature branch with commits ahead of base, use `--base $BASE`
5. If uncommitted changes exist, use `--uncommitted`
6. Otherwise, abort because there is nothing to review

Abort conditions:
- No Codex CLI installed
- No changes to review

## Step 1: Gather Context

Before invoking Codex, gather context to present alongside the review:

```bash
git diff origin/$BASE...HEAD --stat
git log origin/$BASE...HEAD --oneline
```

Report to the user:
- review mode (`branch`, `uncommitted`, or `commit`)
- scope (files changed, lines changed)
- Codex model being used

## Step 2: Run Codex Review

Build and execute the Codex review command. Always use `codex exec review` with `-o` output capture.

```bash
# Base branch review
codex exec review \
  --base "$BASE" \
  --ephemeral \
  -o /tmp/peer-review-output.md \
  "$CUSTOM_INSTRUCTIONS"

# Uncommitted changes
codex exec review \
  --uncommitted \
  --ephemeral \
  -o /tmp/peer-review-output.md \
  "$CUSTOM_INSTRUCTIONS"

# Specific commit
codex exec review \
  --commit "$SHA" \
  --ephemeral \
  -o /tmp/peer-review-output.md \
  "$CUSTOM_INSTRUCTIONS"
```

Base review instructions:

```text
Review this code as a strict but fair peer reviewer. Focus on:
1. Logic bugs and correctness issues
2. Security vulnerabilities (injection, auth bypass, data exposure)
3. Error handling gaps (swallowed errors, missing edge cases)
4. Performance concerns (N+1 queries, unnecessary computation, memory leaks)
5. API contract and type safety issues

For each finding, specify: severity (CRITICAL/WARNING/INFO), file:line, problem description, and suggested fix.
Be concise. Do not praise code - only report issues and improvements.
```

If `--model` is specified, add `-m <model>`.

Set a 120-second timeout. If Codex hangs, kill it and report partial output.

## Step 3: Present Findings

Read the Codex output and present it in a structured format:

```text
## Peer Review (Codex CLI)

Reviewer: Codex CLI v{version} / {model}
Mode: {branch|uncommitted|commit}
Scope: {N} files, {M} lines changed

### Findings

{Codex output, organized by severity}

### Cross-Reference Notes

{Optional notes comparing Codex findings with Claude's own /review}
```

## Step 4: Triage Assistance

After presenting findings, help the user triage them into:

1. Agree - findings that align with your own assessment
2. Disagree - findings you believe are incorrect, with evidence
3. Investigate - findings that need more context

Do not blindly trust Codex findings. Verify technical correctness before recommending action.

## Step 5: Summary

```text
## Peer Review Summary

Reviewer: Codex CLI {version} / {model}
Scope: {description}

CRITICAL: {N} findings
WARNING:  {N} findings
INFO:     {N} findings

Triage:
- Agree:       {N}
- Disagree:    {N}
- Investigate: {N}

Next steps: {recommended follow-up}
```

## Combining with /review

For maximum coverage, run both:
1. `/review` - Claude's self-review
2. `/peer-review` - Codex's independent review

If both reviewers flag the same issue, treat it as highest priority.
