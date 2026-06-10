# Subagent Policy Reference

Goal mode plus subagents can improve throughput only when the main agent keeps ownership.

## Ownership

Main agent owns:

- Scope.
- Product judgment.
- Architecture judgment.
- Final diff.
- Verification.
- User communication.

Subagents may own only bounded local work:

- Research scout: read docs/code and return evidence.
- Plan critic: review plan/contract for missing scope, non-goals, acceptance, or drift risk.
- Diff reviewer: inspect current diff for bugs, unrelated changes, content mismatch, or missing tests.
- Verifier: run narrow commands or browser checks from a given checklist.
- Narrow implementer: only when the file boundary and allowed edits are explicit.

Subagents must not:

- Create or modify goals.
- Expand scope.
- Decide product direction.
- Make cross-system architecture decisions.
- Commit, push, or open PRs.
- Change files outside the allowed scope.
- Convert design/doc implications into implementation scope.

## Delegation Brief

Before spawning a subagent, the main agent must define:

```text
Task:
Mode: research / review / verify / implement
Allowed scope:
Forbidden scope:
Allowed tools:
Expected output:
Stop condition:
```

The subagent must return:

```text
Findings:
Evidence:
Contract impact:
- in scope / out of scope / requires user decision
```

The main agent must verify and integrate. Subagents never own final scope or final decisions.

## Example Brief

```text
Task:
Review the current /privacy implementation for content risk.

Mode:
review

Allowed scope:
- Read the confirmed Goal Description.
- Read relevant product/design docs.
- Read the current privacy page implementation and directly related analytics/auth/billing references if needed.

Forbidden scope:
- Do not edit files.
- Do not propose new pages unless marked as out of scope.
- Do not expand scope to Terms, Billing Terms, zh, or analytics consent implementation.

Allowed tools:
- File reads.
- rg searches.
- Narrow command checks only if explicitly listed.

Expected output:
- Findings ordered by severity.
- Evidence with file paths.
- Whether each finding blocks the current goal.
- Suggested minimal fix, if in scope.

Stop condition:
- Stop if the finding requires a product/legal decision outside the confirmed Goal Description.
```
