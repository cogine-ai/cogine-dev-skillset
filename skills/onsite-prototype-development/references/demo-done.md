# Sales Demo Done Contract

The onsite prototype is runnable when its fixed core business loop is accurately demonstrable.
Version 0.0.5 is accepted only when the core-loop, upstream-direction, and visual-design gates are
reported separately and all required gates pass. Feature count, page count, code volume, exhaustive
proof, and production hardening are not acceptance criteria.

Use these states:

- **Core Loop:** `pass` or `fail`.
- **Direction Divergence:** `pass`, `fail`, `not proven`, or `waived`; always cite the upstream product
  freeze and `Product distinctness` gate.
- **Visual Design:** `accepted`, `fail`, `awaiting acceptance`, `not proven`, or `waived`; cite the
  Design Card, design preview or reference lock, running screenshots, and operator acceptance.
- **0.0.5 Overall:** `pass` only when Core Loop is `pass`, Direction Divergence is `pass`, and Visual
  Design is `accepted`. A waiver never counts as a pass.
- **Batch Portfolio:** `pass`, `drift`, or `not proven`; source it from the post-build portfolio QA in
  `onsite-product-design`. Until every completed prototype has been compared side by side, the batch
  is not ready to claim visual diversity even when this individual prototype passes.

A prototype may be runnable while 0.0.5 Overall remains `not pass`. Do not collapse the states into
one success claim.

## Required Behavior

- The UI uses recognizable customer business language and synthetic or authorized scenario data.
- A user can perform a clear input or action through a clickable interface.
- Processing or a decision is visibly represented; simulated intelligence is coherent and disclosed.
- The operation changes meaningful state and ends in a business result the customer can understand.
- The flow can be repeated or reset.
- The demonstrated path contains no dead controls, fake success states, or blocking errors.
- The rendered core states preserve the Design Card's design thesis, attention order, state map,
  reference mappings, and non-token consequence. A token-only reskin is insufficient.

## Required Proof

- Run focused tests for non-trivial core-loop behavior when a stable seam exists and the repository
  requires or the time box safely permits them.
- Run the fastest sufficient repository-required validation.
- Drive the exact demo path through a real browser with user-like actions.
- Confirm the result, reset path, and absence of blocking browser or runtime errors.
- Confirm the running URL and visible product identity belong to this exact batch/card target rather
  than another parallel task.
- Capture focused screenshots showing the customer input/action and successful business result.
- Preserve the Build Card, product-freeze path and ID, comparison batch, upstream verdict and gates,
  and exact assignment. Confirm that the implementation contains exactly that proposition.
- Preserve the Design Card, design-context path and ID, selected route, operator decision, visible
  preview, reference lock, and acceptance checks. Confirm that exactly that route was implemented.
- Place running input and result screenshots beside the preview or exact design references. Record
  each promised non-token consequence as `visible`, `drifted`, or `not proven` and repeat the reskin
  counterfactual against the running UI.
- Obtain the operator's explicit acceptance of the actual visual result. The implementing Agent's own
  QA cannot set `Visual Design: accepted`.
- Run the repository privacy check when available; otherwise inspect changed files and build output
  for meeting text, customer-sensitive data, private assets, and secrets.
- State every database, authentication, provider, deployment, persistence, or production boundary
  that remains unverified.

Lower-level tests do not prove the browser interaction. A static screenshot does not prove the full
loop. Design-preview quality does not prove the implemented UI.

## Stop Rule

`Sales Demo Done` is a hard stop. Once the fixed loop works and implementation and visual proof are
ready, stop and present the handoff for operator visual acceptance. Do not continue polishing while
waiting for that decision.

After Sales Demo Done, do not start optional reviews, generalized hardening, refactors, backend work,
additional feature tests, or adjacent UX polish unless explicitly requested. Fix only an issue that
makes the confirmed path broken, materially misleading, unsafe, or capable of exposing sensitive
data. Preserve all other ideas as deferred scope.

Visual QA must not reopen alternative routes. If the operator rejects the running result, make only
the smallest correction needed to satisfy the existing Design Card. A new route returns to
`onsite-product-design`.

Reserve the final part of a supplied time box for proof and handoff. In a 30-minute development
window, reserve at least the final five minutes. When that boundary is reached, cut non-essential
steps and report gaps honestly instead of chasing perfection.

## Handoff Format

Return:

1. **Run/access:** exact project path, command, and local URL or separately authorized published URL.
2. **Demo path:** short sequence from customer action to business result and reset.
3. **Talk track:** concise operator explanation focused on customer value.
4. **Implemented:** only behavior that actually works.
5. **Deferred:** discussed ideas intentionally left out.
6. **Mocked/assumed:** synthetic data, simulated processing, and unresolved assumptions.
7. **Proof:** commands run, browser path exercised, screenshots, and observed result.
8. **Batch isolation:** target path, server port, proof directory, and verified batch/card identity.
9. **Product source:** Build Card, product freeze, upstream gates, assignment, and Direction
   Divergence state.
10. **Design source:** Design Card, design context, preview/reference lock, actual screenshot
   comparison, non-token consequence, operator acceptance, and Visual Design state.
11. **Gate summary:** Core Loop, Direction Divergence, Visual Design, and 0.0.5 Overall.
12. **Batch status:** linked portfolio runtime review, or `not proven` until the full batch is ready.
13. **Not proven:** external or production boundaries not tested.

Do not claim production readiness. Publishing, production hardening, and conversion into a
maintained product are separate tasks.
