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
4. When the template came from the maintained registry, verify that the resolved canonical source,
   revision, and manifest ID/version match the selected entry. If they do not match, do not silently
   substitute another source or revision; keep the route unresolved and report the mismatch.
5. Confirm that the template can support the frozen demo loop within the time box. A known template is
   not automatically compatible with every prototype form.

The template's own manifest and repository instructions are authoritative. The maintained registry
is a discovery and compatibility index, not a copy of the template contract. This skill must not
hardcode a template's framework, directory layout, or commands outside the registry entry's narrow
routing purpose.

## Instantiate the Target

- Do not instantiate a new target project until the assigned Build Card and matching Design Card are
  development-ready and the project route is resolved.
- Immediately before cloning, copying, or running a template creation command, verify that the
  external development freeze is `confirmed`, cites the operator's assignment, and links valid
  product and design freezes. An Agent-authored status or move to Code is not sufficient evidence.
- Use the template's declared creation command or procedure when one exists.
- If no procedure is declared, resolve the Git source and fixed revision from either the maintained
  registry or the operator, and resolve the new destination through separate explicit authorization.
  Once all three values are resolved, create a non-destructive clone at that revision. Leave any
  template checkout unchanged, verify the new target path and revision, then remove the template
  repository's `origin` remote from the new target before development. Do not push, create a
  replacement remote, or alter the template source automatically.
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
- Treat the Design Card and its references as implementation constraints, not permission to copy
  another product, modify the Project Template foundation, install a new design system, or add
  dependencies. Translate the confirmed route through the target project's existing editable
  components and tokens.
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
