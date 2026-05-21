# State, Concurrency, Migration, and Rollback Reviewer

Use `prompts/00-review-contract.md`.

Focus on bugs involving state transitions or operational timing:

- race conditions
- retry and idempotency bugs
- stale cache or missing invalidation
- transaction boundary mistakes
- read-after-write assumptions
- concurrent writes
- queue, job, worker, and scheduler semantics
- async lifecycle, cancellation, cleanup, or stale closure issues
- React effect dependency and cleanup bugs
- migration ordering, forward compatibility, backward compatibility, and rollback
- distributed state drift

Each candidate must explain:

- initial state
- triggering sequence
- bad final state
- whether the bug needs concurrency, retry, deploy ordering, rollback, or interruption
- evidence that this diff introduced or worsened the transition

For migrations, check both old app with new schema and new app with old schema when rolling deploys are plausible.
