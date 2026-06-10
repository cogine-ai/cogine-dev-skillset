# Goal Description Reference

Use this when drafting the confirmed Goal Description before `create_goal`.

## Full Form

```text
Objective:
- What exact deliverable will exist when this goal is done?

Scope:
- What will be changed or implemented?
- Which files/apps/routes/modules are in scope?
- What product behavior is included?

Non-goals:
- What is explicitly out of scope?
- Which tempting adjacent tasks should not be done?
- Which inferred tasks from docs/designs should be ignored unless separately requested?

Acceptance:
- What user-visible behavior must be true?
- What code-level conditions must be true?

Verification:
- Which commands will be run?
- Which browser/manual checks will be performed?
- What evidence will be reported?

Tool Policy:
- Which tools are allowed or expected?
- How many retries are allowed for the same tool failure?
- What should happen if verification tooling fails but the app likely works?

Subagent Policy:
- Whether subagents may be used.
- Which local tasks they may own.
- What they are forbidden to decide or change.
- How the main agent verifies their output.

Stop Policy:
- When should the goal stop as complete?
- What adjacent work must not continue after completion?
- When should the agent stop for explicit user approval?
- When should tool retries stop?
- When should the goal be marked blocked?

Stop / Reframe Conditions:
- When must the agent stop and ask/reframe?
- Product ambiguity?
- Scope expansion?
- API/schema/legal/security uncertainty?
- Repeated tool failure?

Runtime Discipline:
- How the agent will keep this Goal Description active during execution.
```

## Synthesis Pattern

When the user confirms the contract, compress it into the goal objective:

```text
Deliver <outcome>.

Scope: <short scope list>.
Non-goals: <short non-goal list>.
Done when: <short acceptance/verification list>.
Tool policy: <retry/stop rule>.
Subagent policy: <delegation boundary>.
Stop policy: <completion/approval/block/tool-stop rule>.
Stop/reframe if: <short stop conditions>.
Runtime discipline: <when to re-check the description>.
```

Avoid vague objectives such as:

```text
Build the privacy page.
```

Prefer bounded objectives:

```text
Deliver an English-only /privacy page in apps/store using the existing Store design system.

Scope: add the route, article-style content, existing top header, and a dismissible cookie notice.
Non-goals: no zh page, no Cookie Policy page, no GA4 consent gating, no Terms/Billing pages, no final legal-counsel approval claim.
Done when: store lint, i18n lint, diff check, and browser smoke pass.
Tool policy: retry a failed browser verification once; after the second failure, classify app issue vs tooling issue and report instead of debugging the browser stack.
Subagent policy: subagents may only do bounded research/review/verification; main agent owns scope, final diff, and user communication.
Stop policy: stop as complete when acceptance and verification are satisfied; do not continue into adjacent legal pages, extra polish, broader refactors, or analytics consent work. Stop for approval before touching auth, billing, analytics behavior, schema, production config, or destructive git operations. Stop tool retries after two failures on the same validation path; mark blocked only when the same blocker repeats and no meaningful progress remains.
Stop/reframe if: legal scope expands, analytics behavior changes, or browser verification fails twice.
Runtime discipline: before edits, new files, subagents, broad tools, failed verification retries, commit, or PR, compare the action against this description.
```

## Stop Policy

Stop Policy controls when the goal should stop, not just when it should be reframed.

Include these categories when relevant:

```text
Stop as complete when:
- All Acceptance items pass and Verification evidence is collected.

Do not continue into:
- Adjacent cleanup, new pages, broad refactors, or extra polish not listed in Scope.

Stop for approval before:
- API, schema, auth, billing, analytics, legal commitment, security, production config, or destructive git changes.

Stop tool retries when:
- The same validation path fails more than the allowed retry count.

Stop as blocked when:
- The same blocker repeats across goal turns and no meaningful progress remains.
```

## Checkpoint Protocol

After each meaningful batch of work, update the active plan with:

```text
Completed:
- What changed?

Contract check:
- Still in scope: yes/no
- Non-goals touched: no/yes
- Stop condition triggered: no/yes
- Stop policy says stop now: no/yes
- Verification remaining:
```

If the answer is not clean, pause.
