---
name: plan-devex-review
description: Use when reviewing a plan or spec for developer-facing API, CLI, SDK, MCP, plugin, integration guide, getting-started documentation, or developer onboarding design before implementation.
---

# Plan DevEx Review

Use this skill to review the planned developer experience before implementation. It applies only to developer-facing surfaces such as APIs, CLIs, SDKs, MCP servers, plugins, integration docs, and getting-started flows.

## Do Not Use

Do not use this for:

- Consumer web UX, landing-page design, or general product copy.
- Backend architecture with no developer-facing surface.
- Live onboarding tests after implementation; use `devex-review` for that.
- General engineering plan review; use `planmode-engineer`.

## Core Rule

A developer-facing plan is not ready unless a new developer can understand the promise, reach a first useful result, recover from common errors, and know what to do next.

## Target Gate

Before reviewing, identify the target:

- API plan or OpenAPI/schema change.
- CLI command, flag, config, or install plan.
- SDK package, import path, or example plan.
- MCP server, plugin, skill, or integration surface.
- Developer documentation or getting-started guide.

If the target is not developer-facing, say this skill does not apply and recommend the appropriate review skill.

## Workflow

1. Define the developer persona.
   - First-time evaluator, integrating engineer, internal maintainer, partner developer, plugin author, or open-source contributor.

2. Map the planned journey.
   - Discover.
   - Install or authenticate.
   - Configure.
   - Run the first example.
   - Get the first useful result.
   - Debug the first failure.
   - Move to the second task.

3. Estimate TTHW.
   - Count commands, files, accounts, tokens, approvals, docs pages, and decisions.
   - Identify the first magical moment.
   - State the target TTHW and why it is realistic.

4. Review the interface contract.
   - Naming, command shape, endpoint shape, arguments, defaults, examples, errors, versioning, compatibility, and migration path.
   - Prefer explicit defaults and reversible setup.

5. Review failure design.
   - Missing credential.
   - Invalid config.
   - Permission denied.
   - Network/provider failure.
   - Version mismatch.
   - Rate limit or quota.
   - Example drift.

6. Produce a readiness verdict.
   - `READY`: the plan can proceed without DX decisions during implementation.
   - `READY WITH RISKS`: implementable, but friction or assumptions must be tracked.
   - `NOT READY`: developer-facing decisions are missing.

## Review Dimensions

| Dimension | Question |
|---|---|
| Persona clarity | Is the first developer type explicit? |
| Promise clarity | Is the value clear before setup begins? |
| TTHW | Can the first useful result happen quickly enough? |
| Setup path | Are install, auth, config, and prerequisites explicit? |
| Interface design | Are API/CLI/SDK names, defaults, and examples coherent? |
| Error quality | Will failures tell developers what to do next? |
| Docs structure | Is there one obvious path from start to success? |
| Production trust | Are versioning, limits, security, and support boundaries visible? |

## Output Contract

```markdown
## Plan DevEx Review

### Target
Surface: API / CLI / SDK / MCP / plugin / docs / onboarding
Persona:

### Verdict
READY / READY WITH RISKS / NOT READY

### Journey Map
Discover -> Setup -> First Example -> First Useful Result -> First Failure -> Second Task

### TTHW Assessment
Current estimate:
Target:
Step count:
Main friction:

### Findings

#### PDX-001: <title>
Severity:
Evidence from plan:
Developer impact:
Recommendation:

### Required Plan Changes
- <required change>

### Deferred DX Improvements
- <deferred improvement>

### Implementation Checklist
- [ ] <implementation step>
- [ ] <implementation step>
- [ ] <implementation step>

### Handoff To Implementation
Files/docs likely affected:
Validation after implementation:
```

## Quality Bar

- Keep the review scoped to developer experience, not general architecture.
- Mark missing examples, vague errors, and unclear setup as plan blockers when they affect first success.
- Do not accept "we will document later" for developer-facing changes that require docs to be usable.
- Prefer measurable outcomes: TTHW, steps, commands, pages, error recovery.
