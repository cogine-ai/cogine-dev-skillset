---
name: onsite-prototype-development
description: Build one demo-ready interactive sales prototype from exactly one fixed Build Card and its matching DESIGN READY Design Card, using an existing project or compatible Project Template. Preserve the upstream product and design decisions, implement the smallest complete business loop, and prove it in a real browser. Use only when explicitly invoked for onsite sales prototyping, not for product ideation, design exploration, Project Template authoring, static mockups, or transcript summarization.
---

# Onsite Prototype Development

Version 0.0.5 is an internal alpha.

Use this skill as the implementation layer after product and design are complete. Build the smallest
working interaction that lets a customer act, observe processing or a decision, see meaningful state
change, and receive a business result. Mock external systems honestly, but make the demonstrated
causal loop real and repeatable.

One Build Card plus its matching Design Card maps to one clean development task. Run the comparison
batch as separate tasks so 3-10 prototypes can be built in parallel without mixing scope.

Every parallel task must own a unique target-project path, development-server port, and proof-output
directory. Never let two cards modify the same checkout, reuse another card's running service, or
write screenshots into one shared proof folder. When the operator authorizes a batch output root,
derive a stable child slug from the batch and card IDs; otherwise resolve only the missing destination.

## Fixed Upstream Decisions

The Build Card is authoritative for **what** to build and validate. The Design Card is authoritative
for **how** that product experience is composed, behaves visually, and communicates state.

Do not regenerate product alternatives, choose another proposition, search for visual routes, call
Refero, or silently redesign the selected route. If either card is missing or mismatched, return the
contract gap. Never fall back to the old combined discovery-and-design behavior.

Accurate completion is more important than perfect hardening. Accuracy means:

- the fixed product mechanism is present;
- the confirmed design thesis and non-token consequence are visible;
- the customer-facing loop works end to end and can reset;
- mock and production boundaries are truthful;
- the exact running path has sufficient browser and screenshot proof;
- implementation stops as soon as the sales demo is ready.

## Start Contract

Before creating or modifying target files:

1. Read [references/input-contract.md](references/input-contract.md) and validate exactly one matching
   Build Card and Design Card plus their linked product and design freezes.
2. Read [references/context-freeze.md](references/context-freeze.md) and draft the development brief
   outside the target repository.
3. Resolve an existing target project or a Project Template source, new-project destination, and
   project name. When the operator has not supplied a route, read
   [references/project-template-registry.md](references/project-template-registry.md) and select the
   narrowest compatible registered template. Never treat the open working directory as the target by
   accident.
4. Read the target or source template instructions, implementation, editable boundaries, and
   validation commands. Verify that the fixed product loop and Design Card are feasible in the
   remaining time.
5. Read [references/demo-done.md](references/demo-done.md) and establish the smallest proof path.
6. Present one compact pre-development check containing the fixed card IDs, core loop, selected
   design route and preview, mock/non-goal boundary, project route, and proof path. Ask only for a
   materially unresolved project route, authority to create or modify the target, or a contradiction
   that makes the upstream decisions infeasible.

An explicit instruction to develop the matching cards in a resolved target is the development
assignment; do not ask the operator to reconfirm the product or design. However, product and design
readiness cannot be waived implicitly. A `NOT READY` product freeze, provisional or unconfirmed
Design Card, missing visible design evidence, mismatched IDs, or failed required gate blocks target
modification.

Use these concise blockers:

- `PRODUCT REQUIRED`: no valid Build Card or product freeze;
- `DESIGN REQUIRED`: no matching Design Card or design freeze;
- `PRODUCT BLOCKED`: upstream product verdict or required gates do not permit development;
- `DESIGN BLOCKED`: Design Card is not `DESIGN READY` or its required evidence is incomplete;
- `PROJECT ROUTE REQUIRED`: product and design are ready but no authorized target route exists.

Do not solve a blocker by inventing missing upstream work inside this skill.

## Project Routing

Use the first matching rule:

1. If the operator identifies a target project, resolve its exact path and confirm that it exists and
   is accessible. Read its repository instructions before modification. If the path does not exist
   and the operator clearly intends a new project, treat it only as the proposed destination and use
   rules 2-3 for template selection.
2. If the operator identifies a Project Template, resolve its source and fixed revision, then use it
   when its verified contract supports the fixed cards. Do not replace it with a registry entry.
3. Otherwise, read [references/project-template-registry.md](references/project-template-registry.md)
   and automatically select the narrowest compatible registered template. Do not ask the operator to
   identify a template that the registry already resolves.
4. Resolve a new project name and destination independently from template selection. If no
   destination is authorized, ask only for the destination. Do not infer authorization from the
   current working directory.
5. If no registered template is compatible, request a compatible template or target project in the
   pre-development check. Do not create an arbitrary stack.

If a supplied path appears to be the template source itself, clarify whether the operator intends to
create a project from it or intentionally edit it. When using a Project Template, follow
[references/template-protocol.md](references/template-protocol.md). For a non-template project,
follow that repository's instructions.

## Development Mode

Follow `Research -> Plan -> Code`, proportionate to the onsite time box.

### Research

- Read the Build Card, Design Card, linked freezes, and visible preview. Do not require or copy the
  private transcript into this task.
- Read the design context's portfolio matrix only to preserve this card's named difference from its
  nearest route. Do not implement or redesign the other cards.
- Inspect the target project's source, dependencies, instructions, current UI foundations, and
  validation path before changing it.
- Map the fixed demo loop and selected design route to existing editable surfaces. Reuse the installed
  stack and components before adding dependencies.
- Report a material product contradiction to `onsite-product-manager` and a material design
  contradiction to `onsite-product-design`; do not repair either by improvising a new direction.

### Plan

- Define one smallest complete vertical slice. It may contain several tightly coupled functions only
  when all are necessary for the same causal loop.
- Express it as `input/action -> processing/decision -> state change -> business result -> reset`.
- Preserve the Design Card's first-screen attention order, state map, reference mappings, and named
  non-token consequence.
- Keep all other features and routes deferred. Do not scaffold the remaining 10 discussed functions.
- Use synthetic, customer-shaped data and identify every mocked external boundary.

### Code

- Instantiate or modify only the resolved target project. Never edit the Project Template source by
  accident.
- Replace starter examples directly and reuse the existing stack.
- Build real interactive state. Static screens, dead controls, navigation-only tours, fake success
  states, and page screenshots do not satisfy the loop.
- Implement the selected Design Card through editable application and theme surfaces. Do not modify
  protected template foundations or install another design system merely to force the route.
- A token-only reskin is not implementation of the Design Card. Preserve its composition,
  information hierarchy, interaction feedback, media role, or state choreography.
- Add focused behavior tests for non-trivial core-loop logic when a stable seam exists and the
  repository requires or the time box safely permits them.
- Run the fastest sufficient repository validation and exercise the exact visible path in a real
  browser.
- Compare running input and result states with the Design Card preview and references. Capture focused
  screenshots and record each promised non-token consequence as `visible`, `drifted`, or `not
  proven`.
- Verify the running URL, visible product identity, process, and proof directory belong to this exact
  batch/card pair; do not accept another parallel task's server as proof.
- Stop implementation when the core loop and required pre-acceptance proof are ready, then present
  the actual result for operator visual acceptance. Keep 0.0.5 Overall at `not pass` until that
  acceptance exists.

Proof must not expand the product architecture. If tooling cannot observe a non-blocking detail,
disclose the proof gap; do not add a backend, service, dependency, or new behavior solely for proof.

## Context And Safety

- Keep recordings, full transcripts, product and design freezes, customer-sensitive data,
  credentials, and secrets outside the target repository and public artifacts.
- Use synthetic data by default and label simulated intelligence, persistence, integrations, and
  production properties.
- Do not access customer, staging, production, paid, authenticated, or database resources without
  exact authorization for that resource and action.
- Do not publish automatically or convert the prototype into production code. Publishing and
  productionization are separate tasks.

## Handoff

Return the runnable location and access method, one concise demo path, operator talk track,
implemented and deferred scope, mock and assumption boundaries, the fixed product and design sources,
verification evidence, and separate core-loop, direction-divergence, and visual-design gate states.
Use [references/demo-done.md](references/demo-done.md) exactly.

An individual task cannot claim that the whole comparison batch remained visually distinct. Mark the
batch `not proven` until `onsite-product-design` performs its post-build portfolio QA across all
running prototypes.
