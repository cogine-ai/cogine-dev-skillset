# Upstream synchronization — 2026-09-15

Canonical source: https://github.com/supabase/agent-skills/tree/8331f910845103c08d51f6ca1d86ebb7d1f745e3/skills/supabase-postgres-best-practices

The Cogine intermediary and installed copy retain their short trigger and existing host navigation files. The partial-index reference and contribution commands follow the canonical source.

The contribution guide's package commands apply to a full `supabase/agent-skills` checkout, not this distributed skill folder or the Cogine collection, which has no standalone package/test runner. A local scope note at the top of `references/_contributing.md` makes this packaging distinction explicit; the upstream contribution commands remain unchanged. Validate the distributed copy with file parity, reference checks, and its host's skill validator instead.

One upstream change is held: `references/security-rls-performance.md`. The new example revokes EXECUTE from authenticated roles and then calls that function in their RLS policy; PostgreSQL requires the policy caller to have access to referenced functions. Preserve the previous example until the upstream contract is corrected.

Evidence: https://www.postgresql.org/docs/16/sql-createpolicy.html and https://github.com/supabase/agent-skills/issues/412 . This is a scoped withheld upstream regression, not a claim that the complete package is byte-identical to upstream.
