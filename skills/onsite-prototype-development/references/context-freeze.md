# Development Freeze

Create a compact proposed development brief outside the target repository before coding. This brief
links the immutable product and design handoffs to one verified project route; it does not repeat the
meeting, regenerate product options, or create another design proposal.

The brief becomes `confirmed` only when all required upstream product and design gates pass, the
operator has explicitly assigned the matching cards to development, the target route is resolved,
and the fixed loop is feasible in that target.

## Required Fields

- **Status:** `proposed`, `confirmed`, or `blocked`.
- **Assignment:** the operator's exact instruction to develop this card pair.
- **Source locks:** Build Card, product freeze, Design Card, and design-context paths and IDs; matching
  batch/card IDs; upstream verdicts and required gate states; acknowledged risks; operator design
  decision; preview path. Reference the upstream fields instead of copying them.
- **Fixed outcome:** one sentence plus
  `input/action -> processing/decision -> state change -> business result -> reset`; cite the exact
  Build Card and Design Card constraints that implementation must preserve.
- **Project route and evidence:** existing target, or fixed Project Template source/revision plus
  authorized destination/name; repository instructions, editable boundaries, required commands, and
  compatibility conclusion.
- **Batch isolation:** unique target path, server port, and proof directory for this batch/card pair.
- **Implementation slice:** the smallest real behavior required for the loop.
- **Mock and deferred boundary:** simulated systems and production properties not claimed; all
  behavior and polish outside the fixed loop.
- **Proof path:** behavior seam when applicable, repository validation, exact browser interaction,
  reset, screenshots, runtime errors, privacy check, and visual comparison.
- **Blockers and time:** only unresolved facts that could stop the loop or proof; remaining time when
  supplied.

Do not place this freeze inside the target project. Do not overwrite the upstream product or design
freeze.

## Compact Pre-Development Check

Present once:

1. `Pxx`, fixed proposition, and the one core demo loop;
2. selected design route, visible preview, and non-token consequence;
3. real behavior, simulated boundaries, and explicit cuts;
4. target project or Project Template route;
5. unique batch/card target, port, and proof route;
6. fastest sufficient proof path;
7. any actual blocker.

Do not ask the operator to choose the product or visual direction again. The matching assignment plus
valid upstream decisions already settles them. Ask only when project routing or modification
authority is missing, target evidence contradicts a fixed card, or a required product/design gate is
not valid.

If the cards or project route change materially after freeze, update only the affected fields and
recheck feasibility before coding.
