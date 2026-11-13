---
name: file-pr
description: File or update a GitHub PR for a prepared branch when requested, including as part of takeover.
---

# File PR

Use when publishing an already prepared change is part of the user's request.

1. Confirm the intended head repository, branch, and base, and inspect the
   branch diff. Push the prepared branch if needed and authorized. Find any
   open PR for that head and base and update it instead of creating a duplicate.
   If the same head has an open PR against a different base, confirm which PR
   the user wants before opening another.
2. Follow the repository's title and template conventions. Start the body with
   the problem or previous behavior, then describe the change and summarize
   verification. Follow the user's request and repository conventions for draft
   status and model attribution. Use only verified model or host names.
3. Create or update the PR with `gh`. If `gh pr create` hits a GraphQL rate
   limit, check for the matching PR via REST before retrying. If it is absent,
   use `gh api --method POST repos/<owner>/<repo>/pulls` with the resolved
   head and base, title, draft status, and `-F body=@<file>`.
4. Return the PR URL to the caller.
