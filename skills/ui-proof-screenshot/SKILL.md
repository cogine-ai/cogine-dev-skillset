---
name: ui-proof-screenshot
description: "Capture and inspect focused screenshots from a real Codex in-app Browser flow. Use when a GUI or Web UI change needs static visual evidence, when the worker must show the trigger/input and successful result, or when the owner asks for screenshots. This skill captures media only; use browser-verify for the actual functional flow."
---

# UI Proof Screenshot

Capture static visual evidence from an already identified real UI flow. The assigned worker invokes this skill directly; it is independent of `fresh-eyes`.

## Capture contract

- Use the Codex in-app Browser and follow `browser:control-in-app-browser`.
- Capture enough surrounding UI to identify the page, target control/state, and result.
- Use one screenshot when it proves the whole state. Use a small sequence when the trigger/input and result cannot fit meaningfully in one frame.
- A screenshot of an isolated component, mockup, unrelated page, loading shell, or presence-only control is not proof of the requested behavior.
- Do not include secrets, passwords, tokens, private account data, or unrelated personal content.

## Procedure

1. Let `browser-verify` or the worker's product flow reach the relevant state.
2. Capture the viewport or a focused clip with the Browser screenshot API.
3. Read the saved image yourself and confirm it visibly contains the intended evidence.
4. If the image is ambiguous, reposition or capture one additional state; do not generate a large screenshot dump.
5. Save under `/tmp`, an ignored `.tmp/proof`, or another owner-approved local evidence directory.
6. Verify screenshots are not staged or tracked by Git.

## Return

For each image report:

- absolute path;
- what user action/state it proves;
- any visual detail that remains ambiguous.

Screenshots do not replace console, network, runtime, DB, or cleanup evidence.
