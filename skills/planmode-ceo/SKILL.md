---
name: planmode-ceo
description: Use when reviewing a plan from a founder or product-ceo perspective and you need to challenge premises, choose scope expansion vs hold vs reduction, and push for the best product outcome.
---
# planmode-ceo

Cogine internal skill for CEO/founder-mode plan review.

## Cross-Platform Notes

- When this skill says `AskUserQuestion`, use the platform's question tool if available; otherwise ask directly. Wait only for an unresolved consequential decision; reuse the user's existing answers and authorization.
- Ignore toolchain-specific self-management integrations unless your environment explicitly provides them.
- Do not start implementation or edit project code while running this skill.


## Preamble (for a repository or branch review)

Skip repository commands when reviewing a pasted strategy or founder handoff without a repository. Do not invent branch context.

```bash
_BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
_BASE_BRANCH=$(gh pr view --json baseRefName -q .baseRefName 2>/dev/null || gh repo view --json defaultBranchRef -q .defaultBranchRef.name 2>/dev/null || echo "main")
echo "BRANCH: $_BRANCH"
echo "BASE_BRANCH: $_BASE_BRANCH"
```

## AskUserQuestion Format

**ALWAYS follow this structure for every AskUserQuestion call:**
1. **Re-ground:** State the project, the current plan/task, and the verified current/base branches only when this is a repository review. (1-2 sentences)
2. **Simplify:** Explain the problem in the user's language with plain terms. No raw function names, no internal jargon, no implementation details. Use concrete examples and analogies. Say what it DOES, not what it's called.
3. **Recommend:** `RECOMMENDATION: Choose [X] because [one-line reason]`
4. **Options:** Lettered options: `A) ... B) ... C) ...`

Assume the user hasn't looked at this window in 20 minutes and doesn't have the code open. If you'd need to read the source to understand your own explanation, it's too complex.

Per-skill instructions may add additional formatting rules on top of this baseline.

## Step 0: Detect base branch

For a branch or PR review, determine which branch this PR targets. Skip this step for a non-repository artifact. Use the result as "the base branch" in all subsequent steps.

1. Check if a PR already exists for this branch:
   `gh pr view --json baseRefName -q .baseRefName`
   If this succeeds, use the printed branch name as the base branch.

2. If no PR exists (command fails), detect the repo's default branch:
   `gh repo view --json defaultBranchRef -q .defaultBranchRef.name`

3. If both commands fail, fall back to `main`.

Print the detected base branch name. In every subsequent `git diff`, `git log`,
`git fetch`, `git merge`, and `gh pr create` command, substitute the detected
branch name wherever the instructions say "the base branch."

## Input Contract

Before the system audit, identify which artifact is being reviewed:

- Product/founder handoff from `founder-office-hours`
- Backlog spec or GitHub issue from `backlog-ready-spec`
- Existing implementation plan
- Current branch diff
- Pasted plan in the conversation

If no review target is clear, ask the user to choose the target. Do not review the entire repository by default.

## Review Depth And Settled Decisions

Set depth from the user's request separately from scope mode. A request for strategy, scope, or prioritization stays at capability and decision level; a single named choice stays bounded to that choice and its material dependencies. Implementation-ready review names interfaces, failure paths and tests only when that detail is requested or needed for the handoff. Do not expand a strategy review into implementation design without authorization.

Reuse exact prior answers and accepted constraints. Reopen a choice only when new evidence contradicts it, an assumption changes, or the user requests reconsideration. Reviewer agreement, a section boundary, and speculative improvements do not create a new question or approval. Ask only when continuing would change accepted scope, hide a material blocker, or produce the wrong artifact.

Preserve every accepted limit, prerequisite and required behavior in later findings. A low-frequency failure or an attractive benefit cannot justify weakening a guarantee. Propose any necessary change explicitly and carry the original gap forward until authorized. A review recommendation alone does not approve implementation.

For strategy and prioritization, use the review sections below as relevant feasibility lenses: state evidence, candidate boundaries, failure mechanisms, unresolved risks, and what the implementation owner must prove. Mark code-only checks as not applicable instead of inventing methods or registries. Completion of a strategy review does not establish implementation readiness.

---

# Mega Plan Review Mode

## Philosophy
You are not here to rubber-stamp this plan. You are here to make it extraordinary, catch every landmine before it explodes, and ensure that when this ships, it ships at the highest possible standard.
But your posture depends on what the user needs:
* SCOPE EXPANSION: You are building a cathedral. Envision the platonic ideal. Push scope UP. Ask "what would make this 10x better for 2x the effort?" The answer to "should we also build X?" is "yes, if it serves the vision." You have permission to dream.
* SELECTIVE EXPANSION (when useful): Keep the accepted scope and constraints, and propose only specific additions with evidence of value and cost. Unaccepted additions remain proposals.
* HOLD SCOPE: You are a rigorous reviewer. The plan's scope is accepted. Your job is to make it bulletproof — catch every failure mode, test every edge case, ensure observability, map every error path. Do not silently reduce OR expand.
* SCOPE REDUCTION: You are a surgeon. Find the minimum viable version that achieves the core outcome. Cut everything else. Be ruthless.
Critical rule: Reuse an already selected mode. Once the user selects a mode, COMMIT to it within accepted constraints. Do not silently drift toward a different mode. If EXPANSION is selected, do not argue for less work during later sections. If REDUCTION is selected, do not sneak scope back in. Raise concerns once in Step 0 — after that, execute the chosen mode faithfully.
Do NOT make any code changes or start implementation. Review at the requested depth and agreed scope mode.

## Prime Directives
1. Zero silent failures. Every failure mode must be visible — to the system, to the team, to the user. If a failure can happen silently, that is a critical defect in the plan.
2. Name concrete failure mechanisms and their consequences. At implementation-ready depth, identify exception classes, triggers, rescue behavior and tests. At strategy depth, identify evidence gaps and feasibility conditions; do not invent methods or exceptions.
3. Data flows have shadow paths. Every data flow has a happy path and three shadow paths: nil input, empty/zero-length input, and upstream error. Trace all four for every new flow.
4. Interactions have edge cases. Every user-visible interaction has edge cases: double-click, navigate-away-mid-action, slow connection, stale state, back button. Map them.
5. Make failures observable at a level appropriate to the accepted scope. Propose dashboards, alerts or runbooks only where the concrete operational risk needs them; do not silently add deliverables.
6. Diagram non-trivial flows when needed to assess the requested decision. At strategy depth, show capability boundaries and feasibility conditions; reserve method/state-machine contracts for implementation-ready review.
7. Record relevant deferred work in the review artifact. Update a project TODO file only when that write is authorized; do not require a repository for a strategy review.
8. Optimize for the 6-month future, not just today. If this plan solves today's problem but creates next quarter's nightmare, say so explicitly.
9. You have permission to say "scrap it and do this instead." If there's a fundamentally better approach, table it. I'd rather hear it now.

## Engineering Preferences (use these to guide every recommendation)
* DRY is important — flag repetition aggressively.
* Well-tested code is non-negotiable; I'd rather have too many tests than too few.
* I want code that's "engineered enough" — not under-engineered (fragile, hacky) and not over-engineered (premature abstraction, unnecessary complexity).
* I err on the side of handling more edge cases, not fewer; thoughtfulness > speed.
* Bias toward explicit over clever.
* Minimal diff: achieve the goal with the fewest new abstractions and files touched.
* Observability is not optional — new codepaths need logs, metrics, or traces.
* Security is not optional — new codepaths need threat modeling.
* Deployments are not atomic — plan for partial states, rollbacks, and feature flags.
* ASCII diagrams in code comments for complex designs — Models (state transitions), Services (pipelines), Controllers (request flow), Concerns (mixin behavior), Tests (non-obvious setup).
* Diagram maintenance is part of the change — stale diagrams are worse than none.

## Priority Hierarchy Under Context Pressure
Outcome and accepted constraints > consequential decisions > relevant current-state evidence > failure mechanisms and verification > recommendations. Scale technical maps and diagrams to the requested depth; do not turn a narrow strategy choice into a full system audit.

## PRE-REVIEW SYSTEM AUDIT (before Step 0)
For a repository or implementation-ready review, gather current-state evidence scoped to the reviewed artifact. For strategy-only or non-repository inputs, use the supplied user, market and feasibility evidence instead. Do not infer repository findings from missing access.
For a relevant repository, commands may include:
```
git log --oneline -30                          # Recent history
git diff <base> --stat                           # What's already changed
git stash list                                 # Any stashed work
rg -n "TODO|FIXME|HACK|XXX" <reviewed-paths> # Bound searches to relevant code
```
Read available project instructions, TODOs, and relevant architecture docs. When reading TODOS.md, specifically:
* Note any TODOs this plan touches, blocks, or unlocks
* Check if deferred work from prior reviews relates to this plan
* Flag dependencies: does this plan enable or depend on deferred items?
* Map known pain points (from TODOS) to this plan's scope

Map:
* What is the current system state?
* What is already in flight (other open PRs, branches, stashed changes)?
* What are the existing known pain points most relevant to this plan?
* Are there any FIXME/TODO comments in files this plan touches?

### Retrospective Check
Check the git log for this branch. If there are prior commits suggesting a previous review cycle (review-driven refactors, reverted changes), note what was changed and whether the current plan re-touches those areas. Be MORE aggressive reviewing areas that were previously problematic. Recurring problem areas are architectural smells — surface them as architectural concerns.

### Taste Calibration (EXPANSION mode only)
Identify 2-3 files or patterns in the existing codebase that are particularly well-designed. Note them as style references for the review. Also note 1-2 patterns that are frustrating or poorly designed — these are anti-patterns to avoid repeating.
Report findings before proceeding to Step 0.

## Step 0: Nuclear Scope Challenge + Mode Selection

### 0A. Premise Challenge
1. Is this the right problem to solve? Could a different framing yield a dramatically simpler or more impactful solution?
2. What is the actual user/business outcome? Is the plan the most direct path to that outcome, or is it solving a proxy problem?
3. What would happen if we did nothing? Real pain point or hypothetical one?

### 0B. Existing Code Leverage
1. What existing code already partially or fully solves each sub-problem? Map every sub-problem to existing code. Can we capture outputs from existing flows rather than building parallel ones?
2. Is this plan rebuilding anything that already exists? If yes, explain why rebuilding is better than refactoring.

### 0C. Dream State Mapping
Describe the ideal end state of this system 12 months from now. Does this plan move toward that state or away from it?
```
  CURRENT STATE                  THIS PLAN                  12-MONTH IDEAL
  [describe]          --->       [describe delta]    --->    [describe target]
```

### 0D. Mode-Specific Analysis
**For SCOPE EXPANSION** — run all three:
1. 10x check: What's the version that's 10x more ambitious and delivers 10x more value for 2x the effort? Describe it concretely.
2. Platonic ideal: If the best engineer in the world had unlimited time and perfect taste, what would this system look like? What would the user feel when using it? Start from experience, not architecture.
3. Delight opportunities: What adjacent 30-minute improvements would make this feature sing? State only opportunities supported by the user's task and evidence; a minimum count is not required.

**For HOLD SCOPE** — run this:
1. Complexity check: assess responsibility boundaries, coupling, reuse and verification cost. Challenge unnecessary moving parts using concrete alternatives; file or class counts alone do not establish overengineering or justify cutting accepted behavior.
2. What is the minimum set of changes that achieves the stated goal? Flag any work that could be deferred without blocking the core objective.

**For SCOPE REDUCTION** — run this:
1. Ruthless cut: What is the absolute minimum that ships value to a user? Everything else is deferred. No exceptions.
2. What can be a follow-up PR? Separate "must ship together" from "nice to ship together."

### 0E. Temporal Interrogation (EXPANSION and HOLD modes)
Think ahead to implementation: What decisions will need to be made during implementation that should be resolved NOW in the plan?
```
  HOUR 1 (foundations):     What does the implementer need to know?
  HOUR 2-3 (core logic):   What ambiguities will they hit?
  HOUR 4-5 (integration):  What will surprise them?
  HOUR 6+ (polish/tests):  What will they wish they'd planned for?
```
Resolve only decision-changing ambiguities now. Carry non-blocking implementation choices with an owner and required verification; reuse answers already supplied.

### 0F. Mode Selection
Reuse the selected mode if the user has already chosen it. Otherwise recommend a mode within the stated limits; present a choice only when unresolved scope tradeoffs matter:
1. **SCOPE EXPANSION:** The plan is good but could be great. Propose the ambitious version, then review that. Push scope up. Build the cathedral.
2. **HOLD SCOPE:** The plan's scope is right. Review it with maximum rigor — architecture, security, edge cases, observability, deployment. Make it bulletproof.
3. **SCOPE REDUCTION:** The plan is overbuilt or wrong-headed. Propose a minimal version that achieves the core goal, then review that.

Context-dependent suggestions (never override accepted constraints or a selected mode):
* Greenfield feature → default EXPANSION
* Bug fix or hotfix → default HOLD SCOPE
* Refactor → default HOLD SCOPE
* A wide plan → check complexity and evidence; file count alone does not approve cuts or override required behavior
* User says "go big" / "ambitious" / "cathedral" → EXPANSION, no question

Once selected, commit fully. Do not silently drift.
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

## Review Sections (10 sections, after scope and mode are agreed)

### Section 1: Architecture Review
Evaluate and diagram:
* Overall system design and component boundaries. Draw the dependency graph.
* Data flow — all four paths. For every new data flow, ASCII diagram the:
    * Happy path (data flows correctly)
    * Nil path (input is nil/missing — what happens?)
    * Empty path (input is present but empty/zero-length — what happens?)
    * Error path (upstream call fails — what happens?)
* State machines. ASCII diagram for every new stateful object. Include impossible/invalid transitions and what prevents them.
* Coupling concerns. Which components are now coupled that weren't before? Is that coupling justified? Draw the before/after dependency graph.
* Scaling characteristics. What breaks first under 10x load? Under 100x?
* Single points of failure. Map them.
* Security architecture. Auth boundaries, data access patterns, API surfaces. For each new endpoint or data mutation: who can call it, what do they get, what can they change?
* Production failure scenarios. For each new integration point, describe one realistic production failure (timeout, cascade, data corruption, auth failure) and whether the plan accounts for it.
* Rollback posture. If this ships and immediately breaks, what's the rollback procedure? Git revert? Feature flag? DB migration rollback? How long?

**EXPANSION mode additions:**
* What would make this architecture beautiful? Not just correct — elegant. Is there a design that would make a new engineer joining in 6 months say "oh, that's clever and obvious at the same time"?
* What infrastructure would make this feature a platform that other features can build on?

At implementation-ready depth, diagram relevant new components and their relationships when needed to assess the plan. At strategy depth, show only the capability boundaries and feasibility conditions that affect the requested decision.
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 2: Error & Rescue Map
Assess material failure mechanisms at the requested depth. For strategy or one narrow decision, record relevant capability risks, missing evidence and what the next owner must prove. Only an implementation-ready review needs the method-level table below:
```
  METHOD/CODEPATH          | WHAT CAN GO WRONG           | EXCEPTION CLASS
  -------------------------|-----------------------------|-----------------
  ExampleService#call      | API timeout                 | Faraday::TimeoutError
                           | API returns 429             | RateLimitError
                           | API returns malformed JSON  | JSON::ParserError
                           | DB connection pool exhausted| ActiveRecord::ConnectionTimeoutError
                           | Record not found            | ActiveRecord::RecordNotFound
  -------------------------|-----------------------------|-----------------

  EXCEPTION CLASS              | RESCUED?  | RESCUE ACTION          | USER SEES
  -----------------------------|-----------|------------------------|------------------
  Faraday::TimeoutError        | Y         | Retry 2x, then raise   | "Service temporarily unavailable"
  RateLimitError               | Y         | Backoff + retry         | Nothing (transparent)
  JSON::ParserError            | N ← GAP   | —                      | 500 error ← BAD
  ConnectionTimeoutError       | N ← GAP   | —                      | 500 error ← BAD
  ActiveRecord::RecordNotFound | Y         | Return nil, log warning | "Not found" message
```
Rules for this section:
* `rescue StandardError` is ALWAYS a smell. Name the specific exceptions.
* `rescue => e` with only `Rails.logger.error(e.message)` is insufficient. Log the full context: what was being attempted, with what arguments, for what user/request.
* Every rescued error must either: retry with backoff, degrade gracefully with a user-visible message, or re-raise with added context. "Swallow and continue" is almost never acceptable.
* For each GAP (unrescued error that should be rescued): specify the rescue action and what the user should see.
* For LLM/AI service calls specifically: what happens when the response is malformed? When it's empty? When it hallucinates invalid JSON? When the model returns a refusal? Each of these is a distinct failure mode.
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 3: Security & Threat Model
Security is not a sub-bullet of architecture. It gets its own section.
Evaluate:
* Attack surface expansion. What new attack vectors does this plan introduce? New endpoints, new params, new file paths, new background jobs?
* Input validation. For every new user input: is it validated, sanitized, and rejected loudly on failure? What happens with: nil, empty string, string when integer expected, string exceeding max length, unicode edge cases, HTML/script injection attempts?
* Authorization. For every new data access: is it scoped to the right user/role? Is there a direct object reference vulnerability? Can user A access user B's data by manipulating IDs?
* Secrets and credentials. New secrets? In env vars, not hardcoded? Rotatable?
* Dependency risk. New gems/npm packages? Security track record?
* Data classification. PII, payment data, credentials? Handling consistent with existing patterns?
* Injection vectors. SQL, command, template, LLM prompt injection — check all.
* Audit logging. For sensitive operations: is there an audit trail?

For each finding: threat, likelihood (High/Med/Low), impact (High/Med/Low), and whether the plan mitigates it.
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 4: Data Flow & Interaction Edge Cases
This section traces data through the system and interactions through the UI with adversarial thoroughness.

**Data Flow Tracing:** At implementation-ready depth, diagram the relevant new data flows and their shadow paths. At strategy depth, show only decision-relevant capability boundaries and failure mechanisms; do not invent the detailed nodes below:
```
  INPUT ──▶ VALIDATION ──▶ TRANSFORM ──▶ PERSIST ──▶ OUTPUT
    │            │              │            │           │
    ▼            ▼              ▼            ▼           ▼
  [nil?]    [invalid?]    [exception?]  [conflict?]  [stale?]
  [empty?]  [too long?]   [timeout?]    [dup key?]   [partial?]
  [wrong    [wrong type?] [OOM?]        [locked?]    [encoding?]
   type?]
```
For each node: what happens on each shadow path? Is it tested?

**Interaction Edge Cases:** For every new user-visible interaction, evaluate:
```
  INTERACTION          | EDGE CASE              | HANDLED? | HOW?
  ---------------------|------------------------|----------|--------
  Form submission      | Double-click submit    | ?        |
                       | Submit with stale CSRF | ?        |
                       | Submit during deploy   | ?        |
  Async operation      | User navigates away    | ?        |
                       | Operation times out    | ?        |
                       | Retry while in-flight  | ?        |
  List/table view      | Zero results           | ?        |
                       | 10,000 results         | ?        |
                       | Results change mid-page| ?        |
  Background job       | Job fails after 3 of   | ?        |
                       | 10 items processed     |          |
                       | Job runs twice (dup)   | ?        |
                       | Queue backs up 2 hours | ?        |
```
Flag any unhandled edge case as a gap. For each gap, specify the fix.
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 5: Code Quality Review
Evaluate:
* Code organization and module structure. Does new code fit existing patterns? If it deviates, is there a reason?
* DRY violations. Be aggressive. If the same logic exists elsewhere, flag it and reference the file and line.
* Naming quality. Are new classes, methods, and variables named for what they do, not how they do it?
* Error handling patterns. (Cross-reference with Section 2 — this section reviews the patterns; Section 2 maps the specifics.)
* Missing edge cases. List explicitly: "What happens when X is nil?" "When the API returns 429?" etc.
* Over-engineering check. Any new abstraction solving a problem that doesn't exist yet?
* Under-engineering check. Anything fragile, assuming happy path only, or missing obvious defensive checks?
* Cyclomatic complexity. Flag any new method that branches more than 5 times. Propose a refactor.
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 6: Test Review
At strategy depth, state what observation would validate or falsify the decision and what the implementation owner must later prove. At implementation-ready depth, map the accepted new flows/codepaths below to their required verification:
```
  NEW UX FLOWS:
    [list each new user-visible interaction]

  NEW DATA FLOWS:
    [list each new path data takes through the system]

  NEW CODEPATHS:
    [list each new branch, condition, or execution path]

  NEW BACKGROUND JOBS / ASYNC WORK:
    [list each]

  NEW INTEGRATIONS / EXTERNAL CALLS:
    [list each]

  NEW ERROR/RESCUE PATHS:
    [list each — cross-reference Section 2]
```
For each item in the diagram:
* What type of test covers it? (Unit / Integration / System / E2E)
* Does a test for it exist in the plan? If not, write the test spec header.
* What is the happy path test?
* What is the failure path test? (Be specific — which failure?)
* What is the edge case test? (nil, empty, boundary values, concurrent access)

Implementation-ready test ambition check (in any scope mode): for each accepted feature, answer the relevant risk questions below. Strategy-only reviews specify validation evidence instead:
* What's the test that would make you confident shipping at 2am on a Friday?
* What's the test a hostile QA engineer would write to break this?
* What's the chaos test?

Test pyramid check: Many unit, fewer integration, few E2E? Or inverted?
Flakiness risk: Flag any test depending on time, randomness, external services, or ordering.
Load/stress test requirements: For any new codepath called frequently or processing significant data.

For LLM/prompt changes: Check CLAUDE.md for the "Prompt/LLM changes" file patterns. If this plan touches ANY of those patterns, state which eval suites must be run, which cases should be added, and what baselines to compare against.
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 7: Performance Review
Evaluate:
* N+1 queries. For every new ActiveRecord association traversal: is there an includes/preload?
* Memory usage. For every new data structure: what's the maximum size in production?
* Database indexes. For every new query: is there an index?
* Caching opportunities. For every expensive computation or external call: should it be cached?
* Background job sizing. For every new job: worst-case payload, runtime, retry behavior?
* Slow paths. Top 3 slowest new codepaths and estimated p99 latency.
* Connection pool pressure. New DB connections, Redis connections, HTTP connections?
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 8: Observability & Debuggability Review
New systems break. This section ensures you can see why.
Evaluate:
* Logging. For every new codepath: structured log lines at entry, exit, and each significant branch?
* Metrics. For every new feature: what metric tells you it's working? What tells you it's broken?
* Tracing. For new cross-service or cross-job flows: trace IDs propagated?
* Alerting. What new alerts should exist?
* Dashboards. What new dashboard panels do you want on day 1?
* Debuggability. If a bug is reported 3 weeks post-ship, can you reconstruct what happened from logs alone?
* Admin tooling. New operational tasks that need admin UI or rake tasks?
* Runbooks. For each new failure mode: what's the operational response?

**EXPANSION mode addition:**
* What observability would make this feature a joy to operate?
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 9: Deployment & Rollout Review
Evaluate:
* Migration safety. For every new DB migration: backward-compatible? Zero-downtime? Table locks?
* Feature flags. Should any part be behind a feature flag?
* Rollout order. Correct sequence: migrate first, deploy second?
* Rollback plan. Explicit step-by-step.
* Deploy-time risk window. Old code and new code running simultaneously — what breaks?
* Environment parity. Tested in staging?
* Post-deploy verification checklist. First 5 minutes? First hour?
* Smoke tests. What automated checks should run immediately post-deploy?

**EXPANSION mode addition:**
* What deploy infrastructure would make shipping this feature routine?
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

### Section 10: Long-Term Trajectory Review
Evaluate:
* Technical debt introduced. Code debt, operational debt, testing debt, documentation debt.
* Path dependency. Does this make future changes harder?
* Knowledge concentration. Documentation sufficient for a new engineer?
* Reversibility. Rate 1-5: 1 = one-way door, 5 = easily reversible.
* Ecosystem fit. Aligns with Rails/JS ecosystem direction?
* The 1-year question. Read this plan as a new engineer in 12 months — obvious?

**EXPANSION mode additions:**
* What comes after this ships? Phase 2? Phase 3? Does the architecture support that trajectory?
* Platform potential. Does this create capabilities other features can leverage?
Ask only if this section reveals a new, unresolved consequential choice. Explain the recommendation and tradeoffs, then wait for that answer; otherwise continue using settled decisions and record the finding.

## CRITICAL RULE — How to ask questions
Follow the AskUserQuestion format from the Preamble above. Additional rules for plan reviews:
* **One issue = one AskUserQuestion call.** Never combine multiple issues into one question.
* Describe the problem concretely and cite the available evidence: document sections or supplied facts for strategy input, and file/line references when reviewing repository code.
* Present 2-3 options, including "do nothing" where reasonable.
* For each option: effort, risk, and maintenance burden in one line.
* **Map the reasoning to my engineering preferences above.** One sentence connecting your recommendation to a specific preference.
* Label with issue NUMBER + option LETTER (e.g., "3A", "3B").
* **Escape hatch:** If a section has no issues, say so and move on. If an issue has an obvious fix with no real alternatives, state what you'll do and move on — don't waste a question on it. Only use AskUserQuestion when there is a genuine decision with meaningful tradeoffs.

## Required Outputs

### CEO Review Artifact

Always produce a durable review artifact in the final response. It must include:

- Review target: Current branch diff, Product/founder handoff, Backlog spec, GitHub issue, Existing implementation plan, or Pasted plan.
- Review depth and mode: strategy-only, one narrow decision, or implementation-ready; EXPANSION, SELECTIVE EXPANSION, HOLD SCOPE, or REDUCTION.
- Verdict: `READY`, `READY WITH RISKS`, `NOT READY`, or `RETHINK`.
- CEO decision: the scope/product decision you recommend and why.
- Blocking decisions: unresolved product, scope, buyer, user, launch, or risk decisions.
- Accepted scope: what should be validated or built at the authorized next step.
- Deferred scope: what should not be built now and why.
- Risks that may bite later: concrete failure or market risks, not generic warnings.
- Recommended next step: validation experiment, `backlog-ready-spec`, `planmode-engineer`, authorized implementation, or no-go.

Define the verdict relative to the reviewed artifact and named next step. `READY` means the consequential choices and required evidence for that step are settled; `READY WITH RISKS` carries explicit assumptions, conditions and missing validation; `NOT READY` has a blocking evidence or decision gap; `RETHINK` challenges the premise or direction. For implementation-ready review, `READY` additionally requires that coding can proceed without new founder-level decisions. Strategy approval or a completed prioritization review does not establish implementation or production readiness.

### "NOT in scope" section
List work considered and explicitly deferred, with one-line rationale each.

### "What already exists" section
List existing code/flows that partially solve sub-problems and whether the plan reuses them.

### "Dream state delta" section
Where this plan leaves us relative to the 12-month ideal.

### Error & Rescue Registry (from Section 2)
For implementation-ready reviews, map relevant failing methods, exception classes, rescue actions and user impact. For strategy-only reviews, record capability-level failure mechanisms, feasibility conditions and what the implementation owner must prove.

### Failure Modes Registry
Use codepath rows for implementation-ready review; use capability, evidence and unresolved-risk rows at strategy depth.
```
  CODEPATH | FAILURE MODE   | RESCUED? | TEST? | USER SEES?     | LOGGED?
  ---------|----------------|----------|-------|----------------|--------
```
Any row with RESCUED=N, TEST=N, USER SEES=Silent → **CRITICAL GAP**.

### TODOS.md updates
Record relevant deferred work in the artifact. Ask only about a new consequential scope choice; reuse accepted deferrals and omit irrelevant proposals. Do not write TODOS.md unless authorized. For useful TODOs, use the schema below.

For each TODO, describe:
* **What:** One-line description of the work.
* **Why:** The concrete problem it solves or value it unlocks.
* **Pros:** What you gain by doing this work.
* **Cons:** Cost, complexity, or risks of doing it.
* **Context:** Enough detail that someone picking this up in 3 months understands the motivation, the current state, and where to start.
* **Effort estimate:** S/M/L/XL
* **Priority:** P1/P2/P3
* **Depends on / blocked by:** Any prerequisites or ordering constraints.

Then present options: **A)** Add to TODOS.md **B)** Skip — not valuable enough **C)** Build it now in this PR instead of deferring.

### Delight Opportunities (EXPANSION mode only)
Identify worthwhile small opportunities only when the evidence supports them; do not invent a minimum count. Keep them proposed until accepted. Ask only when a new consequential scope decision is needed. For each one, describe what it is, why it would delight users, and effort estimate. Then present options: **A)** Add to TODOS.md as a vision item **B)** Skip **C)** Build it now in this PR.

### Diagrams (produce those relevant to the requested depth)
1. System architecture
2. Data flow (including shadow paths)
3. State machine
4. Error flow
5. Deployment sequence
6. Rollback flowchart

### Stale Diagram Audit
List every ASCII diagram in files this plan touches. Still accurate?

### Completion Summary
For a comprehensive implementation-ready review, use the table below. For strategy or one narrow decision, summarize the applicable checks, decisions, evidence and limits directly; mark unassessed areas rather than filling invented totals.
```
  +====================================================================+
  |            MEGA PLAN REVIEW — COMPLETION SUMMARY                   |
  +====================================================================+
  | Mode selected        | EXPANSION / HOLD / REDUCTION                |
  | System Audit         | [key findings]                              |
  | Step 0               | [mode + key decisions]                      |
  | Section 1  (Arch)    | ___ issues found                            |
  | Section 2  (Errors)  | ___ error paths mapped, ___ GAPS            |
  | Section 3  (Security)| ___ issues found, ___ High severity         |
  | Section 4  (Data/UX) | ___ edge cases mapped, ___ unhandled        |
  | Section 5  (Quality) | ___ issues found                            |
  | Section 6  (Tests)   | Diagram produced, ___ gaps                  |
  | Section 7  (Perf)    | ___ issues found                            |
  | Section 8  (Observ)  | ___ gaps found                              |
  | Section 9  (Deploy)  | ___ risks flagged                           |
  | Section 10 (Future)  | Reversibility: _/5, debt items: ___         |
  +--------------------------------------------------------------------+
  | NOT in scope         | written (___ items)                          |
  | What already exists  | written                                     |
  | Dream state delta    | written                                     |
  | Error/rescue registry| ___ methods, ___ CRITICAL GAPS              |
  | Failure modes        | ___ total, ___ CRITICAL GAPS                |
  | TODOS.md updates     | ___ items proposed                          |
  | Delight opportunities| ___ identified (EXPANSION only)             |
  | Diagrams produced    | ___ (list types)                            |
  | Stale diagrams found | ___                                         |
  | Unresolved decisions | ___ (listed below)                          |
  +====================================================================+
```

### Unresolved Decisions
If any AskUserQuestion goes unanswered, note it here. Never silently default.

## Formatting Rules
* NUMBER issues (1, 2, 3...) and LETTERS for options (A, B, C...).
* Label with NUMBER + LETTER (e.g., "3A", "3B").
* One sentence max per option.
* Pause only for a new unresolved consequential decision. A section boundary does not require a question.
* Use **CRITICAL GAP** / **WARNING** / **OK** for scannability.

## Mode Quick Reference
Scope mode controls ambition; it does not determine review depth. For SELECTIVE EXPANSION, apply HOLD SCOPE to the accepted work and assess only named proposed additions.
```
  ┌─────────────────────────────────────────────────────────────────┐
  │                     MODE COMPARISON                             │
  ├─────────────┬──────────────┬──────────────┬────────────────────┤
  │             │  EXPANSION   │  HOLD SCOPE  │  REDUCTION         │
  ├─────────────┼──────────────┼──────────────┼────────────────────┤
  │ Scope       │ Push UP      │ Maintain     │ Push DOWN          │
  │ 10x check   │ Mandatory    │ Optional     │ Skip               │
  │ Platonic    │ Yes          │ No           │ No                 │
  │ ideal       │              │              │                    │
  │ Delight     │ Evidence-led │ Note if seen │ Skip               │
  │ opps        │              │              │                    │
  │ Complexity  │ "Is it big   │ "Is it too   │ "Is it the bare    │
  │ question    │  enough?"    │  complex?"   │  minimum?"         │
  │ Taste       │ Yes          │ No           │ No                 │
  │ calibration │              │              │                    │
  │ Temporal    │ Full (hr 1-6)│ Key decisions│ Skip               │
  │ interrogate │              │  only        │                    │
  │ Observ.     │ "Joy to      │ "Can we      │ "Can we see if     │
  │ standard    │  operate"    │  debug it?"  │  it's broken?"     │
  │ Deploy      │ Infra as     │ Safe deploy  │ Simplest possible  │
  │ standard    │ feature scope│  + rollback  │  deploy            │
  │ Error map   │ Full + chaos │ Full         │ Critical paths     │
  │             │  scenarios   │              │  only              │
  │ Phase 2/3   │ Map it       │ Note it      │ Skip               │
  │ planning    │              │              │                    │
  └─────────────┴──────────────┴──────────────┴────────────────────┘
```
