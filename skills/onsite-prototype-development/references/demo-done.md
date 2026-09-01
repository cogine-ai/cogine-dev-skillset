# Demo Completion Contract

The onsite prototype is runnable when the confirmed core business loop is accurately demonstrable.
Version 0.0.3 is accepted only when the core-loop, direction-divergence, and visual-design gates are
reported separately and all required gates pass. Feature count, page count, code volume, exhaustive
proof, and production hardening are not acceptance criteria. Accurate completion takes priority over
perfect engineering.

Use these states:

- **Core Loop:** `pass` or `fail`.
- **Direction Divergence:** `pass`, `fail`, `not proven`, or `waived`, with `source: local` in discovery
  mode or `source: upstream` in Build Card mode.
- **Visual Design:** `accepted`, `fail`, `awaiting acceptance`, `not proven`, `waived`, or `not material`.
- **0.0.3 Overall:** `pass` only when Core Loop is `pass`, Direction Divergence is `pass`, and Visual
  Design is `accepted` or legitimately `not material`. A waiver never counts as a pass.

A prototype may be runnable while 0.0.3 Overall remains `not pass`. Do not collapse these states into
one success claim.

## Required Behavior

- The UI uses the customer's business language and recognizable scenario.
- A user can perform a clear input or action through a clickable interface.
- The prototype visibly performs processing or a decision. Simulated behavior is acceptable only when
  it is coherent and disclosed.
- The operation changes meaningful state.
- The path ends in a business result the customer can understand.
- The flow can be repeated or reset for another demonstration.
- The demonstrated path contains no dead controls, fake success states, or blocking errors.
- When visual direction was material, the rendered core states preserve the confirmed visual thesis
  and named reference traits, including the non-token design consequence. Exact replication is not
  required; a token-only reskin is insufficient.

## Required Proof

- Run focused tests for non-trivial core-loop behavior when a stable seam exists and the repository
  requires or the time box safely permits them.
- Run the fastest sufficient repository-required validation. If repository instructions mandate a
  specific command, run it; otherwise do not broaden checks beyond the changed path.
- Drive the exact demo path through a real browser with user-like actions.
- Confirm the customer-visible result, reset path, and absence of blocking browser or runtime errors.
- Capture focused screenshot evidence of the customer action and business result.
- In discovery mode, preserve the confirmed direction packet or exact conversation reference and
  confirm that its alternatives passed the distinctness test. In Build Card mode, preserve the parent
  product-document reference, context freeze, comparison batch, card ID, upstream overall verdict,
  upstream gate states, and exact assignment instruction. Confirm that the implementation contains
  exactly the fixed card proposition and one selected visual route.
- When a visual target was confirmed, place the running input and result screenshots beside the
  target composition or exact references. Record promised non-token consequences as `visible`,
  `drifted`, or `not proven`, repeat the reskin counterfactual, and report material hierarchy,
  typography, spacing, color-role, component-character, imagery, or generic-design drift.
- Obtain the operator's explicit acceptance of the actual visual result. The implementing Agent's
  own QA cannot set `Visual Design: accepted`.
- Run the repository's privacy check when available; otherwise inspect the changed files and build
  output for meeting text, customer-sensitive data, and secrets.
- State every database, authentication, provider, deployment, or production boundary that remains
  unverified.

Lower-level tests do not prove the browser interaction. A screenshot of a static screen does not
prove the full loop.

Proof must describe the implementation truthfully; it must not drive new product scope. If the
available browser or test tooling cannot observe a non-critical event, report that proof gap or omit
the detail from the claim. Do not add a backend endpoint, dependency, service, or production-like
architecture solely to make an automated tool observe it.

## Stop Rule

`Sales Demo Done` is a hard stop. Once the confirmed loop works and the required implementation and
visual proof are ready, stop implementation and present the handoff for operator visual acceptance.
Do not continue polishing while waiting for that decision.

After Sales Demo Done, do not start optional static reviews, generalized hardening, refactors, new
backend work, additional feature tests, or adjacent UX polish unless the operator explicitly asks.
Fix only an issue that makes the confirmed path broken, materially misleading, unsafe, or capable of
exposing sensitive data. Preserve every other improvement as deferred scope.

Visual QA must not reopen alternative directions, create a second prototype, or continue as optional
polish after Sales Demo Done. If the operator rejects the actual visual result, make only the smallest
correction needed to satisfy the already confirmed evidence; a new visual direction requires a new
confirmation.

Reserve the final part of a supplied time box for proof and handoff; in a 30-minute session, reserve
at least the final five minutes. When that boundary is reached, stop adding behavior. If the core loop
is not yet complete, cut non-essential steps and report any remaining gap accurately rather than
chasing a perfect result past the delivery window.

## Handoff Format

Return:

1. **Run/access:** exact project path, command, and local URL or separately authorized published URL.
2. **Demo path:** a short sequence from customer action to business result and reset.
3. **Talk track:** a concise operator explanation focused on customer value.
4. **Implemented:** only behavior that actually works.
5. **Deferred:** discussed ideas intentionally left out.
6. **Mocked/assumed:** synthetic data, simulated processing, and unresolved assumptions.
7. **Proof:** commands run, browser path exercised, and observed result.
8. **Direction divergence:** entry mode, local packet or upstream product-document/card reference,
   distinctness evidence, source, and gate state.
9. **Visual design:** confirmed evidence, actual screenshot comparison, non-token consequence,
   operator acceptance, and gate state.
10. **Gate summary:** Core Loop, Direction Divergence, Visual Design, and 0.0.3 Overall.
11. **Not proven:** external or production boundaries that were not tested.

Do not claim production readiness. Publishing, production hardening, and conversion into a maintained
product are separate tasks.
