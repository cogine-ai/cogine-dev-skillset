# Local Ultra Review

**Bring Claude Code's `/ultrareview` quality bar to your local agent workflow.**

Local Ultra Review is a portable agent skill for deep, high-precision code review. It recreates the core mechanics of Claude Code's cloud `/ultrareview` flow using local primitives: git worktrees, focused reviewer lenses, independent verification, dedupe, and severity-ranked findings.

It is built for one thing: **report real bugs before merge, not style opinions.**

> This project is not affiliated with Anthropic. It is a local, open skill inspired by the public Claude Code `/ultrareview` and Code Review documentation.

## Install

```bash
npx skills add https://github.com/cogine-ai/local-ultra-review --skill local-ultra-review
```

Then invoke it from a skill-aware agent:

```text
/local-ultra-review
```

## Why This Exists

Normal AI code review often fails in predictable ways:

- it reports style advice instead of bugs
- it guesses instead of verifying
- it reviews the diff without enough surrounding context
- it repeats the same finding in different words
- it treats "missing tests" as the main issue

Claude Code's `/ultrareview` raises the bar with isolated review environments, multiple reviewer agents, independent verification, dedupe, and severity ranking.

Local Ultra Review brings that pattern to local workflows without depending on Anthropic's remote VM or Claude Code's built-in slash command.

## Default Command

```text
/local-ultra-review
```

Default behavior:

- reviews the current branch against the detected default base branch
- includes staged and unstaged tracked changes
- excludes untracked files by default
- uses `deep` mode
- creates a local git worktree when possible
- writes artifacts under `.local-ultra-review/<session-id>/`
- removes the temporary worktree after a successful report unless `--keep-worktree` is used
- adds `.local-ultra-review/` to `.git/info/exclude`, not the tracked project `.gitignore`
- avoids copying secrets or `.env` files
- avoids network access by default
- reports only verified Important/Nit findings in the main report

## Command Examples

```text
/local-ultra-review
/local-ultra-review origin/main
/local-ultra-review HEAD~3..HEAD
/local-ultra-review pr 123
/local-ultra-review https://github.com/org/repo/pull/123
/local-ultra-review --base origin/main --mode light
/local-ultra-review --base origin/main --mode deep
/local-ultra-review --base origin/main --mode max
/local-ultra-review pr 123 --post summary
/local-ultra-review pr 123 --post review
/local-ultra-review pr 123 --keep-worktree
```

## Modes

| Mode | Use when | Reviewer coverage |
| --- | --- | --- |
| `light` | You want a faster pre-merge bug pass | correctness, security/integration, tests/verification |
| `deep` | Default. You want high confidence before merge | correctness, security/privacy, integration, state/concurrency/migration, tests |
| `max` | Large or high-risk changes | same core reviewers, with room for domain-specific expansion |

## GitHub PR Review

GitHub PR targets are first-class review inputs:

```text
/local-ultra-review pr 123
/local-ultra-review https://github.com/org/repo/pull/123
/local-ultra-review pr 123 --repo org/repo
```

Default PR behavior:

- uses `deep` mode
- collects PR metadata with `gh pr view`
- checks out the PR head into an isolated local worktree
- reviews the PR diff through the normal Local Ultra Review pipeline
- writes a full local report and `findings.json`
- removes the temporary worktree after a successful run unless `--keep-worktree` is used
- renders a GitHub-ready top-level summary comment
- does **not** post to GitHub for PR numbers or non-current-repo PR URLs unless explicitly requested
- automatically posts one GitHub PR review event when the user provides a full PR URL for the current checkout's `origin` repository

To opt out of posting for a current-repo PR URL:

```text
/local-ultra-review https://github.com/org/repo/pull/123 --post none
```

To post the legacy summary comment:

```text
/local-ultra-review pr 123 --post summary
```

To post a GitHub PR review explicitly:

```text
/local-ultra-review pr 123 --post review
```

`--post review` creates one GitHub review event. It leaves CodeRabbit-style inline comments for verified Important/Nit findings that map cleanly to right-side lines in the PR diff. If a verified finding cannot be placed on a GitHub diff-commentable line, Local Ultra Review lists it in the review body instead of forcing a bad inline comment.

The generated PR comment follows this shape:

```markdown
## Automated Local Ultra Review

**Commit:** `9d6dfb537194`
**Mode:** `deep`

| Review Score | Findings | Severity Breakdown |
|---:|---:|---|
| **100/100** (Pass) | **0** | P0: 0 / P1: 0 / P2: 0 / P3: 0 |

> [!IMPORTANT]
> This is an automated Local Ultra Review. Treat findings as review candidates for human verification.

### Review Findings

I did not identify any verified, discrete, actionable bugs introduced by this PR.

<!-- pr-review-agent provider=local-ultra-review head=<sha> session=<id> -->
```

## Design Mapping

| Claude Code `/ultrareview` mechanic | Local Ultra Review equivalent |
| --- | --- |
| Remote sandbox | Local `git worktree` review workspace |
| Fleet of reviewer agents | Reviewer lens prompts or independent model/CLI calls |
| Full codebase context | Diff bundle with changed files, nearby code, tests, project instructions, and package metadata |
| Independent finding verification | Dedicated verifier pass with evidence and base/head checks |
| Dedupe and severity ranking | Local scripts merge findings and sort by impact |
| Background task | Optional local runner that writes artifacts and report files |

## Review Pipeline

1. **Preflight** checks git status, target, tools, test commands, and project instructions.
2. **Target detection** resolves branch, range, PR, base, and mode.
3. **Worktree isolation** creates a temporary review workspace and applies local tracked patches.
4. **Context collection** builds a reproducible review bundle instead of loading the whole repo.
5. **Impact mapping** identifies changed modules, public contracts, consumers, and risk areas.
6. **Reviewer lenses** inspect correctness, security, integration, state/concurrency/migration, and tests.
7. **Verification** filters candidates into confirmed, false positive, pre-existing, or needs manual review.
8. **Dedupe/ranking** merges duplicate root causes and ranks Important findings before Nits.
9. **Report rendering** writes Markdown and JSON artifacts.

## What Counts as a Finding

A finding must include:

- exact `file:line`
- concrete failure scenario
- evidence from code or contract paths
- why the current diff introduced or worsened it
- verification plan or verifier confirmation

The main report excludes:

- style preferences
- generic maintainability advice
- speculative risks
- unverified concerns
- missing tests with no concrete behavior risk
- generated files, lockfiles, vendored code, and CI-enforced lint noise

## Severity Model

| Severity | Meaning |
| --- | --- |
| `Important` | Should be fixed before merge: production bug, security/privacy issue, data loss, broken contract, migration risk, serious regression |
| `Nit` | Minor concrete issue worth fixing, but not a merge blocker |
| `Pre-existing` | Real issue that existed before this diff |
| `NeedsManualReview` | Plausible concern that did not meet the verification bar |

## What's Inside

```text
local-ultra-review/
├── SKILL.md
├── config/
├── prompts/
├── schemas/
├── scripts/
├── templates/
├── examples/
└── output/
```

Key files:

- `SKILL.md`: agent entrypoint and non-negotiable workflow rules
- `prompts/00-review-contract.md`: shared finding bar for every reviewer
- `prompts/02-*.md` through `06-*.md`: focused reviewer lenses
- `prompts/07-verifier.md`: independent verification contract
- `schemas/*.schema.json`: structured bundle and finding formats
- `scripts/collect-context.py`: builds the review bundle
- `scripts/collect-pr-context.py`: records GitHub PR metadata
- `scripts/prepare-pr-worktree.sh`: checks out PR heads into isolated worktrees
- `scripts/run-reviewers.py`: generates reviewer packets or runs CLI backends
- `scripts/verify-findings.py`: applies programmatic finding gates
- `scripts/dedupe-rank.py`: merges duplicate findings and ranks severity
- `scripts/render-report.py`: writes the final report
- `scripts/render-github-summary.py`: writes a GitHub-ready PR summary comment
- `scripts/post-github-summary.py`: optionally posts that summary via `gh pr comment`
- `scripts/post-github-review.py`: optionally posts a GitHub PR review with inline comments via `gh api`
- `scripts/ensure-local-ignore.sh`: adds the output directory to `.git/info/exclude`
- `scripts/finalize-session.sh`: removes or preserves the temporary worktree after report generation

## Optional Script Usage

Most users should invoke the skill from an agent. The scripts are included so agents can run deterministic steps instead of rewriting glue code.

```bash
bash scripts/preflight.sh --base origin/main
bash scripts/detect-target.sh --base origin/main --mode deep
bash scripts/prepare-worktree.sh --base origin/main
python3 scripts/collect-context.py --base origin/main --out .local-ultra-review/session/review-bundle.json
bash scripts/run-checks.sh --dry-run --out .local-ultra-review/session/checks
python3 scripts/run-reviewers.py --bundle .local-ultra-review/session/review-bundle.json --mode deep --backend sequential --out .local-ultra-review/session/reviewers
python3 scripts/verify-findings.py --bundle .local-ultra-review/session/review-bundle.json --candidates .local-ultra-review/session/candidates --out-jsonl .local-ultra-review/session/verification.jsonl --out-json .local-ultra-review/session/verification.json
python3 scripts/dedupe-rank.py --verification .local-ultra-review/session/verification.jsonl --out .local-ultra-review/session/findings.json
python3 scripts/render-report.py --bundle .local-ultra-review/session/review-bundle.json --findings .local-ultra-review/session/findings.json --out .local-ultra-review/session/report.md
python3 scripts/render-github-summary.py --pr-context .local-ultra-review/session/pr-context.json --findings .local-ultra-review/session/findings.json --report .local-ultra-review/session/report.md --out .local-ultra-review/session/github-pr-comment.md
python3 scripts/post-github-review.py --pr-context .local-ultra-review/session/pr-context.json --findings .local-ultra-review/session/findings.json --mode deep --session-id session --out .local-ultra-review/session/github-pr-review-payload.json
bash scripts/finalize-session.sh --session-dir .local-ultra-review/session --status success
```

`run-reviewers.py` supports three backend shapes:

| Backend | Status | Purpose |
| --- | --- | --- |
| `sequential` | available now | generates independent reviewer prompt packets for agent/manual execution |
| `cli` | available now | runs reviewer prompts through a configured CLI command |
| `subagent` | packet mode now | prepares isolated reviewer packets for host tools that support subagents |

## Output

Expected session artifacts:

```text
.local-ultra-review/<session-id>/
├── report.md
├── findings.json
├── candidates.jsonl
├── verification.jsonl
├── review-bundle.json
├── pr-context.json
├── github-pr-comment.md
├── github-pr-review-payload.json
├── logs/
└── worktree-path.txt
```

The temporary worktree is normally removed after a successful run. `worktree-path.txt` remains as provenance for the review workspace that was used. Failed or interrupted runs preserve the worktree for debugging; remove it later with `scripts/cleanup.sh` or `scripts/finalize-session.sh`.

The final agent response should stay short:

- Important count
- Nit count
- Pre-existing count
- report path
- top 3 findings, if any

## Project-Level Review Rules

Add a `REVIEW.md` file to a repository to tune the review bar:

```markdown
# Review Instructions

## Important findings

- Auth or permission bypass
- Tenant isolation bug
- PII in logs
- Backward-incompatible API change
- Data migration that cannot be rolled back
- Incorrect billing, quota, or payment behavior
- Broken async retry or idempotency behavior

## Do not report

- Formatting
- Naming preferences
- Generated files
- Lockfiles
- Issues already enforced by CI
```

`REVIEW.md` is treated as review-specific guidance and should be more important than generic project docs for severity and skip rules.

## Philosophy

Local Ultra Review is intentionally conservative:

**Fewer findings. Better findings.**

It is better to return two verified bugs than twenty plausible comments. The verifier is the product.

## References

- [Claude Code: Find bugs with ultrareview](https://code.claude.com/docs/en/ultrareview)
- [Claude Code: Code Review](https://code.claude.com/docs/en/code-review)
- [Claude Code: Skills](https://code.claude.com/docs/en/skills)
- [Claude Code: Worktrees](https://code.claude.com/docs/en/worktrees)
