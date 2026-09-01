---
name: onsite-product-manager
description: Turn full customer-meeting text, operator emphasis, and customer context into a concise onsite product-direction board plus an internal context freeze and 3-10 independent Build Cards for the downstream design portfolio; after demos, capture customer evidence against those product bets. Use only when explicitly invoked for this onsite product workflow, not for transcript summarization, PRDs, visual design, project routing, or implementation.
---

# Onsite Product Manager

Version 0.0.3 is an internal alpha.

Use this skill as the product-management layer between a live customer conversation and product
design. The eventual code prototype is an experiment instrument; it is not the method for deciding
what product is worth showing. Work in the operator's language; default to Chinese.

## Core Rule

Think broadly, then write briefly. Before any prototype work, convert the evidence into 3-10
materially different product propositions and produce three separate artifacts for three audiences:

1. `onsite-product-board.md`: a short decision board for the onsite team and customer boss;
2. `context-freeze.md`: internal evidence, reasoning, gates, risks, and unknowns;
3. `build-cards/Pxx.md`: one complete product-to-design handoff per proposition.

The human-facing board is not a shortened PRD and must not expose the internal reasoning report.
Each proposition still gets one observable core demo moment, one key validation question, and one
independent Build Card.

Do not create a project, select a Project Template, research visual references, choose a technical
stack, write implementation specs, or build a prototype. Stop at the product handoff bundle.

## Operating Modes

- **Pre-demo planning:** the default. Produce the product-direction board, context freeze, and Build
  Cards, then stop before design.
- **Post-demo learning:** use only when the operator supplies the original output bundle and the
  fullest available demonstration conversation or notes. Append customer evidence, update each
  proposition verdict, and recommend the next product experiment or commercial action. Do not
  regenerate the original context freeze or resume development.

## Inputs And Authority

Read [references/input-contract.md](references/input-contract.md) before processing meeting material.

The minimum input for a `READY` pre-demo bundle is:

1. the full meeting text through the context-freeze point;
2. the onsite operator's short description of what matters most; and
3. the accumulated customer context, or an explicit statement that no prior context exists.

Use supplied artifacts, team capability boundaries, available prototype time, and desired prototype
count when they are available. Notes or a summary may support a provisional `NOT READY` bundle but
cannot pass the evidence gate. Missing context is an `Unknown`, not permission to invent a fact. Ask
only for a missing input that would change the product portfolio materially; do not ask the operator
to rewrite the conversation as requirements, features, or product forms.

Freeze the evidence used for the bundle. Preserve later conversation as a dated addendum rather
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
[references/output-bundle.md](references/output-bundle.md). A chat,
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

### 6. Write The Output Bundle

Use the exact three-artifact contract in
[references/output-bundle.md](references/output-bundle.md). Create one Build Card per portfolio
proposition using
[references/prototype-handoff.md](references/prototype-handoff.md).

Rank the portfolio for internal prototype sequencing using evidence strength, customer-visible value,
learning value, demonstrability, and complementarity. Mark all 3-10 portfolio propositions as one
comparison batch for downstream design and prototype execution; do not force one winner before the
customer has seen the prototypes. Reducing the batch below three requires an explicit operator
waiver and must be reported internally as `READY WITH RISKS`, never `READY`.

Use a dedicated task-output directory supplied by the operator or environment. Never infer a
customer product repository as the output target. If no writable task-output route exists, return
the product board inline, say that the internal handoff has not been persisted, and ask only for an
output directory before claiming the bundle is complete.

Return the complete `onsite-product-board.md` content in the response, followed only by the paths to
`context-freeze.md` and `build-cards/`. Do not dump the internal evidence, gate analysis, or Build
Cards into the human-facing response unless the operator explicitly asks for them. Keep the board to
the exact short template; move every necessary detail to the appropriate internal artifact.

### 7. Stop At Product Handoff

End with the concise board and artifact paths. Do not invoke design or normal engineering workflow
unless a separate instruction explicitly starts the downstream phase. `onsite-product-design` owns
the portfolio's visible design directions and Design Cards. `onsite-prototype-development` later owns
Project Template routing, implementation, browser proof, and publishing boundaries.

## Post-Demo Learning Mode

When explicitly re-invoked after the prototypes are shown, read the original output bundle and
the fullest available demonstration transcript or operator notes. Use the feedback contract in
[references/prototype-handoff.md](references/prototype-handoff.md) to append evidence for every shown
prototype. Preserve the boss's exact meaning, distinguish words from observable actions, and set each
proposition to `Validated`, `Reframed`, `Rejected`, or `Unresolved`.

Append a dated feedback section to `context-freeze.md`, update the internal portfolio judgment, and
use the exact Post-Demo Response Contract in
[references/output-bundle.md](references/output-bundle.md). Do not overwrite the original freeze, disguise unshown
prototypes as rejected, change the historical Build Cards, create a new product direction without
labeling it as a post-demo hypothesis, or start another development cycle.

## Readiness Gates

Record each gate separately in `context-freeze.md` and copy the required states into every Build
Card. Do not expose gate jargon on `onsite-product-board.md`:

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
- **Handoff:** every portfolio proposition has an independent Build Card that requires no new product
  invention to understand what must be designed and validated.
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
one job, lets a boss understand the portfolio in two minutes, and gives the downstream designer
enough product detail without forcing the human reader through that detail.

A weak result is a transcript summary, a long analysis shown to the boss, a list of ten features,
several UI shells around the same workflow, a technology plan, or polished prose with no falsifiable
product hypothesis.
