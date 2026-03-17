# Cogine Dev Skillset

Curated development skills for the Cogine team.

This repository is organized as a multi-skill collection for tools in the `skills.sh` ecosystem.

Repository: `https://github.com/cogine-ai/cogine-dev-skillset`

License: Apache-2.0 for original Cogine-authored material, with third-party notices tracked in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

## Install

Install a single skill:

```bash
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill planmode-ceo
```

Examples:

```bash
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill planmode-engineer
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill site-design-audit
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill site-design-fix
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill get-cookies
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill fix-ci
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill security-best-practices
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill vercel-react-best-practices
```

Before publishing, validate whether your target client also supports collection-level install without `--skill`.

## Repository Layout

```text
skills/
  <skill-name>/
    SKILL.md
docs/
  inventory.md
  provenance.md
```

All publishable skill names use `kebab-case`.

## Included In V1

| Skill | Purpose | Status |
|---|---|---|
| `planmode-ceo` | Founder/CEO-style plan review | included |
| `planmode-engineer` | Engineering plan review | included |
| `get-cookies` | Import browser cookies for authenticated QA | included |
| `site-design-audit` | Report-only live site design audit | included |
| `site-design-fix` | Design audit and targeted fix loop | included |
| `check-compiler-errors` | Compile and type-check validation loop | included |
| `deslop` | Clean up AI-generated code slop | included |
| `fix-ci` | Diagnose and fix failing CI jobs | included |
| `fix-merge-conflicts` | Resolve merge conflicts safely | included |
| `get-pr-comments` | Fetch and summarize PR feedback | included |
| `gh-issue-priority-handoff` | Prioritize issues and generate delegation briefs | included |
| `loop-on-ci` | Watch CI and iterate to green | included |
| `new-branch-and-pr` | Standard branch and PR workflow | included |
| `review-and-ship` | Review, fix, and ship via PR | included |
| `run-smoke-tests` | Playwright-based smoke verification | included |
| `security-best-practices` | Security review guidance with framework references | included |
| `vercel-react-best-practices` | React and Next.js performance guidance | included |

## Notes

- Local private aliases may use underscores on your machine; the public repo normalizes names to `kebab-case`.
- Some skills in the local machine are marketing, SEO, or personal workflow skills. They are intentionally excluded from this repo.
- Provenance and licensing notes are tracked in [docs/provenance.md](./docs/provenance.md).
