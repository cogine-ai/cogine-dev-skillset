---
name: loop-on-pr-review-and-fix
description: Create and run a post-PR review loop for a ready-for-review GitHub pull request. Use when the user asks Codex or Claude Code to watch, loop on, monitor, periodically check, or automatically handle PR review feedback after a PR has been opened. In Codex, the default behavior is to create a 10-minute heartbeat automation first, not to perform an ordinary one-off fix; only execute the review/fix iteration when the skill is invoked by that automation or the user explicitly asks for one immediate pass.
---

# Loop on PR Review and Fix

## Overview

Use this after a PR is open and ready for review. In Codex, first create a heartbeat automation that wakes every 10 minutes. The automation then runs one review-check iteration per wakeup.

The hard part is state, not waiting. Persist what was already fixed, skipped, obsolete, or resolved so repeated wakeups do not re-handle old feedback.

## Entry Decision

Classify the current invocation before doing any PR review work:

- **Setup Mode**: The user asks to start, create, run, enable, watch, monitor, loop on, or automatically handle PR reviews. In Codex, create a heartbeat automation and stop. Do not inspect review comments or make fixes in this setup turn unless the user explicitly says to also run an immediate pass now.
- **Iteration Mode**: The invocation comes from the heartbeat automation, or the user explicitly asks to run one pass now. Run exactly one review-check iteration and then return control to the scheduler.
- **Claude Code Mode**: The user is not in Codex automation but wants a Claude Code loop. Provide or run an explicit agent loop with 10-minute waits, but keep code changes agent-driven, not shell-only.

If unsure, prefer Setup Mode. This skill exists to create a loop, not to replace a normal one-off PR feedback fix.

## Setup Mode: Create Codex Automation

In Codex, use the Codex automation tool directly. When the app exposes `codex_app.automation_update`, call it to create a heartbeat attached to the current thread:

- `mode`: create
- `kind`: heartbeat
- `destination`: thread
- cadence: every 10 minutes
- `status`: ACTIVE
- `name`: `Loop on PR review: <owner/repo>#<pr-number>`
- `prompt`: include the absolute repo path, PR URL/number, and the Iteration Mode instructions below

Prefer a heartbeat over a detached cron job for this skill. Do not satisfy Setup Mode by doing a manual PR review pass, running `sleep`, writing a reminder in prose, or leaving the user with instructions to create the automation themselves.

The automation prompt must be self-contained. Use this shape:

```text
Use $loop-on-pr-review-and-fix in Iteration Mode for PR <PR_URL_OR_NUMBER> in <ABSOLUTE_REPO_PATH>. Run exactly one review-check iteration. Fetch the current PR review state, compare it with the local state file, ignore already handled, resolved, obsolete, duplicate, not-actionable, or intentionally skipped feedback, fix and push only new actionable feedback, update the state file, increment quiet rounds when there is no new actionable feedback, and stop or pause this heartbeat automation after three consecutive quiet rounds. Do not sleep inside this run.
```

After creating the automation, tell the user the PR, repo path, cadence, and stop condition. Do not perform ordinary fix work in the setup response.

## Resolve Context

Use this section in Setup Mode only to resolve enough information to create the automation. Use it fully in Iteration Mode before editing code.

1. Confirm the current directory is the repository for the PR.
2. Resolve the active PR from the current branch or the user-provided PR URL/number.
3. Resolve the repo, PR number, PR URL, head branch, base branch, and current head SHA.
4. Read repo instructions such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, and project-specific agent docs before editing.
5. Initialize the local state file:

```bash
python3 ~/.codex/skills/loop-on-pr-review-and-fix/scripts/review_loop_state.py init \
  --pr "$PR_NUMBER" \
  --repo "$OWNER_REPO" \
  --pr-url "$PR_URL" \
  --head-sha "$HEAD_SHA"
```

If no PR can be resolved, ask for the PR URL or number instead of starting a loop.

## Fetch Review State

Use the GitHub connector if available. With `gh`, collect both PR-level comments and review threads. Prefer thread data because it exposes resolved and outdated status.

Useful starting commands:

```bash
gh pr view "$PR_NUMBER" --json number,url,headRefName,headRefOid,baseRefName,reviewDecision,reviews,comments,latestReviews,statusCheckRollup
gh pr view "$PR_NUMBER" --comments
```

If `gh pr view` does not expose review threads in JSON, use `gh api graphql` for `PullRequest.reviewThreads`, including thread id, `isResolved`, comment ids, author, body, path, line/originalLine, outdated status, created time, URL, and diff hunk.

Use stable item ids when comparing to state. Prefer `comment:<comment-id>` for individual comments and `thread:<thread-id>` for thread-level decisions.

## Classify Feedback

Treat every review comment as a claim to verify against current code, not as an instruction to apply blindly.

Actionable feedback must be new and still valid. Exclude:

- Items already recorded as `fixed`, `skipped`, `not-actionable`, `obsolete`, `duplicate`, or `resolved`.
- Resolved review threads.
- Outdated comments whose referenced code has changed and whose concern no longer applies.
- Repeated bot comments that match an already handled issue.
- Reviewer acknowledgements, praise, questions already answered, or status chatter.
- Comments the user or prior loop explicitly decided not to fix.

If a handled thread receives a new unhandled comment, treat only the new comment as fresh.

## Iteration Mode: One Review Check

Run exactly one iteration when invoked by Codex heartbeat automation or when the user explicitly asks for one immediate pass.

1. Fetch latest remote refs and PR review state.
2. Compare live review items with the local state file.
3. If there are no new actionable items:
   - Increment quiet rounds.
   - Stop or pause the heartbeat automation when quiet rounds reaches 3. If the current automation cannot be resolved by the available tool context, report `stop: true` clearly and do not create a replacement automation.
   - Otherwise let the scheduler wake the task again in 10 minutes.
4. If there are new actionable items:
   - Reset quiet rounds.
   - Inspect the current code and verify each finding.
   - Make the smallest correct fix for still-valid issues.
   - Run focused validation, then broader validation if shared contracts or user-facing behavior changed.
   - Stage only files that belong to the fix.
   - Commit and push to the PR branch.
   - Mark each handled item in the state file with `fixed`, `skipped`, `not-actionable`, `obsolete`, `duplicate`, or `resolved` and a short reason.
   - Optionally reply on the PR with a concise summary if that is the repo's convention.

State helper examples:

```bash
python3 ~/.codex/skills/loop-on-pr-review-and-fix/scripts/review_loop_state.py unseen --pr "$PR_NUMBER" comment:abc thread:def
python3 ~/.codex/skills/loop-on-pr-review-and-fix/scripts/review_loop_state.py quiet --pr "$PR_NUMBER" --increment --stop-after 3
python3 ~/.codex/skills/loop-on-pr-review-and-fix/scripts/review_loop_state.py quiet --pr "$PR_NUMBER" --reset
python3 ~/.codex/skills/loop-on-pr-review-and-fix/scripts/review_loop_state.py mark --pr "$PR_NUMBER" --item-id comment:abc --status fixed --note "Adjusted validation path" --head-sha "$NEW_HEAD_SHA"
```

## Claude Code Loop

In Claude Code, keep the loop explicit:

1. Run one iteration using this skill.
2. If the state helper reports stop, end the loop.
3. Otherwise wait 10 minutes and repeat.

Do not let a shell-only loop make code changes. The agent must inspect feedback, verify it against current code, edit, validate, commit, and push each round.

## Guardrails

- Do not fix stale, resolved, duplicate, or intentionally skipped review feedback.
- Do not mark an item `fixed` until the relevant commit has been created and pushed.
- Preserve unrelated user changes and untracked files.
- Do not broaden scope without user approval.
- Do not bypass tests, hooks, or CI failures to make the loop progress.
- If review feedback is ambiguous or product-level, ask instead of guessing.
- If authentication, branch protection, merge conflicts, or failing validation blocks progress, report the blocker and keep the state accurate.

## Output

Report:

- PR URL and branch.
- New actionable review items handled.
- Items skipped as duplicate, resolved, obsolete, or not actionable.
- Commits pushed.
- Validation commands and outcomes.
- Current quiet-round count and whether the loop continues or stops.
