---
name: devex-review
description: Use when auditing a live or implemented developer experience for APIs, CLIs, SDKs, MCP servers, plugins, integration guides, getting-started docs, or developer onboarding flows.
---

# DevEx Review

Use this skill to test the implemented developer experience from the perspective of a new developer. This is a live audit, not a plan review.

## Core Rule

Measure actual friction. Prefer running the quickstart, CLI help, examples, API requests, docs navigation, and error paths over judging intent from prose.

## Scope

Use this for developer-facing products:

- API onboarding and reference docs.
- CLI install, help text, commands, flags, and errors.
- SDK install/import/example flows.
- MCP servers, plugins, agent skills, templates, or integration guides.
- "Try the onboarding", "test the DX", "measure time to hello world", or "audit developer docs" requests.

Do not use this for end-user web UX, landing-page copy alone, or implementation-plan review before anything exists. Use `plan-devex-review` for plan-stage API/CLI/docs design.

## Workflow

1. Define the developer persona.
   - First-time evaluator, integrating engineer, internal maintainer, API customer, plugin author, or open-source contributor.

2. Measure TTHW.
   - TTHW means time to a credible first successful result.
   - Count steps, commands, accounts, tokens, config files, and decision points.
   - Note where a real developer would abandon.

3. Test the core path.
   - Install or setup.
   - Authentication or configuration.
   - Minimal example.
   - First useful output.
   - Next likely task after success.

4. Test failure paths.
   - Missing credential.
   - Invalid input.
   - Network/provider failure.
   - Permission error.
   - Version mismatch.
   - Rate limit or quota issue if relevant.

5. Score the experience.
   - TTHW.
   - Setup clarity.
   - Error quality.
   - Example correctness.
   - API/CLI surface coherence.
   - Troubleshooting path.
   - Trust and production readiness.

## Scorecard

| Dimension | Score | Evidence |
|---|---:|---|
| Time to hello world | 0-10 | |
| Setup clarity | 0-10 | |
| Error quality | 0-10 | |
| Examples and docs | 0-10 | |
| API/CLI coherence | 0-10 | |
| Troubleshooting | 0-10 | |
| Production trust | 0-10 | |

## Report Contract

```markdown
## Developer Experience Review

### Target
Product:
Surface: API / CLI / SDK / docs / MCP / plugin / template
Persona:

### Summary
Overall score: __/10
TTHW measured:
Status: Ready / Usable with friction / Not ready

### Journey Tested
- <journey>

### Findings

#### DX-001: <title>
Severity:
Evidence:
Developer impact:
Recommended fix:

### Scorecard
<table>

### Not Tested
- <area>

### Recommended Next Step
- <next step>
```

## Quality Bar

- Distinguish tested behavior from inferred judgment.
- Include exact commands, URLs, docs pages, or error text when available.
- Do not optimize for aesthetic docs alone; measure whether a developer can succeed.
- Call out boomerang gaps: where the intended plan says "easy" but the actual path is longer or unclear.
