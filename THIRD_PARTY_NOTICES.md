# Third-Party Notices

This repository contains a mix of Cogine-authored material and third-party skill content.

## Repository-Level License

Unless otherwise noted, original material in this repository is licensed under Apache License 2.0. See [LICENSE](./LICENSE).

## Third-Party Material

- `skills/babysit-pr/`, `skills/council/`, `skills/file-pr/`, `skills/full-send/`, `skills/full-stop/`, `skills/leaving-pr-comments/`, `skills/modernize/`, `skills/sol-loop/`, and `skills/takeover/`
  Source: [Theo Browne's tstack at 11e37a7](https://github.com/t3dotgg/tstack/tree/11e37a74d0a6868c121cd0910ab2b3bd9873b92a), via the [Coding Engineer Marketplace bundle](https://github.com/cogine-ai/marketplace/tree/03fe59c5d42bba98fa747c50a7298a3b23b53f5d/plugins/coding-engineer-skills).
  Upstream copyright: Copyright (c) 2026 Theo Browne
  License: MIT. The upstream notice is included as `LICENSE` in each skill directory so it accompanies single-skill installs.

- `skills/check-compiler-errors/`, `skills/deslop/`, `skills/fix-ci/`, `skills/fix-merge-conflicts/`, `skills/get-pr-comments/`, `skills/review-and-ship/`, and `skills/run-smoke-tests/`
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
