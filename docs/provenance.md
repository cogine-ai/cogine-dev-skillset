# Provenance And Licensing Notes

This repository is intended for public publication, so skill provenance matters.

## Current V1 Assumption

- `planmode-ceo`, `planmode-engineer`, `get-cookies`, `site-design-audit`, `site-design-fix`, `check-compiler-errors`, `deslop`, `fix-ci`, `fix-merge-conflicts`, `get-pr-comments`, `gh-issue-priority-handoff`, `investigate`, `loop-on-ci`, `new-branch-and-pr`, `peer-review`, `review-and-ship`, `run-smoke-tests`, and `slow-is-fast` are copied from local development skills and should be reviewed for original source and redistribution expectations before publication.
- `clawpacker` is intentionally a thin entrypoint skill that delegates to the canonical `cogine-ai/clawpack` repository for current command instructions.
- `npm-release-pipeline` is a locally authored generic npm-release workflow skill and should be reviewed as Cogine-authored material before publication.
- `xianyu-api-client-skill`, `xianyu-product-manager-skill`, and `xianyu-automation-skill` appear to be Cogine-authored Xianyu-specific workflow skills and should be reviewed as original internal material before public publication.
- `security-best-practices` ships with reference material and a bundled license file, so it needs a dedicated provenance review before publication.
- `vercel-react-best-practices` is derived from a public Vercel-authored skill and should retain attribution and compatible licensing treatment before publication.
- `supabase-postgres-best-practices` is derived from a public Supabase-authored skill and should retain attribution and compatible licensing treatment before publication.

## Before Publishing

Confirm for every included skill:

1. Original source
2. Whether the local version is substantially rewritten or copied
3. Whether the upstream source is public
4. Whether redistribution is permitted
5. Whether attribution is required in-file or at repo level

## Immediate Follow-Up

- Review the provenance of the copied engineering workflow skills and add repo-level attribution if needed.
- Keep the `clawpacker` canonical URL current and verify that the referenced raw GitHub path remains valid.
- Review `npm-release-pipeline` for any future external-source material before publication if its guidance/template sections are expanded beyond Cogine-authored content.
- Review the three Xianyu skills for any embedded platform-specific examples, SDK fragments, or copied vendor documentation before publication and add attribution if needed.
- Review `security-best-practices` provenance, bundled references, and `LICENSE.txt` handling before publication.
- Review `vercel-react-best-practices` provenance and decide whether to keep its bundled supporting files as-is or trim them to the minimum publishable set.
- Review `supabase-postgres-best-practices` provenance and decide whether to keep its bundled support files as-is or trim them to the minimum publishable set.
- Keep the repo-level Apache-2.0 license and maintain [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) as additional third-party skills are added.
- Run a real install test with `npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill <name>` before publishing.
