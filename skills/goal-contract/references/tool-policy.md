# Tool Policy Reference

Every tool call must answer a specific question.

Before using a tool, the main agent should be able to state:

```text
Question:
- What do I need to know?

Tool:
- Which tool answers it with the least side effect?

Expected Evidence:
- What output proves the answer?

Stop Rule:
- When do I stop retrying this path?
```

Do not call tools just to explore more once the question is already answered.

## Browser Verification

For frontend or public-page work, prefer the Codex in-app Browser when available.

Use browser verification for:

- Page renders.
- Route is reachable.
- No obvious runtime error overlay.
- Key copy, heading, or CTA exists.
- Critical interaction works.
- No horizontal overflow.
- Responsive layout if relevant.
- Visual polish when user feedback is visual.

Default browser smoke checklist:

```text
1. Open the exact local URL.
2. Wait for the page to render.
3. Check the expected H1 / primary content.
4. Check there is no framework error overlay.
5. Check console errors.
6. Check document width does not exceed viewport width.
7. Test only the interactions in scope.
8. Capture a screenshot only when visual layout is part of acceptance.
```

For local app testing:

- Use the project's documented dev command and expected port.
- If a dev server is already running, reuse it.
- If code changed and the browser is already on the page, reload once before verifying.
- Prefer one exact URL over guessing many route variants.
- Keep the browser hidden unless the user asked to watch or inspect it.

For interaction checks:

- Prefer user-visible interactions: click the actual button, type in the actual input.
- Do not mutate localStorage/sessionStorage/cookies directly unless that behavior is the thing being tested.
- If persistence must be checked, prefer: interact through UI, reload, verify visible state.

For console/runtime issues:

- Treat error overlays and uncaught console errors as blockers.
- Treat warnings as non-blocking unless they affect the requested behavior.
- Report warnings separately if they indicate future cleanup.

Browser failure stop rule:

```text
1st failure:
- Retry with the simplest equivalent check.

2nd failure:
- Classify it:
  - app failure
  - dev-server failure
  - browser/tooling failure
  - environment/auth/network failure

After classification:
- Fix app/dev-server issues if in scope.
- Stop debugging browser/tooling failures unless the user explicitly asks.
- Report what was verified and what could not be verified.
```

Do not spend the goal budget debugging the browser automation layer unless browser automation itself is the task.

## Command-Line Verification

For lint, test, build, typecheck, or git diff checks:

- Run the narrowest command that verifies the changed surface first.
- Broaden only when the change touches shared behavior or release risk.
- Never claim a command passed unless it actually ran.
- If a command fails, identify whether it is caused by the current diff before fixing.
- Do not fix unrelated failures unless the user asks or they block verification.

Recommended pattern:

```text
Question:
- Does the changed package still lint?

Tool:
- pnpm --filter <package> lint

Evidence:
- command exit code 0 and clean output

Stop Rule:
- If unrelated repo-wide lint fails, rerun the package-specific check and report the unrelated failure separately.
```
