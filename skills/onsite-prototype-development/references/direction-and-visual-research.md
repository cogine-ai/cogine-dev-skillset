# Product Direction And Visual Research

Use this workflow before the confirmation gate. In discovery mode, the operator supplies the fullest
meeting text, a short focus note, and customer context when available. In Build Card mode, the
operator supplies one fixed card and its parent product-document evidence. A target project or
template is an execution input that may be supplied initially or resolved in the pre-development
check. The operator does not need to request divergent ideas in discovery mode, name Refero, choose a
design method, or specify a fixed number of visual routes.

## Build Card Mode

When the input is a valid upstream Build Card, do not run product-direction ideation. Validate the
parent document, context freeze, comparison batch, card ID, overall verdict, and upstream gate states.
Freeze the card's actor, business moment, product proposition, product form, distinct mechanism, core
demo loop, required real behavior, customer-visible result, mock boundary, validation question, and
non-goals.

Use the upstream `Product distinctness` gate as the Direction Divergence evidence only when the parent
document is `READY` or operator-acknowledged `READY WITH RISKS`, the card belongs to its stated
comparison batch, and the evidence is accessible. Record `source: upstream` in the gate. Do not
manufacture a local direction packet, challengers, or a second product decision. If the upstream
evidence is absent or not passing, stop and return the contract gap.

Continue with visual research below. Product form and core demo states are fixed inputs to that
research, not options to reopen.

## Frame The Product Direction

This section applies only in discovery mode.

Infer the underlying business outcome, the actor who needs it, the costly or confusing moment being
changed, and the visible evidence that would make the customer recognize the value.

Create a compact direction packet with one recommendation and two challengers before the
pre-development confirmation. Useful lenses may include a focused workbench, guided workflow,
agent workspace, monitoring or BI surface, knowledge retrieval, browser sidecar, or generated
decision artifact.
These are prompts for reasoning, not a menu that must be copied.

For each direction state:

- product form and the reason it fits the evidence;
- primary actor and entry trigger;
- interaction model and meaningful state change;
- customer-visible result;
- smallest demo loop and mocked boundary;
- why it is recommended or not recommended.

Two directions are materially distinct only when their product form or experience topology differs
and at least one of interaction model, state change, or customer-visible result also differs. Actor or
entry-trigger changes alone are insufficient. Renaming the product, changing the layout, adding Top-N
choices, moving the same loop behind chat, or changing only visual tokens does not create another
direction. For example, three variants of
`screenshot -> match SKU -> confirm -> quote -> CSV` are one product bet.

Evaluate each framing against:

- fidelity to the transcript, operator focus, and established customer context;
- strength and immediacy of the customer-visible business result;
- whether the customer can operate it and observe meaningful state change;
- feasibility inside the remaining time and resolved project contract;
- honesty of the synthetic-data and mocked-system boundary;
- fit with established team capabilities or constraints, without inventing capabilities.

Recommend the strongest framing without making the operator discover the answer. The challengers
exist to expose the decision boundary, not to turn every discussed feature into a vote. If the source
evidence cannot support three honest directions, do not invent capabilities: show the supported
directions, mark `Direction Divergence: not proven`, and request an explicit waiver before building.
Decision delegation may authorize the Agent to choose; it does not remove the packet or convert a
waiver into a pass.

## Decide Whether Visual Research Is Material

Treat visual research as material by default for a new customer-facing onsite prototype, a
sales-critical first impression, a major change in product form, or a prototype without an approved
design system. It is not material only when the target already has a concrete approved visual system
and this prototype is a small extension that should visibly preserve it.

Use the first suitable source:

1. Preserve explicit operator-provided brand rules, screenshots, Figma frames, or an approved project
   design system as the primary constraint.
2. If the `refero-design` skill is available, use it as the visual-research authority while keeping
   this skill's onsite time box, confirmation gate, project boundary, and stop rule authoritative.
3. Otherwise, if Refero MCP capabilities are available, use them directly. Start with Styles for
   visual direction, then use Screens for hierarchy and concrete states or Flows for multi-step
   journeys when those layers materially affect the demo.
4. If Refero is unavailable, use the approved project language and other authorized references. If
   none exists, derive two visibly different annotated compositions from the desired customer
   impression, product form, information hierarchy, and interaction states, then label them as
   Agent-derived fallback evidence. Do not ask the operator to install a tool merely to continue, and
   do not block the pre-development check solely because an external design-research capability
   is absent.

When using Refero directly, inspect distinct search angles derived from the customer, domain, desired
impression, and product form. Choose one dominant reference foundation. Give any secondary reference
a narrow role, such as navigation density, table treatment, or interaction feedback. Never copy a
single product wholesale, average references into a safe middle, reuse third-party assets without
authorization, or claim reference imagery as product evidence.

For a blank or visually unresolved target, present two materially different visual routes before
confirmation. When references are available, each route must surface the actual reference image or
an accessible exact source ID or URL, explain the reference's bounded role, and show how the core
business state would be composed. For an Agent-derived fallback, show an annotated wireframe or
screen map for each route and keep the source labeled as fallback. Named brands, mood adjectives,
palette descriptions, or a list of searched products are not visual evidence. When an approved
design system is authoritative, present its actual screen or component evidence instead of inventing
a second style.

Relevant Refero MCP capability names commonly include `refero_search_styles`, `refero_get_style`,
`refero_search_screens`, `refero_get_screen`, `refero_get_similar_screens`,
`refero_get_screen_image`, `refero_search_flows`, and `refero_get_flow`. Treat availability as a
runtime fact; do not assume those tools exist because Refero was used in a previous session.

## Distinguish Design From A Reskin

A reskin is a change that can be fully explained by palette, font, radius, border, shadow, generic
icons, or moving the same standard cards into another grid. If those tokens are hidden and the
template's attention order, media role, interaction feedback, and state expression remain unchanged,
the result is still a reskin.

A designed direction must contain at least one observable non-token consequence tied to the core
business moment. It may change composition, information hierarchy, media role, interaction feedback,
or state choreography. Removing it would change what the customer notices first, how they understand
the value, or how they perceive the state change. Novelty is not required; a business-specific,
evidence-backed decision is.

## Create A Visual Lock

Record a compact visual target in the proposed context freeze:

- intended impression and why it fits this customer;
- primary design source or approved existing system;
- information hierarchy and layout character;
- typography, density, and spacing character;
- color roles, including what receives emphasis;
- component and interaction character;
- imagery or media role when relevant;
- one distinguishing visual or interaction move;
- explicit rejects that would make the result feel generic or off-brand.

Also record a visual evidence packet:

- exact primary and bounded secondary reference IDs or URLs when references are used, with the
  visible references shown to the operator when the tool permits it; otherwise the explicit
  Agent-derived fallback label and its visible compositions;
- a compact target composition for the core state, such as an annotated wireframe, layout sketch, or
  reference-backed screen map;
- `reference trait -> business reason -> target screen/state consequence` mappings;
- the non-token design consequence and where it will appear;
- the reskin counterfactual: what remains recognizably designed after palette, typography, radius,
  border, and shadow are ignored.

If the counterfactual has no concrete answer, mark the route `reskin` and do not recommend it as the
visual direction. Refero calls, completed fields, or a theme-token diff are not substitutes for this
evidence.

Use semantic roles rather than copying raw style values without understanding them. Avoid automatic
fallbacks such as one default AI palette, cards around every section, decorative gradients, or a
generic SaaS dashboard shell when the researched direction does not support them.

## One Pre-Development Check

In discovery mode, before target files are created or modified, present one compact confirmation
containing:

1. the direction packet: one recommendation and two materially different challengers;
2. the recommended core interaction loop and customer-visible result;
3. the visual routes and visual evidence packet when visual research is material;
4. mocked systems or synthetic data;
5. intentionally deferred scope;
6. the target project or Project Template route when it remains unresolved;
7. separate proposed states for `Direction Divergence` and `Visual Direction`.

Ask for one confirmation of the business and visual direction together, anchored to the visible
direction and visual packets. If the operator explicitly delegates the choice, record which option
the Agent selected and continue only after the evidence packets exist. Do not split the onsite window
into separate product, requirements, and design approval ceremonies.

In Build Card mode, replace the direction packet with the fixed Build Card summary and upstream gate
reference. Present the visual routes, mock/deferred boundary, and unresolved project route, then ask
only for visual and route confirmation. The card assignment already confirms the product; do not show
challengers or ask the customer to select the written proposition again.

After confirmation, implement exactly one selected or upstream-fixed product direction and one
selected visual route. In discovery mode, keep unselected product directions and visual routes as
decision evidence and deferred scope. In Build Card mode, keep other portfolio cards outside this
task. Never scaffold, partially build, or average alternatives into the implementation.

## Visual QA

After implementation, compare the exact running input and result states with the confirmed visual
evidence, not only with Agent-authored prose. Show the actual screenshots beside the target
composition or reference and record each promised non-token consequence as `visible`, `drifted`, or
`not proven`, including where it appears. Repeat the reskin counterfactual against the running UI.

Fix drift that makes the confirmed direction misleading, generic, broken, or materially weaker.
Then ask the operator to accept the actual visual result. Until that acceptance exists, report
`Visual Design: awaiting acceptance`; the implementing Agent must not self-upgrade it to `pass`.
An explicit visual-evidence waiver remains `waived`. Keep optional polish in deferred scope and obey
the Sales Demo Done stop rule.

Refero is a research source, not proof that the resulting product is original or production-ready.
The upstream methodology is documented at
<https://github.com/referodesign/refero_skill/tree/master/skills/refero-design>.
