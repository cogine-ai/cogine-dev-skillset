# Upstream Follow-up — 2026-09-16

## Cursor Team Kit

Source: [cursor/plugins at c1c0a328](https://github.com/cursor/plugins/tree/c1c0a32802223f4be824112dd83d33ad29a8b26c/cursor-team-kit).

The nine repository entries listed in `provenance.md` match their source files byte-for-byte. This update adopts the full upstream implementations of `fix-ci`, `loop-on-ci`, and `review-and-ship`, including PR-level check inspection instead of treating GitHub Actions runs as the entire check set. `get-pr-comments` receives the upstream newline formatting. The other five entries already match.

The user's separately installed `review-and-ship` is a deliberate personal adaptation with whole-branch review, resolved base branches, selective staging, existing authorization boundaries, and final validation evidence. It is retained rather than replaced with this collection's upstream version. The other ten matching global Cursor skills, including `weekly-review` and `what-did-i-get-done`, already match upstream and need no content update.

## GStack-derived Adaptations

Historical comparison uses [GStack b65a464](https://github.com/garrytan/gstack/tree/b65a464d37e564a0623e6358d2d7a3080b386647), dated 2026-03-17 17:41:44 UTC, and this repository's initial import `02bb615`, dated 2026-03-17 18:03:40 UTC. The upstream snapshot is a comparison anchor, not a claim that it was the exact import commit.

| Local entry | Historical source | Distinctive identical lines longer than 50 characters | Retained adaptation |
| --- | --- | ---: | --- |
| `planmode-ceo` | `plan-ceo-review` | 237 | Host-neutral entry, repository context and input contract, local output paths, focused review behavior |
| `planmode-engineer` | `plan-eng-review` | 58 | Host-neutral entry, target gate, local test-plan artifact, smaller review workflow |
| `get-cookies` | `setup-browser-cookies` | 22 | Local helper discovery, real-browser/CDP detection, redacted errors and cookie handling |
| `site-design-audit` | `qa-design-review` | 156 | Separate report-only workflow, local browser setup, reports and readiness records |
| `site-design-fix` | `qa-design-review` | 207 | Separate audit/fix/verification loop, local browser setup and bounded changes |

Later local updates are traceable through PR #7 and commits `d87a825`, `84d14bc`, and `3f5c369`. The current upstream design source is `design-review`; the September snapshot comparison is pinned at `4a3c6a8a3cad82cfffdaa4d152e1c5ae5c4af659`.

These are maintained adaptations, not unmodified vendor installations. This follow-up records their provenance and preserves their current runtime. It does not claim full synchronization to current GStack or recover every historic customization decision. Future imports should compare changes within the retained workflow instead of replacing it with GStack's generated host preamble and complete runtime.

## Validation

- All nine Cursor repository entries match the pinned upstream files.
- Changed Markdown entries pass the Codex skill format validator.
- Existing PR-posting boundary checks pass in both the standalone and collection copies.
- Provenance and license references are bundled with the published collection.
