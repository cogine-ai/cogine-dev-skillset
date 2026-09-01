# Input Contract

Resolve exactly one product-input mode before development. Inputs may be pasted text, local files, or
other sources the user has authorized Codex to read.

## Discovery Mode

- **Raw meeting text:** the full transcript or the fullest available verbatim text. Do not replace it
  with a third-party AI summary.
- **Operator focus:** the technical operator's short description of what matters most now, including
  corrections, priority, and any idea that must be demonstrated.

If either source is absent, request it or ask the operator to explicitly authorize the available
source as the substitute. Do not fabricate missing meeting content.

In discovery mode, these are the only product-definition inputs required from the operator. Do not
require the operator to name a product form, prepare a feature list, request alternatives, choose a
visual direction, or name a design-research tool. The Agent owns that reasoning and proposes the
consequential decisions at the confirmation gate.

Treat the operator's statement that supplied meeting text is complete or is the fullest available
source as authoritative. Do not reject or reclassify it merely because it is short, compressed, or
well organized. Ask about completeness only when the operator says the source is partial or when a
missing segment creates a material contradiction in the core demo outcome.

## Build Card Mode

Require all of:

- exactly one complete Build Card from `onsite-product-manager`;
- its linked upstream `context-freeze.md` path from `onsite-product-manager`;
- source context-freeze ID, comparison-batch ID, card ID, and upstream overall verdict;
- upstream `Evidence`, `Product distinctness`, `Validation`, `Demonstrability`, `Portfolio execution`,
  `Mock honesty`, and `Handoff` gate states;
- an explicit operator instruction assigning that card to this prototype task.

`Evidence`, `Product distinctness`, `Validation`, `Mock honesty`, and `Handoff` must pass.
`Demonstrability` may carry a named execution risk, and an operator-waived `Portfolio execution`
gate must remain visible and be acknowledged in the assignment. Any failed or unproven required gate
blocks development.

The Build Card must preserve the product proposition, actor and business moment, product form and
usage surface, distinct mechanism, core demo loop, behavior that must be real, customer-visible
result, mock boundary, validation question, acceptance path, non-goals, and time budget. The upstream
context freeze must be `READY` or `READY WITH RISKS`. The latter requires the operator to acknowledge
the named risks in the assignment. A `NOT READY` context freeze blocks development; do not convert its
provisional cards into implementation scope.

The explicit assignment fixes the product proposition for this task. Do not reopen product ideation,
generate challengers, select another card, or ask the customer to approve a written direction. If
multiple cards are supplied, do not choose among them: request one card per clean downstream task.

Raw meeting text and general customer context are not required in Build Card mode. Read the minimum
anonymized evidence in the card and upstream context freeze; do not copy private transcripts into the
target task or repository. `onsite-product-board.md` is optional and may be read for portfolio names
and presentation order, but it cannot replace the card or upstream context freeze.

## Project Input

Resolve one of:

- An explicitly identified target project path.
- A compatible Project Template selected from the maintained registry or supplied by the operator,
  plus a target project name and destination.

If no project or template is identified, apply the project-routing rules in `SKILL.md` and read
`project-template-registry.md`. Do not ask the operator to name a template when one registered entry
clearly fits. Do not assume that the current working directory is the target. A named path that does
not exist is not a resolved existing project; ask whether the path should be corrected or created
as a new-project destination. Select the template separately through the registry when one clearly
fits.

The project route is an execution input, not part of the operator's product brief. Its absence must
not block initial product framing in discovery mode or visual research in either mode. Ask only for
the unresolved part of the route in the pre-development check, and resolve the route before creating
or modifying target files.

## Optional Inputs

- Established customer background context.
- Remaining onsite time or another explicit time box.
- Existing brand, terminology, screenshots, documents, sample data, or design references.
- Authorized external services or disposable resources.
- Delivery constraints such as local-only operation or a separately requested publishing target.

When no time box is supplied, assume a short onsite session and keep the first vertical slice as small
as possible; do not promise a specific elapsed time.

## Authority Order

In discovery mode, use this order when sources conflict:

1. The operator's latest explicit instruction or correction.
2. The operator focus note.
3. Explicitly established customer background context.
4. The raw meeting transcript.
5. Agent inference.

Expose consequential conflicts in the frozen brief. Never let an inference override an explicit
operator direction.

In Build Card mode, use the operator's latest explicit correction, then the assigned Build Card,
upstream context freeze, resolved target-project evidence, and Agent inference. A correction that
changes the product proposition invalidates the card assignment; return it to the product layer
instead of silently rewriting the card.

## Privacy Handling

- Read source material in place when possible.
- Do not copy raw meeting text or customer-sensitive context into the target repository.
- Do not include raw source material in commits, logs, screenshots, public URLs, or build output.
- Put only synthetic or explicitly approved data in the prototype.
