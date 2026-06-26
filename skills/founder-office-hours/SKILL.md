---
name: founder-office-hours
description: Use when evaluating early product ideas, founder decisions, AI application concepts, wedge markets, target users, product scope, or design handoff before writing specs or architecture.
---

# Founder Office Hours

Use this skill to interrogate a product idea before it becomes a spec, roadmap, or architecture plan. Work in Chinese by default unless the user asks otherwise.

## Core Rule

Do not start implementation. Do not write architecture first. Convert a vague or overconfident idea into a clear product decision, or state why the idea is not ready.

## When To Stop And Ask

Ask the user before writing the final handoff when any of these are unresolved:

- The target user is unclear.
- The user and buyer are different and the buyer is not named.
- The product form is still a guess: SaaS, agent, API, plugin, browser extension, mobile app, CLI, workflow, or service.
- The value depends on model capability, platform policy, distribution, or pricing that has not been verified.
- There are two or more plausible directions with materially different users or execution surfaces.

## Workflow

1. Restate the real observation.
   - Separate the observed change from the user's interpretation.
   - Name what the observation does not prove.

2. Split the layers.
   - Observation: what changed.
   - Judgment: what the user believes it means.
   - User: who has the pain and how often.
   - Buyer: who pays and what budget or ROI exists.
   - Product form: interface, packaging, deployment, and workflow location.
   - Execution surface: browser, repo, terminal, database, SaaS account, documents, chat, local machine, or cloud.
   - Business motion: distribution, pricing, support burden, and defensibility.

3. Pressure-test six founder questions.
   - Who is the first high-frequency user?
   - What painful workflow happens today without this product?
   - Why would this user switch now?
   - What is the smallest useful version that proves demand?
   - What existing surface already contains the user's state, permissions, context, and habit?
   - What breaks if model capability, platform rules, or distribution changes in 3-12 months?

4. Generate alternatives before recommending.
   - Mainstream route: closest to market inertia.
   - Reverse route: contradicts the obvious assumption.
   - Minimal route: proves the value with the fewest capabilities.
   - Future route: becomes stronger if AI capabilities improve.

5. Challenge the premise.
   - Identify the 2-3 riskiest assumptions.
   - Explain how each assumption can be falsified.
   - Call out what is likely overestimated and underestimated.

6. Produce a founder handoff.
   - Write the decision in a form that `backlog-ready-spec`, `planmode-ceo`, or `planmode-engineer` can consume.
   - If no direction is ready, output `VERDICT: NOT READY` and list the missing decisions.

## Founder Handoff Contract

Use this structure for the final artifact:

```markdown
## Founder Office Hours Handoff

### Verdict
READY / READY WITH RISKS / NOT READY

### Product Decision
One clear recommendation and why.

### Target User
First high-frequency user:
First paying user:
Future broader user:

### Problem And Current Workflow
What the user does today, where the pain occurs, and why current options are insufficient.

### Product Form
Recommended form:
Rejected forms:
Reasoning:

### Execution Surface
Where interaction happens:
Where execution happens:
Existing state/permissions/context to reuse:

### Alternatives Considered
- Mainstream:
- Reverse:
- Minimal:
- Future:

### Riskiest Assumptions
1.
2.
3.

### Minimum Validation Experiment
Target user:
Smallest useful product:
Behavior to observe:
Success signal:
Failure signal:
Next decision unlocked:

### Handoff To Planning
Recommended next skill: `backlog-ready-spec` / `planmode-ceo` / `planmode-engineer`
Open questions:
```

## Quality Bar

- Be explicit when the idea is not ready.
- Do not praise or dismiss the idea; evaluate the decision surface.
- Prefer a narrow, testable wedge over a platform-shaped first version.
- Separate interaction from execution for AI and agent products.
- Use current market or platform facts only when verified during the session.
