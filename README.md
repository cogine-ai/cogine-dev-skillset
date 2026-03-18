# Cogine Dev Skillset

Curated development skills for the Cogine team.

This repository is organized as a multi-skill collection for tools in the `skills.sh` ecosystem.

Repository: `https://github.com/cogine-ai/cogine-dev-skillset`

License: Apache-2.0 for original Cogine-authored material, with third-party notices tracked in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

## Install

Recommended for the team: install the whole collection.

```bash
npx skills add https://github.com/cogine-ai/cogine-dev-skillset
```

Install a single skill when you only want a narrow workflow:

```bash
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill gh-issue-priority-handoff
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill check-compiler-errors
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill fix-ci
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill security-best-practices
npx skills add https://github.com/cogine-ai/cogine-dev-skillset --skill vercel-react-best-practices
```

The `skills` CLI supports installing a whole repository collection with `npx skills add owner/repo` or `npx skills add <github-url>`. See the official [CLI docs](https://skills.sh/docs/cli), [FAQ](https://skills.sh/docs/faq), and a concrete collection example in [Trigger.dev's docs](https://trigger.dev/docs/skills).

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

## Included Skills

Recommended order for day-to-day engineering work:

| Skill | Purpose | Status |
|---|---|---|
| `gh-issue-priority-handoff` | Prioritize issues and generate delegation briefs | included |
| `get-pr-comments` | Fetch and summarize PR feedback | included |
| `planmode-engineer` | Engineering plan review | included |
| `planmode-ceo` | Founder/CEO-style plan review when product direction matters | included |
| `new-branch-and-pr` | Standard branch and PR workflow | included |
| `check-compiler-errors` | Compile and type-check validation loop | included |
| `deslop` | Clean up AI-generated code slop | included |
| `vercel-react-best-practices` | React and Next.js performance guidance | included |
| `get-cookies` | Import browser cookies for authenticated QA | included |
| `site-design-audit` | Report-only live site design audit | included |
| `site-design-fix` | Design audit and targeted fix loop | included |
| `run-smoke-tests` | Playwright-based smoke verification | included |
| `security-best-practices` | Security review guidance with framework references | included |
| `fix-ci` | Diagnose and fix failing CI jobs | included |
| `fix-merge-conflicts` | Resolve merge conflicts safely | included |
| `loop-on-ci` | Watch CI and iterate to green | included |
| `review-and-ship` | Review, fix, and ship via PR | included |
| `clawpacker` | Package, export, import, and restore portable OpenClaw agents | included |

## Notes

- Local private aliases may use underscores on your machine; the public repo normalizes names to `kebab-case`.
- Some skills in the local machine are marketing, SEO, or personal workflow skills. They are intentionally excluded from this repo.
- Provenance and licensing notes are tracked in [docs/provenance.md](./docs/provenance.md).
