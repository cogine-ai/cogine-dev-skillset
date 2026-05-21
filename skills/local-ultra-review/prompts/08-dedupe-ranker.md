# Dedupe and Ranker

Input: verified findings.

Keep only:

- `confirmed` findings for the main Important and Nit sections
- `pre_existing` findings in the Pre-existing section
- `needs_manual_review` findings in the appendix

Drop false positives.

## Dedupe Rules

- Same root cause: one finding.
- Same bug at multiple call sites: one finding with multiple evidence entries.
- Same contract break with producer and consumer evidence: one finding.
- Same file and line but different symptoms: merge unless they are genuinely separate bugs.
- Prefer the clearest title and strongest failure scenario.

## Severity Order

Rank by:

1. Security, privacy, permission, or data loss
2. Production behavior break
3. Migration, rollback, or data compatibility risk
4. Integration contract break
5. Concurrency, retry, or idempotency issue
6. Concrete test blind spot
7. Nit

## Limits

- Important: no artificial limit, but merge duplicates
- Nit: at most 5
- Needs manual review: appendix only
- Main report: at most 20 unless the user requests all confirmed findings

If there are no confirmed findings, say that clearly.
