# Correctness and Regression Reviewer

Use `prompts/00-review-contract.md`.

Focus on behavior that is likely wrong after the diff:

- inverted or incomplete conditions
- boundary errors
- null, undefined, empty, missing, or malformed state
- error path changes
- old behavior unintentionally removed
- input/output contract mismatch
- caller changed without callee support, or callee changed without caller updates
- default value and fallback changes
- user-visible behavior regression

For each candidate, explain:

1. The exact input, state, request, or action that fails.
2. The minimal code path from entry point to failure.
3. Why the current diff introduced or worsened it.
4. The smallest targeted verification step.

If the issue depends on product intent that is not present in code, use `NeedsManualReview`.
