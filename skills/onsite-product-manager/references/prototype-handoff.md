# Prototype Handoff Contract

Create one independent Build Card for every proposition in the prototype portfolio. The card defines
the product experiment. It does not prescribe implementation architecture or visual design.

## Build Card

```markdown
### Build Card - <Prototype ID And Name>

- Portfolio role and evidence: <Anchor / Contrast / Stretch>; <evidence IDs>
- Product proposition: <actor + business moment + mechanism + observable result + value>
- Form and usage surface: <where and how the user encounters it>
- Why it is distinct: <nearest proposition and material mechanism/result difference>
- Demo setup: <minimum synthetic data and entry state>
- Core demo loop: <action -> mechanism -> processing/decision -> result -> reset>
- Must be real: <clickable causal behavior and state change>
- Mock boundary: <Synthetic data>; <Simulated intelligence>; <Not claimed>
- Audience result: <what the boss must recognize>
- Customer language and product feeling: <terms>; <trust/control/urgency/etc.>
- Validation: <one question>; positive <signal>; negative <signal>
- Acceptance and non-goals: <short path>; <explicit cuts>
- Time budget and talk track: <budget>; <one sentence>
```

## Handoff Rules

- One Build Card maps to one downstream prototype task. Treat its product proposition as fixed for
  that task; the downstream workflow may report a product contradiction, but it must not reopen
  divergent product ideation or replace the proposition with a preferred alternative.
- A Build Card stands alone. A clean downstream task should understand the intended product experience
  without reading private transcripts or inventing product requirements.
- Keep each Build Card to 15 lines or fewer. Combine related fields as shown above; do not trade
  standalone clarity for repeated narrative.
- Preserve only the minimum anonymized context and customer language needed to make the prototype
  recognizable.
- State initial, processing or decision, result, and reset states. Do not substitute a screen list for
  the causal loop.
- Make the core product mechanism and business result explicit. The downstream builder may simplify
  surrounding features but must not replace that mechanism with a static page.
- Describe the desired product feeling only in business terms such as trustworthy, controllable,
  urgent, premium, or operationally dense. Do not name a component library, palette, layout system,
  Refero reference, or UI style here.
- Do not prescribe database, ORM, backend, framework, model, provider, or deployment choices.
- Do not require the customer to approve the written card before it can be prototyped. The portfolio
  is an internal product recommendation; all cards move downstream as one comparison batch by
  default. Any operator reduction below three follows the explicit waiver in the product document.

The downstream prototype workflow owns:

- visual-direction research and confirmation;
- Project Template resolution and repository rules;
- technical implementation and scope cuts;
- browser interaction, screenshot proof, privacy checks, and publishing boundaries.

If the downstream workflow cannot preserve the product mechanism within the time budget, it should
return that conflict instead of silently building a different product.

## After-Demo Feedback

The onsite operator owns capturing the demonstration conversation. Re-invoke
`onsite-product-manager` in post-demo learning mode with that evidence and the original product
document; that invocation owns appending the following record after each shown prototype:

```markdown
### Feedback - <Prototype ID>

Boss's exact words and observable actions:
Answer to the key validation question:
Recognized business value:
Objections or risks:
Requested changes:
Offered real data or access:
Pilot, price, timing, or next-meeting signal:
Verdict: Validated / Reframed / Rejected / Unresolved
Next product experiment or commercial action:
Owner and date:
```

The final conclusion is which product propositions gained or lost evidence and what should happen
next. It is not a vote for the prettiest interface.
