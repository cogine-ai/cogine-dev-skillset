# Product-To-Design Handoff Contract

Create one independent Build Card file for every proposition in the prototype portfolio. Write it to
`build-cards/<Prototype ID>.md`. The card defines the product experiment. It does not prescribe
implementation architecture or visual design.

## Build Card

```markdown
# Build Card - <Prototype ID And Name>

- Source, role, and evidence: <context-freeze.md path; freeze ID; batch ID; card ID; upstream verdict>; <Anchor / Contrast / Stretch>; <evidence IDs>
- Upstream gates and risks: <Evidence=...; Product distinctness=...; Validation=...; Demonstrability=...; Portfolio execution=...; Mock honesty=...; Handoff=...>; <named risks or none>
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

- One Build Card maps to one downstream Design Card and, after design is ready, one prototype task.
  Treat its product proposition as fixed throughout that chain; either downstream workflow may
  report a product contradiction, but it must not reopen divergent product ideation or replace the
  proposition with a preferred alternative.
- A Build Card is product-scope-complete. Together with its linked `context-freeze.md`, it gives the
  design stage the complete product and evidence handoff without private transcripts or invented
  product requirements.
- Keep each Build Card to 18 lines or fewer. Combine related fields as shown above; do not trade
  scope clarity for repeated narrative.
- Preserve only the minimum anonymized context and customer language needed to make the prototype
  recognizable.
- State initial, processing or decision, result, and reset states. Do not substitute a screen list for
  the causal loop.
- Make the core product mechanism and business result explicit. The downstream designer and builder
  may simplify surrounding presentation or features but must not replace that mechanism with a
  static page.
- Describe the desired product feeling only in business terms such as trustworthy, controllable,
  urgent, premium, or operationally dense. Do not name a component library, palette, layout system,
  Refero reference, or UI style here.
- Do not prescribe database, ORM, backend, framework, model, provider, or deployment choices.
- Do not require the customer to approve the written card before it can be prototyped. The portfolio
  is an internal product recommendation; all cards move downstream as one comparison batch by
  default. Any operator reduction below three follows the explicit waiver in the upstream
  `context-freeze.md`.

The downstream design workflow owns:

- portfolio-level visual and interaction research;
- visible previews, design confirmation, and one Design Card per Build Card;

The later prototype-development workflow owns:

- Project Template resolution and repository rules;
- technical implementation and scope cuts;
- browser interaction, screenshot proof, privacy checks, and publishing boundaries.

If either downstream workflow cannot preserve the product mechanism within the time budget, it
should return that conflict instead of silently designing or building a different product.

## After-Demo Feedback

The onsite operator owns capturing the demonstration conversation. Re-invoke
`onsite-product-manager` in post-demo learning mode with that evidence and the original output
bundle; that invocation owns appending the following record after each shown prototype to
`context-freeze.md`:

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
