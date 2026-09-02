---
name: onsite-prototype-development
description: Build a clickable onsite sales prototype from an operator-confirmed product brief and design brief, preferably using a compatible Project Template. Implement only the core business loop, prove it in a real browser, and clearly separate working interaction from mocked external capabilities.
---

# Onsite Prototype Development

Build the smallest convincing, clickable prototype for a product and design that the operator has
already confirmed. Accurate completion is more important than perfect engineering. The goal is a
working customer conversation aid, not a production system.

## Required Input

Require:

- one confirmed product brief from `onsite-product-manager`;
- one matching confirmed design brief from `onsite-product-design`;
- an existing target project or permission to create a new one.

Equivalent explicit context in the conversation is acceptable; special IDs, freeze documents,
gate matrices, or card schemas are not required. If the product or design has not been confirmed,
stop and ask for that decision. Do not invent or silently choose either one.

## Project Route

Prefer a compatible Project Template. If the operator supplied one, use it. Otherwise read
[references/project-template-registry.md](references/project-template-registry.md) and use a clear
match. If no suitable template or authorized destination exists, ask one short routing question.

Never modify the Project Template source by accident. Create or use an independent target project,
then read its `AGENTS.md`, `CLAUDE.md`, manifest, setup guide, existing dependencies, editable paths,
and validation commands before changing code.

## Build The Core Loop

Implement only what is needed for this causal demonstration:

```text
customer-shaped input or user action
-> visible processing or decision
-> meaningful state change
-> recognizable business result
-> reset or repeat
```

Rules:

- Preserve the confirmed product mechanism and selected design composition.
- If ten functions were discussed, build only the functions needed for the core loop.
- Use the target project's existing stack and components before adding dependencies.
- Buttons and controls in the demo path must work; navigation-only tours and static mock screens do
  not count.
- Synthetic data and simulated intelligence are allowed when clearly labeled. Do not imply that
  telephony, databases, integrations, persistence, accuracy, or production deployment are real when
  they are not.
- Do not add a backend, database, authentication, or external integration unless the confirmed loop
  actually requires it and the operator authorized it.

## Verify And Stop

Run the project's fastest relevant validation. Then use a real browser to exercise the exact demo
path, check the meaningful result and reset, inspect visible layout and blocking console errors, and
capture focused screenshots.

Stop when the confirmed core loop is convincing and repeatable. Present the running result to the
operator for visual acceptance; do not keep polishing or add adjacent features automatically.

Return only what helps the onsite team use and judge it:

- project path and running URL;
- a short click-through demo path;
- what actually works;
- what is mocked or assumed;
- checks actually run;
- anything still not proven.

Publishing and productionization are separate requests.
