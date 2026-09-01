# Input Contract

Resolve the following inputs before development. They may be pasted text, local files, or other
sources the user has authorized Codex to read.

## Required Source Inputs

- **Raw meeting text:** the full transcript or the fullest available verbatim text. Do not replace it
  with a third-party AI summary.
- **Operator focus:** the technical operator's short description of what matters most now, including
  corrections, priority, and any idea that must be demonstrated.

If either source is absent, request it or ask the operator to explicitly authorize the available
source as the substitute. Do not fabricate missing meeting content.

These are the only product-definition inputs required from the operator. Do not require the operator
to name a product form, prepare a feature list, request alternatives, choose a visual direction, or
name a design-research tool. The Agent owns that reasoning and proposes the consequential decisions
at the confirmation gate.

Treat the operator's statement that supplied meeting text is complete or is the fullest available
source as authoritative. Do not reject or reclassify it merely because it is short, compressed, or
well organized. Ask about completeness only when the operator says the source is partial or when a
missing segment creates a material contradiction in the core demo outcome.

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
not block initial product framing or visual research. Ask only for the unresolved part of the route
in the combined direction check, and resolve the route before creating or modifying target files.

## Optional Inputs

- Established customer background context.
- Remaining onsite time or another explicit time box.
- Existing brand, terminology, screenshots, documents, sample data, or design references.
- Authorized external services or disposable resources.
- Delivery constraints such as local-only operation or a separately requested publishing target.

When no time box is supplied, assume a short onsite session and keep the first vertical slice as small
as possible; do not promise a specific elapsed time.

## Authority Order

When sources conflict, use this order:

1. The operator's latest explicit instruction or correction.
2. The operator focus note.
3. Explicitly established customer background context.
4. The raw meeting transcript.
5. Agent inference.

Expose consequential conflicts in the frozen brief. Never let an inference override an explicit
operator direction.

## Privacy Handling

- Read source material in place when possible.
- Do not copy raw meeting text or customer-sensitive context into the target repository.
- Do not include raw source material in commits, logs, screenshots, public URLs, or build output.
- Put only synthetic or explicitly approved data in the prototype.
