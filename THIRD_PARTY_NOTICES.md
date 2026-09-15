# Third-Party Notices

This repository contains a mix of Cogine-authored material and third-party skill content.

## Repository-Level License

Unless otherwise noted, original material in this repository is licensed under Apache License 2.0. See [LICENSE](./LICENSE).

## Third-Party Material

- `skills/check-compiler-errors/`, `skills/deslop/`, `skills/fix-ci/`, `skills/fix-merge-conflicts/`, `skills/get-pr-comments/`, `skills/loop-on-ci/`, `skills/new-branch-and-pr/`, `skills/review-and-ship/`, and `skills/run-smoke-tests/`
  Source: `cursor/plugins`, `cursor-team-kit`, commit `c1c0a32802223f4be824112dd83d33ad29a8b26c`
  Upstream copyright: Copyright (c) 2026 Cursor
  License: [MIT](./licenses/cursor-team-kit-MIT.txt)

- `skills/planmode-ceo/`, `skills/planmode-engineer/`, `skills/get-cookies/`, `skills/site-design-audit/`, and `skills/site-design-fix/`
  Source: GStack-derived adaptations of `plan-ceo-review`, `plan-eng-review`, `setup-browser-cookies`, and historical `qa-design-review`.
  Upstream copyright: Copyright (c) 2026 Garry Tan
  License: [MIT](./licenses/gstack-MIT.txt)
  Note: Preserve Cogine's host integration and the separate audit-only and audit-and-fix workflows. See [provenance](./docs/upstream-followup-2026-09-16.md).

- `skills/vercel-react-best-practices/`
  Source: `vercel-labs/agent-skills`
  Upstream repository license: MIT
  Note: Retain upstream attribution and review any additional generated or support files before publishing updates.

- `skills/supabase-postgres-best-practices/`
  Source: Supabase-authored Postgres best-practices skill
  Upstream repository license: MIT
  Note: Retain upstream attribution and review bundled reference files before publishing updates.

- `skills/security-best-practices/`
  Contains its own [LICENSE.txt](./skills/security-best-practices/LICENSE.txt)
  Note: This directory ships bundled reference material and should keep its in-directory license and notices intact.

- `skills/founder-office-hours/`, `skills/backlog-ready-spec/`, `skills/ai-app-security-audit/`, `skills/qa-only/`, `skills/devex-review/`, and `skills/plan-devex-review/`
  Source of inspiration: `garrytan/gstack`
  Upstream repository license: MIT
  Upstream copyright: Copyright (c) 2026 Garry Tan
  Note: These are Cogine-authored adaptations informed by GStack workflows such as `office-hours`, `spec`, `cso`, `qa-only`, `devex-review`, and `plan-devex-review`; keep this attribution if the adapted skills remain in the public collection.

## Before Publishing Changes

- Confirm provenance for copied skills that were adapted from local installs.
- Keep any per-skill license files and attribution notices when redistributing third-party material.
- If you add more third-party skills later, document them here.
