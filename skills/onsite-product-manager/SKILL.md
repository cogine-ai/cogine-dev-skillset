---
name: onsite-product-manager
description: Turn full customer-meeting text, operator emphasis, and customer context into an onsite product opportunity document with 3-10 evidence-backed product propositions, core demo moments, validation questions, and downstream Build Cards; after demos, update the same document with customer evidence. Use only when explicitly invoked for this onsite product workflow, not for transcript summarization, PRDs, visual design, project routing, or implementation.
---

# Onsite Product Manager

Version 0.0.1 is an internal alpha.

Use this skill as the product-management layer between a live customer conversation and code-prototype
development. The code prototype is an experiment instrument; it is not the method for deciding what
product is worth showing. Work in the operator's language; default to Chinese.

## Core Rule

Produce one **Onsite Product Opportunity And Prototype Validation Document** before any prototype
work. Convert the evidence into a portfolio of 3-10 materially different product propositions. Give
each proposition one observable core demo moment, one key validation question, and one independent
Build Card.

Do not create a project, select a Project Template, research visual references, choose a technical
stack, write implementation specs, or build a prototype. Stop at the product document.

## Operating Modes

- **Pre-demo planning:** the default. Produce the context freeze, product portfolio, validation plan,
  and Build Cards, then stop before development.
- **Post-demo learning:** use only when the operator supplies the original product document and the
  fullest available demonstration conversation or notes. Append customer evidence, update each
  proposition verdict, and recommend the next product experiment or commercial action. Do not
  regenerate the original context freeze or resume development.

## Inputs And Authority

Read [references/input-contract.md](references/input-contract.md) before processing meeting material.

The minimum input for a `READY` pre-demo document is:

1. the full meeting text through the context-freeze point;
2. the onsite operator's short description of what matters most; and
3. the accumulated customer context, or an explicit statement that no prior context exists.

Use supplied artifacts, team capability boundaries, available prototype time, and desired prototype
count when they are available. Notes or a summary may support a provisional `NOT READY` document but
cannot pass the evidence gate. Missing context is an `Unknown`, not permission to invent a fact. Ask
only for a missing input that would change the product portfolio materially; do not ask the operator
to rewrite the conversation as requirements, features, or product forms.

Freeze the evidence used for the document. Preserve later conversation as a dated addendum rather
than silently rewriting the original interpretation.

## Workflow

### 1. Build The Context Snapshot

Extract only the evidence that changes product judgment:

- the customer, decision-maker, user, and buyer when known;
- the current workflow and costly, slow, risky, or confusing business moments;
- the business result the boss appears to care about;
- existing systems, data, habits, constraints, and previous attempts;
- explicit customer ideas and objections;
- the operator's emphasis;
- contradictions and unknowns.

Keep `Fact`, `Operator interpretation`, `Product hypothesis`, and `Unknown` distinct. Do not turn a
third-party summary into a transcript or a plausible inference into customer intent.

### 2. State The Product Opportunity

Answer this question before listing directions:

> Which different product mechanisms are worth testing because they could change a business result
> this customer recognizes?

Do not answer with a feature inventory, screen list, architecture, or generic claim such as "use AI
to improve efficiency."

### 3. Generate A Product Portfolio

Generate 3-10 product propositions supported by the evidence. Use these portfolio roles as reasoning
lenses, not as quotas:

- **Anchor:** closest to an explicit customer pain and easiest for the boss to recognize.
- **Contrast:** changes the mechanism, decision ownership, or workflow rather than reskinning the
  Anchor.
- **Stretch:** uses the customer context to reveal a credible opportunity beyond the stated request.

Prefer honest diversity over volume. If the evidence cannot support three propositions, show the
supported propositions, mark the portfolio `NOT READY`, and name the missing evidence instead of
inventing a surprise direction.

A proposition must identify the actor, business moment, present state, distinct product mechanism,
product form and usage surface, observable result, and business value. Use this sentence as a check:

> When **actor** reaches **business moment**, the product uses **distinct mechanism** to change
> **present state** into **observable result**, producing **business value**.

Apply the distinctness and portfolio tests in
[references/product-opportunity-document.md](references/product-opportunity-document.md). A chat,
dashboard, agent, workflow, canvas, report, or browser extension is only a delivery form; a different
shell alone is not a different product proposition.

### 4. Define The Core Demo Moment

Give each proposition one two-minute-or-shorter causal demonstration:

```text
business input
-> one meaningful user action
-> the product's distinct mechanism
-> visible state change
-> a business result the boss can recognize
```

The demonstration must test the proposition, not merely display a page. Infrastructure, integrations,
model output, and data may be simulated when disclosed. The causal behavior being validated must be
real in the clickable prototype. For example, if the proposition says one correction changes how a
similar case is handled, the later state must actually change during the interaction.

### 5. Define The Validation Experiment

Each proposition gets one consequential unknown and one question that could change the decision.
Avoid approval prompts such as "Do you like it?" Define observable positive and negative signals,
including whether the boss offers real data, changes the workflow framing, asks about a pilot or
commercial next step, rejects the role, or says the result has no value.

### 6. Write The Product Document And Build Cards

Use the exact document contract in
[references/product-opportunity-document.md](references/product-opportunity-document.md). Then create
one Build Card per portfolio proposition using
[references/prototype-handoff.md](references/prototype-handoff.md).

Rank the portfolio for internal prototype sequencing using evidence strength, customer-visible value,
learning value, demonstrability, and complementarity. Mark all 3-10 portfolio propositions as one
comparison batch for downstream execution; do not force one winner before the customer has seen the
prototypes. Reducing the batch below three requires an explicit operator waiver and must be reported
as `READY WITH RISKS`, never `READY`.

Return the full document in the response. If the operator provides a dedicated output directory,
also write `onsite-product-opportunity.md` there. Never infer a customer product repository as the
document target.

Keep it usable during a live meeting. Use a compact portfolio overview plus Build Cards as the
canonical detail; do not repeat the same proposition fields in both places. For a five-proposition
portfolio, target roughly 150 lines or fewer and keep each Build Card to 15 lines or fewer. Add
length only when material evidence or risk would otherwise be lost.

### 7. Stop At Product Handoff

End with the readiness verdict and the Build Cards. Do not invoke normal engineering workflow or
continue into prototype development unless a separate instruction explicitly starts the downstream
phase. The downstream prototype skill owns visual research, Project Template routing, implementation,
browser proof, and publishing.

## Post-Demo Learning Mode

When explicitly re-invoked after the prototypes are shown, read the original product document and
the fullest available demonstration transcript or operator notes. Use the feedback contract in
[references/prototype-handoff.md](references/prototype-handoff.md) to append evidence for every shown
prototype. Preserve the boss's exact meaning, distinguish words from observable actions, and set each
proposition to `Validated`, `Reframed`, `Rejected`, or `Unresolved`.

Update the overall portfolio judgment and recommend the next product experiment or commercial action.
Do not overwrite the context freeze, disguise unshown prototypes as rejected, change the historical
Build Cards, create a new product direction without labeling it as a post-demo hypothesis, or start
another development cycle.

## Readiness Gates

Report each gate separately:

- **Evidence:** every proposition traces to at least one meeting `Fact`; operator interpretations,
  product hypotheses, and unknowns remain explicitly labeled.
- **Product distinctness:** propositions differ in product mechanism and observable outcome, not only
  features, layout, visual style, or UI shell.
- **Validation:** every proposition names one risky assumption, one decision-changing question, and
  positive and negative signals.
- **Demonstrability:** every proposition has a clickable core moment with meaningful state change and
  a customer-visible business result.
- **Portfolio execution:** 3-10 materially different Build Cards are assigned to the same customer
  comparison batch; a smaller operator-waived batch is explicit and cannot receive `READY`.
- **Mock honesty:** `Real interaction`, `Synthetic data`, `Simulated intelligence`, and `Not claimed`
  are explicit.
- **Handoff:** every portfolio proposition has an independent Build Card that requires no technical
  invention to understand the intended product experience.
- **Stop boundary:** no project, Project Template, visual route, architecture, or implementation was
  created by this skill.

Use one overall verdict:

- `READY`: 3-10 propositions are assigned to the prototype batch and all required gates pass.
- `READY WITH RISKS`: the portfolio is actionable, but named assumptions or evidence gaps may change
  individual propositions.
- `NOT READY`: the evidence cannot support a truthful prototype portfolio or a core product decision
  remains unresolved.

Do not upgrade a failed gate because the prose sounds polished.

## Non-Goals

This skill does not:

- summarize a meeting for general reading;
- produce a complete PRD, roadmap, backlog, or system design;
- decide the component library, UI style, database, backend, model, or integration architecture;
- turn every discussed feature into a separate prototype;
- ask the customer to choose from text descriptions before seeing the prototypes;
- claim that visual preference proves product value;
- include private meeting transcripts, customer assets, or generated prototypes in the skill package.

## Quality Bar

A strong result makes the product logic more specific than the customer's initial wording while
remaining traceable to evidence. It offers multiple credible product mechanisms, gives each prototype
one job, and tells the downstream builder exactly what business change must become visible without
telling the builder how to engineer or style it.

A weak result is a transcript summary, a list of ten features, several UI shells around the same
workflow, a technology plan, or a polished document with no falsifiable product hypothesis.
