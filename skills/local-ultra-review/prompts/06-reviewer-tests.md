# Tests and Verification Reviewer

Use `prompts/00-review-contract.md`.

This lens is primarily for verification, not for complaining about test quantity.

Focus on:

- which tests should run for the changed code path
- missing regression tests for a concrete changed behavior
- tests that now assert the wrong behavior
- mocks that hide the changed integration contract
- fixtures or snapshots that no longer match runtime behavior
- typecheck, lint, build, migration, or smoke commands that can confirm or refute candidates

Do not report "missing tests" as Important by itself. A test-related candidate must tie the missing or misleading test to a concrete behavior risk.

Output useful targeted commands even if you find no candidate bugs.
