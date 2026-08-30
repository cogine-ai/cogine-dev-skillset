---
name: onsite-prototype-development
description: Turn a full customer-meeting transcript, operator focus notes, and customer context into the smallest demo-ready interactive business prototype inside an explicitly chosen project or compatible Project Template. Use only when the user explicitly invokes this onsite sales-prototyping mode; do not use for ordinary product development, Project Template authoring, static mockups, or transcript summarization alone.
---

# Onsite Prototype Development

Use this skill as a time-boxed sales-prototyping mode. Build the smallest complete interaction that
lets a customer operate something, observe processing or a decision, see state change, and receive a
business-meaningful result. The prototype may use clearly disclosed mock behavior, but the
demonstrated interaction must work.

Version 0.0.1 is an internal alpha that targets one core business loop. Do not expand it into
simultaneous generation of many prototype variants, ASR integration, Project Template maintenance,
production integration, or automatic publishing unless the user separately requests that work.

## Operating Principle

Accurate completion is more important than perfect hardening. Accuracy means that the operator has
confirmed the demo bet or explicitly delegated that decision, the customer-visible core loop works
end to end, every visible claim is truthful, mock boundaries are disclosed, and the result is ready
to present inside the time box.

Do not spend the onsite window perfecting adjacent behavior, broad test coverage, generalized
accessibility or security hardening, production architecture, or acceptance-grade proof for
non-critical details. Defer that work after the accurate core loop is ready. Never defer a blocker,
false success state, sensitive-data exposure, or material safety issue on the confirmed demo path.

## Start Contract

Before creating or modifying the target project:

1. Read [references/input-contract.md](references/input-contract.md) and resolve the source inputs.
2. Read [references/context-freeze.md](references/context-freeze.md) and draft the business outcome
   outside the target repository.
3. Resolve the existing target project or Project Template source and destination route without
   creating or copying target files. Never treat the current working directory as the target merely
   because it is open.
4. Read the existing target project's instructions and current implementation, or the source
   template's instructions and implementation when the target has not been instantiated.
5. Read [references/demo-done.md](references/demo-done.md) and define one recommended demo bet and its
   smallest proof path.
6. Present the demo bet to the operator and wait for explicit confirmation before creating or
   changing target project files. Confirm the customer problem, core loop, customer-visible result,
   mock boundary, and deferred scope. Do not ask the operator to write a detailed specification or
   select from every meeting idea.

An instruction to build a prototype does not by itself waive this confirmation gate. Skip it only
when the operator explicitly says to proceed without confirmation or to decide and build directly.
After confirmation or explicit delegation, record the operator's decision in the external context
freeze, mark it confirmed, and enter development.

Ask only when a missing answer would materially change the target project, core business loop, data
boundary, or feasible proof path. Otherwise state the assumption and continue.

## Project Routing

Use the first matching rule:

1. If the user explicitly identifies a target project, resolve its exact path and confirm that it
   exists and is accessible. Then use it after reading its repository instructions. If the path does
   not exist, ask whether the path is incorrect or the user intends to create a project there from a
   specific template; do not create an arbitrary project.
2. Otherwise, if a compatible Project Template is identified, prefer creating a new project from
   that fixed template version. Resolve the destination path and project name before writing, but do
   not instantiate the target until the demo bet is confirmed or explicitly delegated.
3. If neither a target project nor a compatible template is clear, ask the user which existing
   project or template to use. Do not silently edit the current directory or create an arbitrary
   stack.

If the supplied path appears to be the template source itself, clarify whether the user intends to
create a project from it or intentionally edit it. When a Project Template is used, read
[references/template-protocol.md](references/template-protocol.md). For a non-template project,
follow that repository's own instructions and validation commands.

## Development Mode

Follow `Research -> Plan -> Code` while keeping each phase proportional to the onsite time box.

### Research

- Read the raw meeting text directly; do not route it through another AI summary service.
- Inspect the target repository, its source, dependencies, instructions, and available validation
  path before changing it.
- Treat the operator's latest explicit direction as authoritative when it conflicts with transcript
  inference.
- Identify the priority already formed during the meeting. Do not introduce a separate exercise that
  lists all discussed features and then selects one.

### Plan

- Define one smallest complete vertical slice. It may contain a few tightly coupled functions when
  they are all necessary for the same demonstrable business loop.
- Express the path as `input/action -> processing/decision -> state change -> business result`.
- Keep the implementation inside the confirmed demo bet. Return to the operator only when new
  evidence materially contradicts it; do not silently reinterpret the bet during development.
- Mark all other ideas as deferred rather than silently implementing them.
- Prefer synthetic, customer-shaped demo data. Identify every mocked external boundary.

### Code

- Replace starter examples directly and reuse the target project's installed stack.
- Build real interactive state; do not substitute static screens, dead controls, or page navigation
  for the requested business behavior.
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
- Do not access customer, staging, production, paid, authenticated, or database resources without
  exact authorization for that resource and action.
- Use synthetic data by default and label mocked behavior in the handoff.
- Do not convert the prototype into production code or publish it automatically. Those are separate
  decisions and tasks.

## Handoff

Return the runnable prototype location and access method, one concise demo path, a short operator
talk track, implemented and deferred scope, mock and assumption boundaries, and verification evidence.
Use the exact reporting contract in [references/demo-done.md](references/demo-done.md).
List possible improvements under deferred scope; do not implement them as part of the handoff.
