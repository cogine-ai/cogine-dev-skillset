# Input Contract

Resolve one complete product-design pair before development. Inputs may be local files or another
source the operator has authorized Codex to read.

## Required Product Inputs

Require all of:

- exactly one complete Build Card from `onsite-product-manager`;
- its linked product `context-freeze.md` path and freeze ID;
- comparison-batch ID, card ID, upstream product verdict, gate states, and named risks;
- an explicit operator instruction assigning that card to this prototype task.

`Evidence`, `Product distinctness`, `Validation`, `Mock honesty`, and `Handoff` must pass.
`Demonstrability` may carry a named execution risk. An operator-waived `Portfolio execution` gate
must remain visible and be acknowledged. The product freeze must be `READY` or operator-acknowledged
`READY WITH RISKS`. `NOT READY` blocks development.

The Build Card fixes the product proposition, actor, business moment, product form, mechanism, core
demo loop, real behavior, customer-visible result, mock boundary, validation question, acceptance
path, non-goals, and time budget. Do not reopen product ideation or select another card.

## Required Design Inputs

Require all of:

- exactly one Design Card from `onsite-product-design` with the same card and batch IDs;
- its linked `design-context.md` path and design freeze ID;
- the exact Build Card and product-freeze paths referenced by the Design Card;
- a visible preview path or accessible link;
- selected route, state map, reference lock, first-screen attention order, non-token consequence,
  reference mappings, explicit rejects, and visual acceptance checks;
- `DESIGN READY` as both the design bundle state and the card's development eligibility;
- recorded operator confirmation or explicit design-decision delegation.

Required design gates are `Upstream product`, `Visible evidence`, `Product-design fit`, `Portfolio
design distinctness`, `State completeness`, `Reference lock`, `Mock honesty`, `Decision`, `Handoff`,
and `Stop boundary`. They must pass. An explicit evidence waiver remains `waived` and does not count
as a pass for the 0.0.5 acceptance gate.

A missing Design Card returns `DESIGN REQUIRED`. A bundle in `AWAITING DESIGN DECISION`,
`PROVISIONAL - PRODUCT BLOCKED`, or `DESIGN NOT READY` returns `DESIGN BLOCKED`. Do not research a
visual route or synthesize a Design Card inside development.

The Design Card may shape presentation and interaction but may not alter the Build Card's product
mechanism, mock boundary, validation question, or non-goals. A mismatch returns the cards to the
upstream stage that introduced it.

## Project Input

Resolve one of:

- an explicitly identified existing target project path; or
- a compatible Project Template selected from the maintained registry or supplied by the operator,
  plus an authorized destination and project name.

If no project or template is identified, use the project-routing rules in `SKILL.md` and read
`project-template-registry.md`. Do not assume the current working directory is the target. A named
path that does not exist is not an existing project; treat it as a proposed destination only when the
operator clearly intends a new project.

Project routing is an implementation input. It must be resolved before target files are created or
modified, but it must not cause product or design decisions to be reopened.

For a parallel comparison batch, each card requires a unique target path, development-server port,
and proof directory. A shared authorized batch root is sufficient when this task derives a stable
child path from the batch and card IDs. A shared checkout, shared writable proof folder, or ambiguous
running URL is not a resolved route.

## Optional Inputs

- remaining onsite time;
- authorized synthetic assets or sample data;
- device and presentation constraints;
- authorized external services or disposable resources;
- local-only delivery or a separately requested publishing target.

When no time box is supplied, keep the first vertical slice as small as possible; do not promise a
specific elapsed time.

## Authority Order

Use this order when inputs conflict:

1. the operator's latest explicit correction;
2. the assigned Build Card and product freeze for product scope;
3. the matching Design Card and design freeze for presentation and interaction design;
4. the resolved target project's verified constraints;
5. Agent implementation inference.

A correction that changes the product proposition returns to `onsite-product-manager`. A correction
that changes the selected design route returns to `onsite-product-design`. Do not silently rewrite
either upstream card.

## Privacy

- Read product and design artifacts in place.
- Do not require or copy raw meeting text into the target project.
- Do not include customer-sensitive context, private reference assets, credentials, or internal URLs
  in commits, screenshots, public URLs, or build output.
- Put only synthetic or explicitly approved data and assets in the prototype.
