# Product Direction And Visual Research

Use this workflow before the confirmation gate. The operator supplies business evidence: the fullest
meeting text, a short focus note, and customer context when available. A target project or template is
an execution input that may be supplied initially or resolved in the combined direction check. The
operator does not need to request divergent ideas, name Refero, choose a design method, or specify a
fixed number of directions.

## Frame The Product Direction

Infer the underlying business outcome, the actor who needs it, the costly or confusing moment being
changed, and the visible evidence that would make the customer recognize the value.

When the evidence supports more than one plausible product form, internally explore a small set of
materially different framings. Useful lenses may include a focused workbench, guided workflow, agent
workspace, monitoring or BI surface, knowledge retrieval, browser sidecar, or generated decision
artifact. These are prompts for reasoning, not a required menu.

Evaluate each framing against:

- fidelity to the transcript, operator focus, and established customer context;
- strength and immediacy of the customer-visible business result;
- whether the customer can operate it and observe meaningful state change;
- feasibility inside the remaining time and resolved project contract;
- honesty of the synthetic-data and mocked-system boundary;
- fit with established team capabilities or constraints, without inventing capabilities.

Recommend the strongest framing. Do not turn every discussed feature into a candidate and ask the
operator to vote. The goal is to find the smallest loop that embodies the important customer outcome,
not to choose one item from a feature list.

Surface alternatives only when they would lead to meaningfully different customer experiences or
implementation bets. There is no required option count. If one direction is clearly dominant, explain
it briefly and recommend it directly.

## Decide Whether Visual Research Is Material

Treat visual research as material for a new customer-facing surface, a sales-critical first
impression, a major change in product form, or a prototype without an approved design system. Keep it
light when the target already has a clear approved visual language or the change is a small addition
whose design direction is not in question.

Use the first suitable source:

1. Preserve explicit operator-provided brand rules, screenshots, Figma frames, or an approved project
   design system as the primary constraint.
2. If the `refero-design` skill is available, use it as the visual-research authority while keeping
   this skill's onsite time box, confirmation gate, project boundary, and stop rule authoritative.
3. Otherwise, if Refero MCP capabilities are available, use them directly. Start with Styles for
   visual direction, then use Screens for hierarchy and concrete states or Flows for multi-step
   journeys when those layers materially affect the demo.
4. If Refero is unavailable, use the approved project language and other authorized references. If
   none exists, derive one restrained visual thesis from the desired customer impression, product
   form, information hierarchy, and interaction states, then record that fallback in the visual
   lock. Do not ask the operator to install a tool merely to continue, and do not block the combined
   direction check solely because an external design-research capability is absent.

When using Refero directly, inspect distinct search angles derived from the customer, domain, desired
impression, and product form. Choose one dominant reference foundation. Give any secondary reference
a narrow role, such as navigation density, table treatment, or interaction feedback. Never copy a
single product wholesale, average references into a safe middle, reuse third-party assets without
authorization, or claim reference imagery as product evidence.

Relevant Refero MCP capability names commonly include `refero_search_styles`, `refero_get_style`,
`refero_search_screens`, `refero_get_screen`, `refero_get_similar_screens`,
`refero_get_screen_image`, `refero_search_flows`, and `refero_get_flow`. Treat availability as a
runtime fact; do not assume those tools exist because Refero was used in a previous session.

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

Use semantic roles rather than copying raw style values without understanding them. Avoid automatic
fallbacks such as one default AI palette, cards around every section, decorative gradients, or a
generic SaaS dashboard shell when the researched direction does not support them.

## One Combined Direction Check

Before target files are created or modified, present one compact confirmation containing:

1. the customer outcome and recommended product framing;
2. the core interaction loop and customer-visible result;
3. the visual target and its primary basis when visual research is material;
4. mocked systems or synthetic data;
5. intentionally deferred scope;
6. only the consequential alternatives, if any;
7. the target project or Project Template route when it remains unresolved.

Ask for one confirmation of the business and visual direction together. If the operator explicitly
delegates the decision, record the recommended direction as confirmed and continue. Do not split the
onsite window into separate product, requirements, and design approval ceremonies.

## Visual QA

After implementation, compare the exact running demo path with the visual lock. Check the primary
viewport and relevant interaction states for hierarchy, typography, spacing, color-role drift,
component character, imagery, customer language, and the distinguishing move. Fix drift that makes
the confirmed direction misleading, generic, broken, or materially weaker. Keep optional polish in
deferred scope and obey the Sales Demo Done stop rule.

Refero is a research source, not proof that the resulting product is original or production-ready.
The upstream methodology is documented at
<https://github.com/referodesign/refero_skill/tree/master/skills/refero-design>.
