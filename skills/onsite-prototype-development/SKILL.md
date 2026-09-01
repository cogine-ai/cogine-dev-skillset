---
name: onsite-prototype-development
description: Build the smallest visually deliberate, demo-ready interactive business prototype from either full customer-meeting evidence and operator focus or one fixed Build Card from an onsite product portfolio. In discovery mode, frame and confirm the product and visual direction; in Build Card mode, preserve the upstream proposition, confirm or delegate only the visual and project route, then build the working loop. Use only when explicitly invoked for onsite sales prototyping, not for ordinary product development, Project Template authoring, static mockups, or transcript summarization.
---

# Onsite Prototype Development

Use this skill as a time-boxed sales-prototyping mode. Build the smallest complete interaction that
lets a customer operate something, observe processing or a decision, see state change, and receive a
business-meaningful result. The prototype may use clearly disclosed mock behavior, but the
demonstrated interaction must work.

Version 0.0.3 is an internal alpha that targets one fixed core business loop after the product and
visual decisions have been proved at the appropriate layer. Implement exactly one product proposition
and one selected visual route per task. Do not expand into ASR integration, Project Template
maintenance, production integration, or automatic publishing unless the user separately requests
that work.

## Entry Modes

- **Discovery mode:** use full meeting text, operator focus, and customer context to create one
  recommendation plus two materially different challengers. Confirm one product direction and one
  visual route, then build only that loop.
- **Build Card mode:** use exactly one Build Card and its parent product-document evidence from
  `onsite-product-manager`. The task assignment fixes the product proposition. Do not regenerate
  product directions, show challengers, ask the customer to choose a written product direction, or
  replace the card with a preferred idea. Validate the upstream gates, research the visual direction,
  resolve the project route, and build that card only.

One Build Card maps to one clean downstream task. A comparison batch runs as separate tasks so the
customer can see multiple materially different prototypes before choosing among them.

## Operating Principle

Accurate completion is more important than perfect hardening. Accuracy means that the operator has
confirmed the demo bet or explicitly delegated that decision, the customer-visible core loop works
end to end, every visible claim is truthful, mock boundaries are disclosed, and the result is ready
to present inside the time box.

For a new sales-critical surface, product divergence and visual design are part of accuracy rather
than optional polish. Product divergence may be proved locally in discovery mode or inherited from a
valid upstream portfolio in Build Card mode. Report the core-loop, direction-divergence, and
visual-design gates separately. A working interaction cannot substitute for missing direction or
design evidence, and changed color, type, radius, border, or shadow tokens do not by themselves prove
design.

Do not spend the onsite window perfecting adjacent behavior, broad test coverage, generalized
accessibility or security hardening, production architecture, or acceptance-grade proof for
non-critical details. Defer that work after the accurate core loop is ready. Never defer a blocker,
false success state, sensitive-data exposure, or material safety issue on the confirmed demo path.

## Start Contract

Before creating or modifying the target project:

1. Read [references/input-contract.md](references/input-contract.md), select exactly one entry mode,
   and resolve that mode's source inputs.
2. Read [references/context-freeze.md](references/context-freeze.md) and draft the business outcome
   outside the target repository.
3. Resolve the existing target project or Project Template source and destination route without
   creating or copying target files. When the operator has not supplied a project or template, read
   [references/project-template-registry.md](references/project-template-registry.md) and select a
   compatible registered template when one clearly fits. Never treat the current working directory
   as the target merely because it is open. Ask a routing question only for the unresolved part.
4. When a route is already resolved, read the existing target project's instructions and current
   implementation, or the source template's instructions and implementation when the target has not
   been instantiated. Use that evidence to verify the proposed direction is feasible. If a project or
   template source is supplied only in a reply to the pre-development check, treat that reply as routing
   input rather than final confirmation. Keep the brief `proposed`, inspect the source, update any
   affected assumptions, and obtain the confirmation required by the selected mode before marking it
   `confirmed`.
5. Read [references/direction-and-visual-research.md](references/direction-and-visual-research.md) and
   [references/demo-done.md](references/demo-done.md). In discovery mode, actively frame the product
   direction and prove divergence. In Build Card mode, validate and freeze the upstream proposition
   and divergence evidence without reopening product ideation. In both modes, establish a visual
   target when presentation quality is material and verify the smallest proof path against the
   resolved project evidence.
6. Present one compact pre-development check and wait for the confirmation required by the selected
   mode before creating or changing target files. Discovery mode confirms the product and visual
   direction together. Build Card mode treats the explicit card assignment as product confirmation,
   presents and preserves the fixed mock/deferred boundaries, and confirms only the visual direction
   and unresolved project route.
   Do not ask the operator to rewrite the card or choose another product direction.

In discovery mode, an instruction to build a prototype does not by itself waive this confirmation
gate. Requests such as "judge it yourself," "see what works," or "handle this as an onsite demo"
authorize the Agent to form and recommend the direction only; they do not authorize project creation
or development. Skip
the gate only when the operator unambiguously says that no confirmation is needed and delegates both
the business/visual direction and immediate target-project modification. If that authority is
ambiguous, keep the brief `proposed` and wait.

Before marking the brief `confirmed`, record the operator's actual confirmation or explicit waiver
and verify that the project route is resolved. In Build Card mode, record the exact task instruction,
card ID, parent document, context freeze, comparison batch, and upstream gate states as the product
confirmation evidence. Product confirmation does not waive visual evidence or visual confirmation.
Decision delegation lets the Agent make the still-open visual choice; it does not waive evidence
packets. An explicit evidence waiver must remain recorded as `waived`, never converted into `pass`.
The Agent's own recommendation, plan, phrase such as "direction frozen," or transition to Code is
never confirmation evidence.

Ask only when a missing answer would materially change the target project, core business loop, data
boundary, or feasible proof path. Otherwise state the assumption and continue.

## Project Routing

Use the first matching rule:

1. If the user explicitly identifies a target project, resolve its exact path and confirm that it
   exists and is accessible. Then use it after reading its repository instructions. If the path does
   not exist, do not treat it as an existing project. When the operator clearly intends a new
   project, treat the path only as the proposed destination and continue with template selection
   under rules 2–3. If that intent is ambiguous, ask only whether this is the intended new-project
   destination; do not also ask which template to use when the registry resolves one.
2. If the operator explicitly identifies a Project Template, resolve its source and fixed revision,
   then use it when its verified contract supports the demo bet. Do not replace an operator-supplied
   template with a registry entry.
3. Otherwise, read [references/project-template-registry.md](references/project-template-registry.md)
   and automatically select the narrowest compatible registered template. Do not ask the operator
   to identify a template that the registry already resolves.
4. Resolve a new project name and destination independently from template selection. When the task
   explicitly authorizes a new-project output root, propose a concise project slug inside it. If no
   destination is authorized, ask only for the destination in the pre-development check. Do not
   infer authorization from the current working directory.
5. If no registered template is compatible, include one concise request for a compatible template
   or target project in the pre-development check. Do not interrupt initial pre-development work with a
   separate routing exchange, silently edit the current directory, or create an arbitrary stack.

If the supplied path appears to be the template source itself, clarify whether the user intends to
create a project from it or intentionally edit it. When a Project Template is used, read
[references/template-protocol.md](references/template-protocol.md). For a non-template project,
follow that repository's own instructions and validation commands.

## Development Mode

Follow `Research -> Plan -> Code` while keeping each phase proportional to the onsite time box.

### Research

- In discovery mode, read the raw meeting text directly; do not route it through another AI summary
  service. In Build Card mode, read the Build Card and its parent product-document evidence; do not
  require or copy the private transcript into the target task.
- Inspect the target repository, its source, dependencies, instructions, and available validation
  path before changing it.
- Treat the operator's latest explicit direction as authoritative when it conflicts with transcript
  inference.
- In discovery mode, identify the priority already formed during the meeting and develop one
  recommendation plus two materially different challengers. Do not introduce a feature-voting
  exercise. In Build Card mode, preserve the assigned product proposition, product form, core demo
  loop, behavior that must be real, mock boundary, validation question, and non-goals. Do not create a
  new direction packet.
- When visual presentation can materially affect recognition or sales impact, automatically use the
  best available design-research capability according to the direction-and-visual-research contract.
  Do not wait for the operator to name Refero or another source.

### Plan

- Define one smallest complete vertical slice. It may contain a few tightly coupled functions when
  they are all necessary for the same demonstrable business loop.
- Express the path as `input/action -> processing/decision -> state change -> business result`.
- Preserve the confirmed visual target as an implementation constraint. Use one dominant direction;
  do not average unrelated references into a generic dashboard style.
- Preserve the confirmed non-token design consequence: the composition, information hierarchy,
  media role, interaction feedback, or state choreography that makes the core business moment
  recognizable even without its palette or typography.
- Keep the implementation inside the confirmed demo bet or fixed Build Card. Return to the operator
  only when new evidence materially contradicts it; do not silently reinterpret the product
  proposition during development.
- Mark all other product and visual directions as deferred rather than scaffolding, partially
  implementing, or silently merging them into the selected route.
- Prefer synthetic, customer-shaped demo data. Identify every mocked external boundary.

### Code

- Replace starter examples directly and reuse the target project's installed stack.
- Build real interactive state; do not substitute static screens, dead controls, or page navigation
  for the requested business behavior.
- Implement the visual target through the target project's editable application and theme surfaces.
  Do not modify Project Template foundations or protected UI components merely to force a style.
- Treat generic template composition with new tokens as an incomplete design, not a valid visual
  implementation. Preserve the confirmed reference-to-screen mapping and distinguishing move.
- Add focused behavior tests for non-trivial core-loop logic when a stable public seam exists and the
  repository requires or the time box safely permits them.
- Run the fastest sufficient repository-required validation and exercise the exact visible path in a
  real browser.
- Proof must not expand the product architecture. If a browser or test harness cannot observe a
  non-blocking detail, disclose the proof gap; do not add a backend, service, dependency, or new
  product behavior solely to make the tooling observe it.
- Stop and hand off immediately when the core path satisfies the Sales Demo Done contract. More
  discussed features, optional reviews, and non-blocking polish are not reasons to continue.

## Context and Safety

- Keep recordings, full transcripts, frozen context, customer-sensitive data, credentials, and
  secrets outside the target repository and public build artifacts.
- Use generalized product, industry, and interaction terms in external visual research. Never send
  raw meeting excerpts, customer identity, confidential data, or proprietary terminology to Refero
  or another external research service.
- Do not access customer, staging, production, paid, authenticated, or database resources without
  exact authorization for that resource and action.
- Use synthetic data by default and label mocked behavior in the handoff.
- Do not convert the prototype into production code or publish it automatically. Those are separate
  decisions and tasks.

## Handoff

Return the runnable prototype location and access method, one concise demo path, a short operator
talk track, implemented and deferred scope, mock and assumption boundaries, the visual target used,
verification evidence, and separate core-loop, direction-divergence, and visual-design gate states.
Use the exact reporting contract in
[references/demo-done.md](references/demo-done.md).
List possible improvements under deferred scope; do not implement them as part of the handoff.
