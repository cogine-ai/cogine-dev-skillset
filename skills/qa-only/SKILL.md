---
name: qa-only
description: Use when the user asks for a report-only browser QA pass on a web application, live site, preview URL, authenticated app flow, or release candidate without making code changes.
---

# QA Only

Use this skill to test a web application like a user and produce an evidence-based QA report. Do not edit code, commit changes, or apply fixes.

## Core Rule

Report only. If you find a bug, document the evidence, reproduction path, severity, and suggested fix. Do not fix it unless the user explicitly switches to an implementation task.

## Scope

Use this for:

- Web apps, dashboards, SaaS tools, AI application frontends, and preview deployments.
- Authenticated flows when cookies or a real browser session are available.
- Release-candidate checks before shipping.
- "Find bugs", "test the site", "QA this", or "report-only QA" requests.

Do not use this for unit-test-only debugging, backend-only compiler failures, or design critique without functional browser testing.

## Workflow

1. Establish target and mode.
   - Target URL or local app URL.
   - Auth state: public, login required, cookie import needed, or real-browser session.
   - Mode: Quick, Standard, or Focused.
   - Scope exclusions named by the user.

2. Prepare the browser path.
   - If the site needs auth, use `get-cookies` or an existing real browser session.
   - If no browser automation helper exists, use the available local browser tooling and state the limitation.
   - Capture screenshots for every reported issue when tooling allows it.

3. Orient before testing.
   - Identify primary user journeys, navigation, forms, stateful actions, AI interactions, and payments or account settings if present.
   - For AI apps, include empty input, long input, model failure, slow response, retry, cancellation, and malformed output paths when relevant.

4. Execute the QA pass.
   - Quick: homepage plus top 5 user paths; console/network errors; major broken states.
   - Standard: primary journeys, key forms, mobile/desktop layout, auth/session behavior, loading/error/empty states.
   - Focused: user-specified page, flow, or feature with deeper edge cases.

5. Score and report.
   - Use a 0-100 health score.
   - Separate blockers from polish.
   - Include reproduction steps precise enough for another agent to verify.

## Severity Guide

| Severity | Meaning |
|---|---|
| Blocker | Core flow cannot complete, data loss, auth break, payment break, or severe AI failure. |
| High | Important user path broken or misleading. |
| Medium | Functional issue with workaround or limited reach. |
| Low | Minor visual, copy, or interaction defect. |

## Report Contract

```markdown
## QA Report

### Target
URL:
Mode:
Auth:
Date:

### Summary
Health score: __/100
Overall status: Ship / Ship with known issues / Do not ship

### Paths Tested
- <path>

### Findings

#### QA-001: <title>
Severity:
Path:
Evidence:
Reproduction steps:
Expected:
Actual:
Suggested fix:

### Screenshots / Artifacts
- <artifact>

### Not Tested
- <area>

### Recommended Next Step
- <next step>
```

## Quality Bar

- Do not report an issue without a reproduction path.
- Do not hide limitations; list what was not tested.
- Prefer concrete evidence over broad impressions.
- Do not call a site ready if critical paths were not tested.
