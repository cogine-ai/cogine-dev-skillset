# Context Freeze

Create a compact proposed development brief before coding. Keep it in the conversation or an
external session workspace, never inside the target repository. The brief becomes frozen only after
the operator confirms the demo bet or explicitly delegates that decision.

A proposed business outcome can be drafted before the target route is resolved. Confirm and freeze it
after the existing target project or source template has been resolved, its relevant instructions
have been read, and the demo bet is known to be feasible inside the time box. Do not instantiate a
new target project before the confirmation gate.

The brief must contain:

- **Status:** `proposed` until an actual operator message explicitly confirms the combined direction
  or unambiguously waives confirmation and delegates immediate development; `confirmed` only after
  that evidence exists.
- **Business situation:** who the customer is and what operational problem is being discussed.
- **Product framing:** the recommended form of the experience and why it best expresses the customer
  outcome.
- **Direction packet:** one recommendation and two materially different challengers, each with actor,
  trigger, interaction model, state change, customer-visible result, mocked boundary, and reason for
  its rank. If the evidence supports fewer honest directions, record the gap instead of inventing one.
- **Direction divergence:** `pass`, `not proven`, or `waived`, with the evidence or actual waiver. A
  confirmed recommendation does not by itself make this gate pass.
- **Demo bet:** the one recommended customer-facing experience most likely to create recognition or
  interest during this meeting.
- **Core demo outcome:** one sentence describing what the customer must be able to experience.
- **Demo loop:** actor, trigger/input, processing or decision, state change, and business result.
- **Customer language:** terms, roles, entities, and visible data the prototype should use.
- **Operator direction:** the priority, corrections, and constraints supplied by the technical
  operator.
- **Visual target:** the intended impression, primary design basis, key visual roles, distinguishing
  move, and explicit rejects when visual presentation is material; otherwise state which approved
  existing design system remains authoritative.
- **Visual evidence:** exact generalized reference IDs or URLs when used, visible reference or
  Agent-derived fallback material, target composition, `reference trait -> business reason ->
  screen/state consequence` mappings, the non-token design consequence, and the reskin
  counterfactual. When an external design-research capability was unavailable, record the fallback
  label and its visible annotated compositions.
- **Visual direction:** `pass`, `not proven`, `waived`, or `not material`, with the evidence or actual
  waiver. A theme description or a record of Refero calls is not evidence of pass.
- **Project route:** the confirmed target project, or Project Template source and destination. It may
  remain unresolved only while the brief is `proposed`.
- **Mock boundary:** synthetic data, simulated processing, and unconnected external systems.
- **Deferred scope:** discussed ideas not needed for the current loop.
- **Unknowns:** only unresolved assumptions that could affect the demo or its proof.
- **Time box:** remaining time when supplied.
- **Operator confirmation:** the operator's actual confirmation, concise correction, or explicit
  waiver and delegation to decide and proceed. Preserve a concise quote or faithful paraphrase of the
  operator message and the chosen direction/visual packet version; never substitute an Agent-authored
  recommendation or status label.

Do not turn the transcript into a broad requirements document. The freeze exists to stabilize one
demonstrable outcome, not to preserve every idea as active scope.

## Confirmation Gate

Present one compact decision package:

1. The customer problem the prototype will make visible.
2. One recommended product framing and two materially different challengers.
3. The recommended core interaction loop and business result.
4. The visual routes and evidence packet when visual presentation is material.
5. The boundaries that will be mocked.
6. The important ideas intentionally deferred.
7. The target project or Project Template route when it has not yet been supplied.

Ask the operator once whether to proceed with the business and visual direction together. This is a
direction confirmation, not a request for detailed requirements, field definitions, screen
specifications, implementation choices, or the name of a design source. Do not create or modify the
target project until the operator confirms or explicitly delegates the decision and the project route
is resolved.

Asking the Agent to judge, recommend, explore, or handle the request in onsite-demo mode is not
explicit delegation to modify files. A waiver must clearly state that confirmation is unnecessary
and that the Agent may decide the business and visual direction and start development immediately.
Decision delegation does not waive the evidence packets. A separate explicit evidence waiver must be
recorded as `waived`, cannot be reported as `pass`, and must remain visible in the handoff. When in
doubt, leave the brief `proposed`.

If the operator corrects the bet, update the smallest affected part of the proposed brief and confirm
again. Once confirmed, record the decision and avoid reopening it for non-consequential details.

## Updates After Freeze

New transcript text is additional evidence, not an automatic instruction to restart or replan active
development.

Change the confirmed core direction when the operator explicitly updates or corrects the development focus.
Record the amendment in the brief, identify what current work it invalidates, and adjust the smallest
possible scope. If new evidence contradicts the current loop but the operator's intent is unclear,
pause only that decision and ask.
