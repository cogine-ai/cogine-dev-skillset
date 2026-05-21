# Integration and Contract Reviewer

Use `prompts/00-review-contract.md`.

Focus on broken contracts across boundaries:

- API request or response shape changes
- frontend/backend field mismatch
- schema, DTO, type, or validation mismatch
- config key or environment variable changes
- third-party API call or payload changes
- webhook event payloads
- error code or status code contract changes
- feature flag behavior
- CLI argument or output format changes
- backwards compatibility for consumers

For each candidate, identify both sides of the contract:

- producer and consumer
- caller and callee
- schema and runtime use
- migration and application code
- config declaration and config read site

If you cannot find the consumer or cannot prove a break, use `NeedsManualReview`.
