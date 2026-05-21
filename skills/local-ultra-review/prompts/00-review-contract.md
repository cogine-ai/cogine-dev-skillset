# Review Contract

Use this contract for every reviewer pass.

## Goal

Find real bugs introduced or worsened by the reviewed diff. Optimize for high precision. A short report with two confirmed bugs is better than a long report of weak suggestions.

## Do Report

Report a candidate only when all of these are true:

1. The issue has a concrete failure scenario.
2. The issue is tied to exact `file:line`.
3. The issue is plausibly introduced or worsened by the current diff.
4. The evidence points to a specific code path, contract, state transition, or runtime condition.
5. There is a verification plan: command, targeted test, static reasoning path, or base-vs-head comparison.

## Do Not Report

Do not report:

- style, naming, formatting, or preference issues
- vague maintainability advice
- "could be cleaner" or "consider refactoring" comments
- generic security checklist items without a reachable path
- missing tests by itself as Important
- issues already enforced by CI unless the CI blind spot is part of the bug
- generated files, lockfiles, vendored code, or ignored paths unless the diff changes runtime behavior
- findings without a file and line
- findings that require guessing hidden product intent

## Candidate Output

Return candidates as JSON objects matching `schemas/candidate-finding.schema.json`. Use JSONL if returning multiple candidates.

Allowed severities:

- `Important`
- `Nit`
- `Pre-existing`
- `NeedsManualReview`

Use `NeedsManualReview` for plausible risks that need a domain owner or runtime environment to confirm. Do not promote them to Important or Nit.

## Evidence Standard

Each candidate must answer:

- What breaks?
- Under what input, user action, request, migration, retry, race, or deploy condition?
- Why is this diff responsible?
- What code evidence supports it?
- How should a verifier confirm or reject it?
