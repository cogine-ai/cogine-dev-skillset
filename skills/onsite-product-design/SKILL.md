---
name: onsite-product-design
description: Turn one complete onsite product portfolio into a concise, visibly differentiated design portfolio plus one confirmed Design Card per Build Card. Use after onsite-product-manager and before onsite-prototype-development when 3-10 sales prototypes need deliberate visual and interaction directions. Use only when explicitly invoked; do not use for product ideation, Project Template routing, implementation, or general design audits.
---

# Onsite Product Design

Version 0.0.1 is an internal alpha.

Use this skill as the design layer between product judgment and code-prototype development. It sees
the entire comparison batch so that 3-10 parallel prototypes do not independently collapse into the
same safe SaaS shell. Work in the operator's language; default to Chinese.

The goal is not a long design document. The goal is a small visible design portfolio that lets the
onsite team recognize each proposed experience before separate development tasks implement it.

This is a short coordination pass inside the same onsite delivery window, not a separate design
project. When the runtime supports parallel workers, parallelize card-level research and preview
drafting, then bring every result back to one portfolio coordinator for the final overlap check.
Stop when every card has one visible, actionable route; do not spend prototype time on pixel-perfect
design artifacts.

## Core Rule

Keep the upstream product propositions fixed. Explore broadly inside the design stage, then lock one
deliberate visual and interaction route for every Build Card.

Produce four artifacts:

1. `onsite-design-board.md`: a concise design portfolio for the operator;
2. `design-context.md`: internal research, alternatives, decisions, gates, and risks;
3. `design-cards/Pxx.md`: one complete development handoff matching every Build Card;
4. `previews/Pxx.*`: at least one visible target composition per Design Card.

The distinction must survive removal of color, font, radius, border, and shadow choices. Different
palettes on the same dashboard composition are not different design directions.

Do not create a product project, select a Project Template, install a UI library, write business
code, or run the final prototype. Stop at the confirmed design bundle.

## Operating Modes

- **Pre-development design:** the default workflow below. Turn one full product batch into visible
  previews and Design Cards, then stop before implementation.
- **Post-build portfolio QA:** use only when the operator supplies the original design bundle and the
  actual running input/result states for every completed prototype in the batch. Compare the built
  portfolio side by side and report drift; do not create a new route or modify code.

## Inputs And Authority

Read [references/input-contract.md](references/input-contract.md) before working. Require the whole
upstream product bundle, not a single isolated card, so portfolio-level design overlap can be seen.

The Build Cards are authoritative for what each product does. The latest explicit operator
correction is authoritative over design inference. Existing approved brand rules, screenshots,
Figma frames, or a product design system are authoritative visual constraints when supplied.

An upstream `READY` bundle may proceed normally. `READY WITH RISKS` requires the named risks to be
acknowledged. A `NOT READY` bundle may receive clearly labeled provisional design exploration so the
team can see possibilities, but it can never produce development-ready Design Cards.

## Workflow

### 1. Validate The Product Portfolio

- Read `onsite-product-board.md`, `context-freeze.md`, and every Build Card in the comparison batch.
- Verify freeze ID, batch ID, card IDs, verdict, gates, and card count agree.
- Freeze each card's actor, business moment, product mechanism, product form, core demo loop, visible
  result, validation question, mock boundary, and non-goals.
- Do not merge cards, rank a new winner, invent a new proposition, or rewrite the product mechanism.

If product evidence is contradictory, record the gap. Return the affected card to the product layer
instead of solving the contradiction through visual design.

### 2. Research The Design Space

Read [references/visual-research.md](references/visual-research.md). For this sales-critical new
surface, visual research is material by default.

Use this source order:

1. operator-provided brand, screen, Figma, or approved design-system evidence;
2. the `refero-design` skill when it is actually available;
3. Refero MCP capabilities when they are actually available;
4. other authorized visible references;
5. clearly labeled Agent-derived visible compositions when no external reference is available.

Do not wait for the operator to name Refero. When Refero is available, actively use Styles for the
visual language, Screens for concrete hierarchy and states, and Flows when journey choreography is
material. Send only generalized public concepts; never send customer identity, raw transcript text,
private assets, or proprietary terminology.

Explore more than one credible route internally for each card, but do not multiply the final
portfolio into `3-10 x alternatives`. Recommend and lock one route per card. Preserve rejected routes
briefly in `design-context.md` so the choice is auditable.

### 3. Design The Portfolio, Not Isolated Screens

For every card define:

- the intended first impression and product-specific design thesis;
- entry, processing or decision, result, and reset states;
- first-screen attention order and target composition;
- the core interaction and visible state choreography;
- information hierarchy, media role, density, component character, and semantic color roles;
- one observable non-token design consequence tied to the business moment;
- a primary reference lock and any narrowly scoped secondary reference;
- explicit rejects and the reskin counterfactual;
- what development must preserve and how the rendered result will be accepted.

Then compare the whole batch. Prevent accidental repetition of the same shell, navigation model,
card grid, hero composition, state expression, or decorative AI styling. Shared customer branding may
remain consistent, but each product mechanism must receive a recognizably appropriate experience
topology. Do not force novelty that makes the product harder to understand.

### 4. Make Every Direction Visible

For each card create at least one visible preview of the core state and reference it from the design
board and Design Card. A preview may be an authorized reference-backed screen map, annotated
wireframe, SVG, image, or lightweight HTML composition. It is design evidence, not the final
prototype and need not implement business logic.

When the current client can render local media or open a browser preview, actually show each preview
to the operator. Do not report only that a preview file exists. Use a clickable exact path when the
format cannot be embedded directly.

Named brands, mood words, color codes, component lists, or a record that Refero was called are not a
preview. The artifact must make attention order, composition, primary action, and result state
visible.

### 5. Present One Design Decision

Use the exact short board in [references/output-bundle.md](references/output-bundle.md). Show the
recommended route for each product, its visible preview, the material differences across the batch,
and the fixed mock boundary.

Ask once for confirmation of the design portfolio. If the operator explicitly delegates the design
choice, the Agent may select and freeze the routes after the evidence exists. Delegation does not
waive evidence. An evidence waiver must remain `waived` and cannot become a pass.

Do not ask the operator to choose product directions again, approve implementation details, name a
component library, or specify a design tool.

### 6. Write The Design Bundle

Use [references/output-bundle.md](references/output-bundle.md) exactly. Keep the human board short;
put alternatives, mappings, gate evidence, and implementation constraints in the internal artifacts.

Use one of these overall states:

- `DESIGN READY`: the upstream product bundle is eligible, all required design gates pass, and the
  operator has confirmed the portfolio or explicitly delegated the design decision;
- `AWAITING DESIGN DECISION`: the evidence and recommended routes are complete but the operator has
  not confirmed or delegated the portfolio;
- `PROVISIONAL - PRODUCT BLOCKED`: visible routes exist, but the upstream product bundle is
  `NOT READY` or unacknowledged `READY WITH RISKS`;
- `DESIGN NOT READY`: a truthful, visible, sufficiently distinct design portfolio cannot yet be
  formed.

Only `DESIGN READY` Design Cards may enter prototype development.

### 7. Stop At Design Handoff

Return the complete `onsite-design-board.md`, actually show or link every visible preview, and then
give only the paths to `design-context.md`, `design-cards/`, and `previews/`. Do not continue into
Project Template selection or implementation unless a separate instruction explicitly starts
`onsite-prototype-development`.

## Readiness Gates

Record these separately in `design-context.md` and copy the required states to every Design Card:

- **Upstream product:** product verdict and required gates are eligible for design handoff.
- **Visible evidence:** every selected route has a visible preview and exact source or fallback label.
- **Product-design fit:** composition and interaction express the fixed product mechanism and result.
- **Portfolio design distinctness:** the batch differs beyond tokens or superficial layout changes.
- **State completeness:** entry, processing or decision, result, and reset are designed.
- **Reference lock:** one dominant basis and bounded secondary roles are explicit.
- **Mock honesty:** design does not imply production integrations or intelligence that are mocked.
- **Decision:** operator confirmation or explicit delegation is recorded.
- **Handoff:** every Build Card has one matching, scope-complete Design Card.
- **Stop boundary:** no project routing, template mutation, business code, or final prototype was made.

Do not upgrade failed gates because the board looks polished.

## Post-Build Portfolio QA

The individual development tasks prove their own loops and fidelity. They cannot prove that the
running batch still looks and behaves materially different after every task has used the same PT.

When explicitly re-invoked after the batch is built:

1. read the original `design-context.md`, every Design Card, and every preview;
2. inspect the actual running input and result states for every completed Pxx, using screenshots and
   real browser paths when available;
3. compare each result with its own non-token consequence and with the nearest route named in the
   portfolio matrix;
4. check for convergence in shell, navigation, attention order, core interaction, state expression,
   media role, and customer-visible result;
5. write `portfolio-runtime-review.md` beside the original design bundle.

Use `PORTFOLIO READY`, `PORTFOLIO DRIFT`, or `PORTFOLIO NOT PROVEN`. A missing or unbuilt card is
`not proven`, not silently omitted. When drift exists, identify the smallest Design Card acceptance
check that the affected development task failed and return that card for a bounded correction. A new
design route requires a new operator decision.

This mode owns only batch comparison. It does not replace each development task's browser proof or
operator acceptance and does not modify a project.

## Non-Goals

This skill does not:

- summarize the meeting or generate product propositions;
- change the upstream product portfolio;
- create several coded variants of one proposition;
- select Project Templates, frameworks, libraries, databases, models, or deployment targets;
- copy another product wholesale or reuse third-party assets without authorization;
- treat color variation, visual taste, or customer praise as product validation;
- claim that a design preview is a working prototype.
