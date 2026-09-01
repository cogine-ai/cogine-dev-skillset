# Input And Evidence Contract

Use the fullest available source material. This skill forms product hypotheses from a customer
conversation; it must not improve a lossy summary until it looks like original evidence.

## Accepted Inputs

Minimum inputs for a `READY` pre-demo document:

- full meeting text through the context-freeze point;
- onsite operator focus in the operator's own words;
- accumulated customer context, or an explicit statement that no prior context exists.

Use when available:

- customer background: company, decision-maker, users, buyer, workflow, existing systems, previous
  meetings, and commercial stage;
- customer-provided screenshots, forms, tables, documents, media, or sample data;
- team capability boundaries and explicitly unsupported work;
- remaining preparation time, desired prototype count, and expected demonstration time;
- later transcript segments as dated additions to the frozen context.

The operator may provide paths, pasted text, or accessible connected sources. Read the source
directly. Do not route it through another AI summarizer before product reasoning. A live transcript
is complete for this purpose when it includes the full conversation through the recorded freeze
point; later speech belongs to an addendum.

If only notes or a summary exist, they may support a provisional document when they contain enough
product evidence, but the evidence gate and overall verdict remain `NOT READY`. Mark the source
`summary-only` or `notes-only`; never call it a full transcript.

For post-demo learning mode, also require the original product document and the fullest available
conversation or operator notes from the prototype presentation. Mark notes-only feedback accurately;
do not reconstruct the boss's exact words.

## Authority Order

When sources conflict, use this order:

1. explicit operator instructions and declared team constraints;
2. direct customer statements and customer-supplied artifacts;
3. established customer context from prior work;
4. operator interpretation;
5. product hypotheses derived by this skill;
6. generic industry patterns.

Operator emphasis selects attention; it does not rewrite what the customer said. Preserve material
conflicts in the document instead of silently choosing the more convenient version.

## Evidence Labels

Label every material claim with one of these types:

- `Fact`: directly stated by the customer or demonstrated by supplied material.
- `Operator interpretation`: the onsite team's reading or priority.
- `Product hypothesis`: a product inference that still needs validation.
- `Unknown`: information not established by the evidence.

Add a compact source pointer when possible, such as speaker and timestamp, source filename and
section, or artifact name. Quote only the shortest fragment needed and redact unnecessary personal or
commercial details.

## Context Freeze

Record:

- freeze ID or timestamp;
- source files or conversation range used;
- operator focus used;
- customer context used;
- explicit no-prior-context statement when applicable;
- artifacts inspected;
- missing sources and known contradictions;
- desired prototype count and time boundary, when supplied.

Once frozen, later conversation becomes an addendum. Do not replace the original source list or
retroactively present new information as if it drove the first product portfolio.

## Missing Information

Proceed with labeled assumptions unless the missing information would materially change at least one
of these:

- target user or buyer;
- business moment or desired result;
- whether two propositions are genuinely distinct;
- whether the core demo moment is truthful;
- team capability or confidentiality boundary.

When blocked, ask one compact question about the decision-changing unknown. Do not ask the operator
to produce a PRD, feature list, screen map, architecture, or formal requirements.

## Privacy Boundary

- Keep raw transcripts and customer artifacts in their authorized location.
- Do not paste private customer text, names, files, or internal URLs into external search, design,
  analytics, or model services.
- If public research is materially needed and authorized, search only sanitized public concepts.
- Use synthetic or anonymized examples in the final product document unless exact customer data is
  explicitly required and authorized.
- Do not place meeting material, customer assets, or generated customer documents inside this Skill
  repository.
