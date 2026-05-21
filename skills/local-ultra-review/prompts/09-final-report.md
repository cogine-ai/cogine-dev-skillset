# Final Report

Write a concise Markdown report. Do not paste raw logs unless needed for a finding.

Required structure:

```markdown
# Local Ultra Review Report

## Scope

- Target:
- Base:
- Head:
- Files changed:
- Lines changed:
- Mode:
- Worktree:
- Commands run:

## Summary

## Important Findings

## Nits

## Pre-existing Issues

## Needs Manual Review

## Reviewer Coverage

## Ignored Paths

## Artifacts
```

Each Important or Nit finding must include:

- title
- severity
- file:line
- what breaks
- why this diff introduced or worsened it
- evidence
- suggested fix direction
- verification

Do not include unverified candidates in Important or Nits.
