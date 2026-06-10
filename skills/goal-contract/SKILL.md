---
name: goal-contract
description: Use after research and a dev plan, before creating a long-running goal. Generates a runtime-enforceable goal description with scope, non-goals, acceptance criteria, verification, tool policy, subagent policy, and stop conditions. Use when the user explicitly wants goal mode or when a moderate/complex task is about to be executed as a goal.
---

# Goal Contract

Use this skill after Research and Dev Plan, before `create_goal`.

The purpose is to turn a dev plan into a confirmed, runtime-enforceable Goal Description. The Goal Description is the long-lived contract that the agent must follow during goal execution.

Do not create a goal from the user's raw request.
Do not create a goal directly from a dev plan.
Create a goal only after the user confirms the Goal Description.

## Workflow

1. Complete the normal research and dev plan first.
2. Draft a Goal Description from the dev plan.
3. Ask the user to confirm or edit the Goal Description.
4. Only after confirmation, call `create_goal` with the confirmed Goal Description.
5. During execution, repeatedly compare actions against the active Goal Description.

## Goal Description Fields

Every Goal Description must include:

```text
Objective:
Scope:
Non-goals:
Acceptance:
Verification:
Tool Policy:
Subagent Policy:
Stop Policy:
Stop / Reframe Conditions:
Runtime Discipline:
```

Minimum requirements:

- At least one concrete deliverable.
- At least three non-goals for moderate/complex work.
- A finite verification plan.
- Explicit stop/reframe conditions.
- A tool retry/stop policy when browser, CI, external APIs, or MCP tools are involved.
- A subagent policy when delegation is allowed or likely.
- A stop policy that says when to stop as complete, stop for approval, stop retries, or stop as blocked.
- Runtime discipline that says when to re-check the description.

For the full template and examples, read `references/goal-description.md`.

## User Confirmation

Before creating the goal, show the filled Goal Description and ask:

```text
我根据 dev plan 整理了 Goal Description。你确认后我再 create_goal；如果要改，优先改 Scope / Non-goals / Stop Policy / Stop Conditions / Tool Policy / Subagent Policy。
```

Do not ask the user to fill the whole form from scratch unless the dev plan lacks enough information.

## Runtime Discipline

After the goal is created, the Goal Description stays active for the whole goal.

Run a short Drift Audit before:

- Editing files.
- Creating a new file or route.
- Changing API, auth, billing, analytics, schema, legal behavior, security behavior, or production config.
- Spawning a subagent.
- Running broad or expensive tools.
- Retrying a failed validation path.
- Committing, pushing, or opening a PR.
- Continuing after user feedback changes direction.

Drift Audit:

```text
1. Is this action inside Scope?
2. Does it violate any Non-goal?
3. Does it trigger a Stop / Reframe Condition?
4. Does Stop Policy say this goal should stop now?
5. Is this tool call inside Tool Policy?
6. Does this subagent task fit Subagent Policy?
7. What evidence will this action produce?
```

If any answer is unclear, stop and ask/reframe before continuing.

## Tool Use

Every tool call must answer a specific question and produce specific evidence.

If browser, CLI, CI, external API, or MCP tooling is part of the goal, define a retry/stop rule in the Goal Description.

For browser/CLI details and stop rules, read `references/tool-policy.md`.

## Subagents

Goal mode plus subagents can improve throughput only when the main agent keeps ownership.

Main agent owns scope, product judgment, architecture judgment, final diff, verification, and user communication.

Subagents may only do bounded local work: research, plan critique, diff review, narrow verification, or tightly scoped implementation.

Before spawning a subagent, define its task, allowed scope, forbidden scope, allowed tools, expected output, and stop condition.

For the full delegation policy and brief template, read `references/subagent-policy.md`.

## Resume Guard

Any handoff or compact summary during an active goal must preserve:

- Goal Outcome.
- Scope.
- Non-goals.
- Stop Conditions.
- Stop Policy.
- Tool Policy.
- Subagent Policy.
- Current phase.
- Verification remaining.
