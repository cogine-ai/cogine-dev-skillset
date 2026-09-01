# Onsite Product Opportunity And Prototype Validation Document

Create one document per meeting context freeze. This is a product-hypothesis portfolio and prototype
experiment plan, not a complete PRD.

## Document Structure

```markdown
# Onsite Product Opportunity And Prototype Validation

## Document Status
Verdict: READY / READY WITH RISKS / NOT READY
Context freeze:
Target prototype count:
Prototype comparison batch:
Preparation and demonstration time:

## 1. Context Snapshot
Evidence index: 8-15 material facts, interpretations, hypotheses, or unknowns.
Customer and decision context:
Current workflow and business tensions:
Desired business results:
Existing systems, constraints, ideas, and objections:
Operator focus:
Contradictions and unknowns:

## 2. Product Opportunity Judgment
One paragraph about which product mechanisms are worth validating and why.

## 3. Prototype Portfolio
Portfolio rationale:
Recommended internal sequence:
Coverage: Anchor / Contrast / Stretch

| ID | Role | Product proposition | Distinct mechanism | Form and usage surface | Visible business result | Key unknown |
|---|---|---|---|---|---|---|
| P01 | Anchor | ... | ... | ... | ... | ... |
<Repeat one row per proposition>

## 4. Build Cards
One compact, independent Build Card per portfolio proposition. This is the canonical proposition
detail; do not repeat a second long proposition section.

## 5. Demonstration Feedback Capture
The evidence to record after each prototype is shown.

## 6. Gate Summary
Evidence:
Product distinctness:
Validation:
Demonstrability:
Portfolio execution:
Mock honesty:
Handoff:
Stop boundary:
Overall verdict:

## 7. Risks And Open Questions
Only uncertainties that can change a product or commercial decision.
```

Every material context statement and Build Card must carry or link to an evidence label from the
input contract. Keep the document compact enough to scan onsite. Limit the context snapshot to facts
that change the portfolio, use one row per proposition in the overview, keep each Build Card to 15
lines or fewer, and cap decision-changing risks at five. Do not repeat prose across sections.

## Product Proposition Test

A proposition is not a feature. It names a product mechanism that changes a business state for a
specific actor at a specific moment.

Name the product form and where the user encounters it because those choices affect adoption and the
prototype experience. Treat them as product hypotheses, not proof of distinctness and not technical
architecture.

Use this check:

> When **actor** reaches **business moment**, the product uses **distinct mechanism** to change
> **present state** into **observable result**, producing **business value**.

Reject a candidate when it is only:

- a feature extracted from the conversation;
- a generic AI capability with no business mechanism;
- a page, dashboard, chat, agent, canvas, report, plugin, or workflow shell;
- the same loop with a different layout, visual theme, role label, or amount of detail;
- an idea whose value requires an unproven production integration to be visible;
- an impressive animation that does not test a consequential assumption.

## Distinctness Test

Two propositions are materially distinct only when the product mechanism differs and the resulting
business state or customer-visible result also differs. In addition, at least two of these should
differ:

- primary actor;
- entry trigger or business moment;
- decision ownership;
- product mechanism;
- resulting artifact or next action;
- business result.

Changing only the actor or entry trigger is insufficient. Product form may support a distinction but
does not establish one by itself.

## Portfolio Test

The portfolio should collectively provide:

- an `Anchor` grounded in an explicit customer pain;
- a `Contrast` that tests a different mechanism or decision model;
- a `Stretch` when the context supports a credible opportunity beyond the stated request.

Rank the propositions for internal prototype sequencing using:

- evidence strength;
- immediacy of the customer-visible result;
- value of the learning if the hypothesis is accepted or rejected;
- ability to demonstrate the causal mechanism honestly in the available time;
- complementarity with the other prototypes.

Do not use a numeric score to manufacture precision. Do not force ten weak ideas or ask the customer
to select a text description before the portfolio is prototyped.

Assign every portfolio proposition to the same downstream comparison batch by default. A normal
`READY` document therefore hands off 3-10 Build Cards for prototyping. If the operator explicitly
reduces the batch below three, record the reason and waiver; the overall verdict is at most
`READY WITH RISKS`.

## Core Demo Moment Test

Each proposition gets exactly one primary demo moment:

```text
business input
-> one meaningful user action
-> distinct product mechanism
-> visible state change
-> recognizable business result
```

The moment should fit within two minutes of demonstration and be repeatable or resettable. A page
view, navigation tour, fake loading animation, static dashboard, or list of future capabilities does
not qualify.

## Validation Test

Name one largest unknown per proposition. Ask a question that could reveal why the product would or
would not fit the real workflow. Define signals before the prototype is shown:

- `Strong positive`: offers real data, asks about integration, pilot, price, timing, or names a real
  owner and next step.
- `Moderate positive`: selects the product logic and gives a concrete business reason.
- `Weak positive`: says it looks good or interesting without workflow commitment.
- `Negative`: rejects the problem, actor, mechanism, workflow change, or value of the result.

Visual preference is supporting feedback, not product validation.

## Mock Boundary Test

Infrastructure may be mocked; the causal relationship under validation may not be mocked.

Record four boundaries for every proposition:

- `Real interaction`: clickable behavior, computation, state transition, and feedback that truly run
  in the prototype.
- `Synthetic data`: anonymized or invented customer, order, document, and metric data.
- `Simulated intelligence`: precomputed recognition, agent, retrieval, or model outputs.
- `Not claimed`: authentication, persistence, external integration, accuracy, performance, security,
  compliance, or production readiness not proven by the prototype.

If the product proposition promises that a correction changes a later decision, the correction and
later changed result must really happen in prototype state. A static success screen is insufficient.
