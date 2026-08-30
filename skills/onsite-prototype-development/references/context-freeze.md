# Context Freeze

Create a compact proposed development brief before coding. Keep it in the conversation or an
external session workspace, never inside the target repository. The brief becomes frozen only after
the operator confirms the demo bet or explicitly delegates that decision.

A proposed business outcome can be drafted before the target route is resolved. Confirm and freeze it
after the existing target project or source template has been resolved, its relevant instructions
have been read, and the demo bet is known to be feasible inside the time box. Do not instantiate a
new target project before the confirmation gate.

The brief must contain:

- **Status:** `proposed` before operator confirmation or delegation and `confirmed` afterward.
- **Business situation:** who the customer is and what operational problem is being discussed.
- **Demo bet:** the one recommended customer-facing experience most likely to create recognition or
  interest during this meeting.
- **Core demo outcome:** one sentence describing what the customer must be able to experience.
- **Demo loop:** actor, trigger/input, processing or decision, state change, and business result.
- **Customer language:** terms, roles, entities, and visible data the prototype should use.
- **Operator direction:** the priority, corrections, and constraints supplied by the technical
  operator.
- **Mock boundary:** synthetic data, simulated processing, and unconnected external systems.
- **Deferred scope:** discussed ideas not needed for the current loop.
- **Unknowns:** only unresolved assumptions that could affect the demo or its proof.
- **Time box:** remaining time when supplied.
- **Operator confirmation:** the confirmed direction, the operator's concise correction, or explicit
  delegation to decide and proceed.

Do not turn the transcript into a broad requirements document. The freeze exists to stabilize one
demonstrable outcome, not to preserve every idea as active scope.

## Confirmation Gate

Present one recommended demo bet in a compact form:

1. The customer problem the prototype will make visible.
2. The proposed core interaction loop.
3. The business result the customer will see.
4. The boundaries that will be mocked.
5. The important ideas intentionally deferred.

Ask the operator whether to proceed with that bet. This is a direction confirmation, not a request
for detailed requirements, field definitions, screen specifications, or implementation choices. Do
not create or modify the target project until the operator confirms or explicitly delegates the
decision.

If the operator corrects the bet, update the smallest affected part of the proposed brief and confirm
again. Once confirmed, record the decision and avoid reopening it for non-consequential details.

## Updates After Freeze

New transcript text is additional evidence, not an automatic instruction to restart or replan active
development.

Change the confirmed core direction when the operator explicitly updates or corrects the development focus.
Record the amendment in the brief, identify what current work it invalidates, and adjust the smallest
possible scope. If new evidence contradicts the current loop but the operator's intent is unclear,
pause only that decision and ask.
