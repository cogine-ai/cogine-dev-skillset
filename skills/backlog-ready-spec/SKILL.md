---
name: backlog-ready-spec
description: Use when turning vague product requests, founder notes, GitHub issues, roadmap bullets, bug reports, or feature ideas into backlog-ready specs or executable GitHub issues.
---

# Backlog Ready Spec

Use this skill to turn ambiguous work into a ready issue or implementation spec. The output must be specific enough for another coding agent to execute without guessing product intent.

## Core Rule

Do not merely rewrite the user's wording. Verify what already exists, remove duplicates, define boundaries, and state a readiness verdict.

## Inputs

Accept any of these:

- Product brief or founder handoff.
- GitHub issue number or issue text.
- Roadmap bullet.
- Bug report.
- User story.
- Conversation summary.

If the source is ambiguous, ask only for the missing decision that changes the spec materially. Otherwise proceed with stated assumptions.

## Workflow

1. Identify the target repository and scope.
   - Confirm whether the output should be a new issue, an update to an existing issue, or a local spec.
   - If using GitHub, fetch current issues before drafting.

2. De-duplicate first.
   - Search open and recently closed issues by keywords, affected modules, and user-visible behavior.
   - Search the codebase for existing implementation, partial implementation, TODOs, and related tests.
   - If the work is duplicate, obsolete, or already implemented, output `VERDICT: NOT NEEDED` with evidence.

3. Read enough code to make the spec executable.
   - Identify likely files, modules, APIs, routes, database tables, prompts, jobs, or tests.
   - Do not invent file paths.
   - If the affected area cannot be identified, mark that as an open question.

4. Define the contract.
   - User outcome.
   - In-scope behavior.
   - Out-of-scope behavior.
   - Acceptance criteria.
   - Validation commands or manual checks.
   - Risks and dependencies.

5. Redact and tighten.
   - Remove secrets, customer data, internal-only links, and unrelated conversation context.
   - Replace vague words like "better", "fast", "smart", or "support" with observable behavior.

6. Emit the readiness verdict.
   - `READY`: implementable now.
   - `READY WITH RISKS`: implementable, but risks or assumptions must be visible.
   - `NOT READY`: missing a decision that would materially change implementation.
   - `NOT NEEDED`: duplicate, obsolete, already implemented, or out of scope.

## Output Contract

Use this structure:

```markdown
## Backlog Ready Spec

### Verdict
READY / READY WITH RISKS / NOT READY / NOT NEEDED

### Source
Brief / issue / roadmap item:
Related issues:
Related code:

### User Outcome
What changes for the user.

### Problem
Current behavior or missing capability.

### Scope
In:
- <in-scope item>

Out:
- <out-of-scope item>

### Proposed Implementation Direction
Likely files/modules:
Implementation notes:
Reuse existing code:

### Acceptance Criteria
- [ ] <criterion>
- [ ] <criterion>
- [ ] <criterion>

### Validation
Automated:
- <command or check>
Manual:
- <manual check>

### Risks And Dependencies
- <risk or dependency>

### Open Questions
- <question>

### GitHub Issue Body
Copy-pasteable issue text if the user wants an issue created.
```

## Quality Bar

- A ready spec names target behavior, affected surfaces, acceptance criteria, and validation.
- A ready spec is smaller than a product brief and more precise than a task title.
- If the implementation would require product judgment during coding, the spec is not ready.
- If a duplicate exists, do not produce a second live issue; recommend updating or closing the existing one.
