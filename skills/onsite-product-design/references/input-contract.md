# Input Contract

Read one complete output bundle from `onsite-product-manager`. Inputs may be local files or another
source the operator has authorized Codex to read.

## Required Product Inputs

Require all of:

- `onsite-product-board.md`;
- the linked upstream `context-freeze.md`;
- every `build-cards/Pxx.md` file in the stated comparison batch;
- matching freeze ID, comparison-batch ID, card IDs, upstream verdict, and gate states;
- an explicit operator instruction to design that portfolio.

Do not accept one isolated Build Card as a complete design input. The design stage must see the full
comparison batch to prevent accidental repetition and to preserve the promised 3-10 direction
portfolio.

Legacy Build Cards from `onsite-product-manager` v0.0.2 are valid when their existing fields and
linked context freeze are complete. Do not require product cards to contain visual decisions.

## Upstream Eligibility

- `READY`: eligible for a confirmed design bundle.
- `READY WITH RISKS`: eligible only after the operator acknowledges the named upstream risks.
- `NOT READY`: may receive `PROVISIONAL - PRODUCT BLOCKED` visible exploration, but every Design Card
  must block development.

Required product gates are `Evidence`, `Product distinctness`, `Validation`, `Demonstrability`,
`Portfolio execution`, `Mock honesty`, and `Handoff`. Preserve their exact states. Do not use design
quality to repair failed product evidence.

If the comparison batch contains fewer than three cards, require the exact upstream portfolio waiver
and keep its risk visible. Do not silently invent cards or choose a subset.

## Optional Design Inputs

- approved customer brand rules or design system;
- operator-provided screenshots, Figma frames, flows, references, or visual rejects;
- customer terminology, media, and anonymized sample data already authorized for design use;
- desired device, room/display constraints, or accessibility needs;
- remaining onsite time and explicit authority to choose the design routes without a second
  confirmation.

Absence of optional visual material does not block research. Use Refero or a visible Agent-derived
fallback according to `visual-research.md`.

## Authority Order

When design sources conflict, use:

1. the operator's latest explicit instruction or correction;
2. approved customer brand, Figma, screenshots, and design-system evidence;
3. fixed product facts in the Build Card and upstream context freeze;
4. authorized external visual research;
5. Agent design inference.

A correction that changes the actor, product mechanism, business result, core demo loop, validation
question, or mock boundary is a product change. Return it to `onsite-product-manager`; do not rewrite
the Build Card inside design work.

## Privacy

- Read upstream artifacts in place and keep raw meeting sources out of design outputs.
- Send only generalized product, industry, and interaction concepts to external design services.
- Never send customer names, raw meeting text, internal URLs, confidential assets, or commercial
  details to Refero or another external service.
- Use synthetic or explicitly authorized data in previews.
- Record exact external references without copying protected assets into the Skill repository.
