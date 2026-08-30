# Project Template Protocol

Use this protocol only when the target project was created from, or is intended to be created from, a
Project Template.

## Discover the Contract

Before writing:

1. Locate the template manifest, such as `pt.manifest.json`, `pt.manifest.yaml`, or the template's
   declared equivalent.
2. Read the repository's canonical agent instructions, then its template contract and setup guide.
   Common entrypoints include `AGENTS.md`, `CLAUDE.md`, `PT_CONTRACT.md`, and `README.md`; follow the
   repository's own references when names differ.
3. Record the template ID/version or source revision, declared capabilities, editable and protected
   paths, validation commands, and privacy boundaries.
4. Confirm that the template can support the frozen demo loop within the time box. A known template is
   not automatically compatible with every prototype form.

The template's own manifest and repository instructions are authoritative. This skill must not
hardcode a template's framework, directory layout, or commands.

## Instantiate the Target

- Do not instantiate a new target project until the operator has confirmed the demo bet or explicitly
  delegated that decision.
- Use the template's declared creation command or procedure when one exists.
- If no procedure is declared and the user explicitly supplied a local Git template, fixed revision,
  and new destination, create a non-destructive clone at that revision. Leave the template source
  unchanged, verify the new target path, and do not push or create a remote automatically.
- For a non-Git template without a declared procedure, use a safe independent copy only when source
  and destination are explicit. Exclude VCS metadata, dependency directories, build output, local
  environment files, secrets, and meeting context.
- If source, revision, destination, or copy semantics remain ambiguous, ask before writing.

## Work Within the Contract

- Modify only the resolved target project.
- Preserve declared protected paths unless the user explicitly authorizes a different task.
- Treat declared editable paths as expected safe touchpoints. For unclassified paths, follow the
  repository instructions; they are not automatically forbidden unless the manifest declares a
  deny-by-default policy. Keep new customer-specific code outside protected foundations.
- Replace or remove declared starter examples instead of building a parallel example layer.
- Reuse installed UI, API, persistence, testing, and build foundations before adding dependencies.
- Use the commands actually declared by the manifest for start, validation, build, privacy, and reset
  when available; do not invent missing commands.
- Keep raw meeting context, credentials, and sensitive customer data out of the project.

If the resolved path is the template source rather than a generated project and the user's intent is
not explicit, ask before modifying it. If a template defect blocks the prototype, prefer a bounded
workaround in the target project and report the defect; do not silently turn onsite development into
template maintenance.

## Non-template Projects

When the user explicitly supplies an existing project without a template manifest, use that project
and follow its own repository instructions, architecture, dependencies, and verification commands.
Do not initialize another stack alongside it.
