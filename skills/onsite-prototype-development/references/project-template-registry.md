# Project Template Registry

Use this maintained registry when the operator has not supplied an existing target project or a
specific Project Template. It lets a clean session discover approved foundations without relying on
conversation history, shared memory, or a user-specific filesystem path.

The registry selects a source; it does not replace the template's own manifest, repository
instructions, setup guide, or validation commands. Verify the registered source, fixed revision,
and expected manifest identity before development. After that identity check passes, treat the
template files as authoritative for implementation details. A source, revision, or identity
mismatch leaves the route unresolved rather than authorizing a silent substitution.

## Selection Rules

1. An explicitly identified existing target project still takes precedence.
2. For a new project, choose the narrowest registered template whose fit and exclusions support the
   proposed core loop.
3. Do not ask the operator which template to use when one registry entry clearly fits.
4. Template selection does not authorize a destination. Use an explicitly authorized new-project
   output root when one is available; otherwise ask only for the destination in the mode-specific
   pre-development check. Build Card mode does not reopen product confirmation.
5. Never write a personal absolute checkout path into the frozen brief as the canonical source.
   Local checkouts are optional caches and must be verified against the canonical repository and
   fixed revision before use.
6. If no entry fits, ask for a compatible template or existing target project. Do not force a known
   template onto an unsupported product form.

## Registered Templates

### `web-app`

- **Canonical repository:** `https://github.com/cogine-ai/web-app-pt.git`
- **Fixed revision:** `470c2455b17e7c9ba574148005e6a60d716ac410`
- **Registry metadata:** template ID `web-app`, version `0.1.0`, last verified `2026-09-01`
- **Best fit:** browser-delivered interactive prototypes such as focused workbenches, guided
  workflows, CRUD-style tools, SaaS surfaces, dashboards, agent workspaces, knowledge-retrieval
  experiences, and generated business artifacts.
- **Available foundation at the fixed revision:** React/Vite UI, Tailwind with Base UI primitives,
  a small Hono API example, optional Prisma/PostgreSQL example, behavior tests, validation, and
  privacy checks. These are compatibility hints only; read `pt.manifest.json` for the actual
  contract.
- **Do not select by default for:** browser extensions, native desktop or mobile applications,
  games, immersive 3D experiences, or a prototype whose core proof depends on a runtime the
  template does not declare.

When `web-app` fits, name it in the proposed project route with the canonical repository, fixed
revision, proposed destination, and the statement that the source template remains unchanged. If
the source is not already available, use read-only remote evidence or a separately authorized
temporary inspection checkout outside the target. Keep the context freeze `proposed` until the fixed
revision's manifest, repository instructions, and relevant implementation have been inspected and
the proposed loop is known to fit. If the source cannot be verified, leave the route unresolved and
ask for the smallest access or routing correction needed; do not confirm first and inspect later.
