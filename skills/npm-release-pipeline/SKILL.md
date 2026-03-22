---
name: npm-release-pipeline
description: Use when releasing a Node.js package to npm, or when asked to verify release readiness, run prepublish checks, publish a new version, create/push git tags, create a GitHub Release, or close release-related issues/epics. Best for repo-agnostic npm package release work where the package is defined by package.json and the exact release checklist must be executed safely.
---

# Npm Release Pipeline

## Overview

Use this skill to run a safe, repeatable npm release flow for a generic Node.js package.

Favor a strict order: verify release readiness first, publish second, then do Git/GitHub follow-up. Stop on failed preconditions. If a step partially succeeds, report the exact state instead of pretending the whole release is clean.

## Default workflow

1. Identify the package and release target.
2. Verify remote default branch / release branch state.
3. Verify version, changelog / release-notes inputs, npm availability, release channel, CI, and working tree safety.
4. Run local release checks.
5. Generate or confirm release notes.
6. Publish to npm with the intended dist-tag/channel.
7. Verify published version and dist-tags.
8. Create and push git tag.
9. Create GitHub Release if requested.
10. Close or comment on related release issues/epics if requested.
11. Report final state, including any partial-success cleanup needed.

## Release-readiness checklist

Check these before publishing:

- `package.json` exists and contains `name` and `version`.
- The intended release version is already committed on the branch you plan to release from.
- The working tree is clean, unless the user explicitly wants a different flow.
- The local branch matches the intended remote branch tip.
- Relevant PRs are merged.
- Relevant CI checks are green.
- The intended npm release channel is clear (`latest`, `next`, or another tag).
- Set `<channel>` to the intended npm release tag (`latest`, `next`, or another tag) and verify the target channel does not already point at the release version by checking `npm view <package-name>@<channel> version` or `npm view <package-name> dist-tags.<channel>`.
- If a changelog or release notes process exists, confirm the new version is documented or draftable from merged PRs.
- If `prepublishOnly` exists, treat it as a final guardrail, not a substitute for proactive verification.

If any of the above is unclear, ask the smallest clarifying question needed.

## Core commands

Use the package's actual scripts and metadata; do not assume every repo has the same tooling.

### Inspect package metadata

```bash
jq '{name,version,scripts,files,publishConfig}' package.json
```

### Check git state

```bash
git status --short --branch
git fetch --tags origin
git rev-parse HEAD
git rev-parse origin/<default-branch>
```

### Check npm auth, remote version, and dist-tags

```bash
npm whoami
npm view <package-name> versions --json
npm dist-tag ls <package-name>
npm view <package-name>@<channel> version
# or
npm view <package-name> dist-tags.<channel>
```

Set `<channel>` to the intended release tag such as `latest`, `next`, or a custom tag before using the channel-specific checks above.

### Run prepublish verification

Preferred baseline for npm repos:

```bash
npm run build
npm test
npm pack --dry-run
```

Also inspect package contents when `npm pack --dry-run` prints the tarball file list. Confirm the built output and only intended files are included.

### Publish

For the default stable channel:

```bash
npm publish
```

For an explicit release channel/tag:

```bash
npm publish --tag <dist-tag>
```

Use a non-`latest` tag such as `next` for prereleases, staged rollouts, or any release that should not become the default install target.

Then verify both version visibility and tag assignment:

```bash
npm view <package-name> version
npm dist-tag ls <package-name>
npm view <package-name>@<dist-tag> version
```

### Tag and push

Use semantic tags unless the repo uses another convention.

```bash
git tag -a v<version> -m "release: v<version>"
git push origin v<version>
```

### GitHub follow-up

Examples:

```bash
gh release create v<version> --repo <owner/repo> --title "v<version>" --notes-file <notes-file>
gh issue close <number> --repo <owner/repo> --comment "Released in <package-name>@<version>."
```

## Decision rules

### When to stop before publish

Stop and report instead of publishing when:

- local version does not match the intended release version
- target version is already on npm for the intended channel
- working tree is dirty in a way that changes release output
- branch is behind remote release branch
- required CI is failing or missing
- `npm run build`, `npm test`, or `npm pack --dry-run` fails
- package contents look wrong or incomplete
- npm auth is missing

### When partial success happens

Treat these as separate states and report them explicitly:

- **Publish succeeded, tag not pushed**
- **Publish succeeded, GitHub Release not created**
- **Tag pushed, issue/epic still open**
- **GitHub Release created, npm publish failed**

For each partial-success state, report:

1. what succeeded
2. what failed
3. whether users can already install the release
4. the exact next repair step

## Package-content validation

During `npm pack --dry-run`, verify at least:

- built artifacts expected by the package are present
- tests, fixtures, secrets, local scratch files, and unrelated source files are not accidentally included unless intentionally published
- README/LICENSE and other required metadata files are present when expected
- tarball name and version match `package.json`

If the repo uses `files`, `.npmignore`, or `publishConfig`, inspect them when package contents look surprising.

## Release-notes guidance

Generate release notes before creating a GitHub Release or final release announcement.

Preferred source order:

1. `CHANGELOG.md` entry for the target version
2. merged PR titles/descriptions since the previous tag
3. issue/epic summary or explicit user-supplied notes

If `CHANGELOG.md` exists, prefer its version-specific entry as the canonical notes source. If it does not exist or is incomplete, synthesize concise notes from merged PRs and call out that the notes were generated from Git history / PR metadata.

Suggested release-notes template:

```markdown
## <package-name> v<version>

### Highlights
- <most important user-visible change>
- <second important change>
- <third important change>

### Included changes
- PR #123 — <title>
- PR #124 — <title>
- <other merged change if no PR number is available>

### Notes
- Install: `npm install <package-name>@<version>`
- Channel: `<dist-tag>`
- Migration/compatibility: <none|brief note>
```

Keep the notes factual and compact. Include only user-relevant changes, migration notes, and the actual install/package name when useful.

## Dist-tags and release channels

Check release-channel intent before publishing.

Default guidance:

- use `latest` for the default stable release users should get from `npm install <package-name>`
- use `next` (or another explicit tag) for prereleases, canaries, beta lines, or staged rollouts
- do not assume a prerelease semver automatically implies the correct dist-tag; verify the repo's intended channel

Before publish, check current tags:

```bash
npm dist-tag ls <package-name>
```

After publish, verify that:

- the new version exists on npm
- the intended dist-tag points to that version
- `latest` was not moved unintentionally when publishing a non-stable release

If channel state looks wrong, stop and report the exact mismatch before doing follow-up steps such as GitHub Release creation or issue closure.

## GitHub Release guidance

Create a GitHub Release only when the user asks for it or the repo's release flow clearly requires it.

Use the finalized release notes as the source of truth for the GitHub Release body.

## Closing issues and epics

Do not assume every release should close issues automatically.

Before closing release-related issues/epics, confirm that:

- the code is merged to the intended branch
- the package is actually published
- the tag exists remotely
- any promised release artifact is complete

If closing an issue, leave a short comment stating the released package version.

## Repo-specific inputs to gather when needed

Ask only if not already obvious from repo state:

- default branch name (`main`, `master`, or another branch)
- whether a GitHub Release is required
- which issue/epic should be closed
- whether release notes should come from `CHANGELOG.md`, merged PRs, or custom text
- whether the publish tag/channel (`latest`, `next`, etc.) differs from default npm publish behavior

## Output format

Report in this order:

1. release-readiness verdict
2. evidence
3. actions taken
4. resulting published version / tag / release links
5. any remaining follow-up

Keep the report short and operational.

## Common mistakes

- Publishing before checking whether the version already exists on npm.
- Assuming the default branch is `main`.
- Relying on `prepublishOnly` alone and skipping proactive checks.
- Forgetting to inspect `npm pack --dry-run` contents.
- Claiming release completion before verifying npm actually serves the new version.
- Treating publish, tag, GitHub Release, and epic closure as one atomic step.
- Closing issues before the package is publicly available.
