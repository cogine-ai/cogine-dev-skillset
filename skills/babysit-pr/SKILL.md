---
name: babysit-pr
description: Follow a GitHub PR through CI and review to a requested outcome, including as part of takeover.
---

# Babysit PR

Use when following an existing PR is part of the user's request. Default to
following through required checks and review, then report any remaining
approval. Fix, push, post replies, resolve threads, or merge within the
user's authorization for those actions.

1. Resolve the live PR, head SHA, and base. Read existing checks and review
   feedback before waiting. Use `gh pr view` for review and merge state and
   `gh pr checks` for PR checks. Use `--required` for reported required
   checks and verify the repository rules if an expected check is missing.
2. Follow CodeRabbit as the primary automated reviewer where used. Include QA,
   human reviews, and other bots as configured or requested. Use the repository
   rules and the user's request to determine what must finish. Keep optional
   results separate and distinguish pending, failed, and completed reviews.
3. Verify each actionable finding against the current code. Focus authorized
   fixes on real issues, test before pushing, and use
   `leaving-pr-comments` for any authorized reply.
   Preserve the context of existing review threads.
4. Follow the PR in the current task using one watcher. For reported pending
   required checks, use `gh pr checks --required --watch --fail-fast`.
   Refresh the live PR periodically when waiting for review. Re-read reviews
   and checks after each push and whenever the head or relevant base changes.
5. Stop when the requested outcome is reached, the PR closes, or a decision
   outside the granted scope is needed. Report CI, review, and any remaining
   approval separately. Check GitHub's live review decision and merge state
   before saying a PR is ready.
