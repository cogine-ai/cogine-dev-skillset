---
name: local-ultra-review
description: Use when the user explicitly asks for a deep local code review, PR review, bug hunt, pre-merge review, or Ultra Review style review with high confidence findings.
disable-model-invocation: true
arguments:
  - target
  - mode
---

# Local Ultra Review

Run a local Ultra Review style code review. The goal is to find real bugs introduced or worsened by the target diff, with low false positives.

This skill is read-only. Do not modify product code, commit, push, or apply fixes.

## Inputs

Invocation examples:

- `/local-ultra-review`
- `/local-ultra-review origin/main`
- `/local-ultra-review HEAD~3..HEAD`
- `/local-ultra-review pr 123`
- `/local-ultra-review https://github.com/org/repo/pull/123`
- `/local-ultra-review --base origin/main --mode deep`
- `/local-ultra-review pr 123 --post summary`

If no target is provided, review the current branch against the default base branch and include staged and unstaged tracked changes.

If the target is a GitHub PR, default to `deep` mode, collect PR metadata, review the PR head in an isolated worktree, and render a GitHub-ready summary comment. Do not post the comment unless the user passes `--post summary`.

Modes:

- `light`: correctness, security/integration, and tests/verification
- `deep`: default, five reviewer lenses plus verification
- `max`: broader review for large or high-risk changes

GitHub output:

- `--post none`: default; write local artifacts only
- `--post summary`: post one top-level PR summary comment after verification and report rendering

## Hard Rules

1. Review only. Do not edit business code.
2. Use an isolated worktree when possible.
3. Prefer `.local-ultra-review/worktrees/<session-id>/` for review workspaces.
4. Do not copy `.env`, credentials, private keys, tokens, gitignored secrets, or local database config unless the user explicitly allows it.
5. Do not use network access unless the user explicitly allows it or approved project checks require it.
6. Do not report style, formatting, naming preference, or generic maintainability advice as findings.
7. A finding must cite exact `file:line`.
8. A finding must include a concrete failure scenario.
9. A finding must be checked by a separate verifier pass before it appears as Important or Nit.
10. If a candidate cannot be verified, put it under `Needs manual review` or omit it.

## Supporting Files

- `config/default.yaml`: default review behavior and safety settings.
- `config/severity.yaml`: local severity definitions.
- `config/ignore.yaml`: default low-value path and rule exclusions.
- `prompts/00-review-contract.md`: shared finding bar for all reviewers.
- `prompts/01-impact-mapper.md`: impact map prompt; does not produce findings.
- `prompts/02-*.md` through `06-*.md`: reviewer lens prompts.
- `prompts/07-verifier.md`: required verification pass.
- `prompts/08-dedupe-ranker.md`: dedupe and severity ranking rules.
- `prompts/09-final-report.md`: final report instructions.
- `schemas/*.schema.json`: review bundle and finding schemas.
- `scripts/*.sh` and `scripts/*.py`: optional local automation.
- `templates/*.j2`: report and comment templates.

Load only the supporting files needed for the current phase.

## Pipeline

### Phase 0: Preflight

Run:

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/preflight.sh "$ARGUMENTS"
```

If the script is unavailable, manually inspect:

- git repo root and current branch
- default base branch
- staged, unstaged, and untracked status
- changed files
- package and test commands
- `REVIEW.md`, `AGENTS.md`, `CLAUDE.md`, `README.md`, or equivalent instructions

Stop only if the target cannot be determined or the directory is not a git repository.

### Phase 1: Detect Target

Run:

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/detect-target.sh "$ARGUMENTS"
```

If no argument is provided, use current branch versus the detected default base and include staged and unstaged tracked changes.

### Phase 2: Prepare Isolated Workspace

For branch or working-tree targets, run:

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/prepare-worktree.sh --base <base-ref>
```

For GitHub PR targets, first collect PR metadata and then prepare the PR worktree:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/collect-pr-context.py \
  --pr <pr-number-or-url> \
  --repo <owner/repo-if-known> \
  --out .local-ultra-review/<session-id>/pr-context.json

bash ${CLAUDE_SKILL_DIR}/scripts/prepare-pr-worktree.sh \
  --pr <pr-number-or-url> \
  --repo <owner/repo-if-known> \
  --base <pr-base-ref-name> \
  --session-id <session-id>
```

Expected behavior:

1. Create `.local-ultra-review/<session-id>/`.
2. Create a detached worktree under `.local-ultra-review/worktrees/<session-id>/`.
3. Apply staged and unstaged tracked changes when reviewing local working tree changes.
4. Do not copy secrets by default.
5. Record base, head, session id, worktree path, and patch paths.

If worktree creation fails, continue read-only from the current working tree and state that isolation was not available.

### Phase 3: Collect Context

Run in the review workspace if one exists:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/collect-context.py \
  --base <base-ref> \
  --out .local-ultra-review/<session-id>/review-bundle.json
```

The bundle should include diff patches, changed files, relevant test files, package scripts, project instructions, ignore rules, and detected languages/frameworks. Do not load the whole repository blindly.

### Phase 4: Impact Map

Read `prompts/01-impact-mapper.md` and produce an impact map before looking for bugs. The impact map should identify changed modules, public interfaces, consumers, data models, auth/tenant/privacy boundaries, tests, and high-risk reviewer focus areas. It must not produce final findings.

### Phase 5: Reviewer Passes

Run independent reviewer passes using the shared contract in `prompts/00-review-contract.md` and these lenses:

1. Correctness and regression
2. Security and privacy
3. Integration and API contract
4. State, concurrency, migration, and rollback
5. Tests and verification

Each reviewer must output candidate findings matching `schemas/candidate-finding.schema.json`. Prefer fewer high-confidence findings.

### Phase 6: Verification

Read `prompts/07-verifier.md` and verify every candidate. Classify each as:

- `confirmed`
- `false_positive`
- `pre_existing`
- `needs_manual_review`

Only `confirmed` findings may appear in the main Important or Nit sections.

### Phase 7: Dedupe and Rank

Read `prompts/08-dedupe-ranker.md`. Deduplicate confirmed findings by root cause and rank by severity:

1. Security, privacy, permission, data loss
2. Production behavior regression
3. Migration, rollback, data compatibility
4. Integration contract break
5. Concurrency, retry, idempotency
6. Test blind spot tied to a concrete behavior risk
7. Nit

Do not pad the report. If no confirmed findings exist, say so.

### Phase 8: Report

Write:

- `.local-ultra-review/<session-id>/report.md`
- `.local-ultra-review/<session-id>/findings.json`
- `.local-ultra-review/<session-id>/candidates.jsonl`
- `.local-ultra-review/<session-id>/verification.jsonl`
- `.local-ultra-review/<session-id>/review-bundle.json`
- `.local-ultra-review/<session-id>/logs/`

For GitHub PR targets, also write:

- `.local-ultra-review/<session-id>/pr-context.json`
- `.local-ultra-review/<session-id>/github-pr-comment.md`

Render the GitHub summary with:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/render-github-summary.py \
  --pr-context .local-ultra-review/<session-id>/pr-context.json \
  --findings .local-ultra-review/<session-id>/findings.json \
  --report .local-ultra-review/<session-id>/report.md \
  --out .local-ultra-review/<session-id>/github-pr-comment.md \
  --mode <mode> \
  --session-id <session-id>
```

If and only if the user passed `--post summary`, post exactly one top-level PR comment:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/post-github-summary.py \
  --pr-context .local-ultra-review/<session-id>/pr-context.json \
  --body-file .local-ultra-review/<session-id>/github-pr-comment.md
```

Do not create inline comments or GitHub review events in this version.

The final response to the user should include only:

1. Important count
2. Nit count
3. Pre-existing count
4. Report path
5. Top 3 findings, if any

Do not paste large logs into chat.
