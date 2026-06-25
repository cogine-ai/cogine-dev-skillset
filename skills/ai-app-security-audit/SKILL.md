---
name: ai-app-security-audit
description: Use when auditing AI applications, LLM features, agent workflows, RAG systems, tool-calling code, prompt pipelines, model output handling, AI API keys, cost controls, or skill/agent supply-chain risks.
---

# AI App Security Audit

Use this skill for security work specific to AI applications. It complements `security-best-practices`; do not replace framework security checks with this skill.

## Core Rule

Only report findings with a concrete exploit path or failure scenario. Do not list generic AI risks unless the current code, config, prompt flow, or architecture actually exposes them.

## Scope

Audit these surfaces when present:

- Prompt assembly and role boundaries.
- User content flowing into system prompts, tool schemas, eval prompts, or agent instructions.
- Tool/function calling and argument validation.
- RAG ingestion, retrieval, citation, and source trust.
- LLM output parsing, schema validation, sanitization, and downstream execution.
- AI API keys, provider credentials, model routing, and proxy credentials.
- Cost, quota, retry, queue, and spend amplification controls.
- Agent memory, long-term context, uploaded files, browser sessions, and workspace access.
- Skill/plugin/agent supply chain, including local instructions that can run commands or read credentials.

## Workflow

1. Map AI data flow.
   - Identify inputs: user text, files, URLs, database rows, RAG chunks, web pages, tool outputs.
   - Identify prompt construction: system, developer, user, tool, and hidden context.
   - Identify model calls and providers.
   - Identify tool calls, side effects, and output consumers.

2. Find trust boundary crossings.
   - Untrusted content entering privileged prompt positions.
   - Untrusted content shaping tool names, schemas, arguments, SQL, shell commands, file paths, URLs, or auth scopes.
   - Model output becoming executable code, HTML, SQL, shell, JSON instructions, or persisted state.

3. Check AI-specific risks.
   - Prompt injection that changes instructions or tool behavior.
   - RAG poisoning or untrusted retrieval content overriding app policy.
   - Tool call without schema validation, authorization, or allowlists.
   - Output parser trusting malformed, empty, hallucinated, or refusal responses.
   - Missing rate limits, retry caps, token caps, queue caps, or budget limits.
   - Secrets exposed through logs, traces, prompts, eval fixtures, screenshots, or tool results.
   - Cross-user memory or document leakage.
   - Unsafe browser, filesystem, terminal, or SaaS-account actions.

4. Verify before reporting.
   - Quote the exact file and line when possible.
   - Explain attacker control, trust boundary, exploit path, impact, and why existing controls do not block it.
   - If confidence is below 8/10 for a normal audit, mark it as `Needs verification` instead of a finding.

5. Produce fixes or a report depending on the user's request.
   - For a report-only audit, do not edit files.
   - For fix work, address one finding at a time and run the relevant tests.

## False Positive Rules

- User content in a normal user-message position is not prompt injection by itself.
- A model returning wrong prose is not a security issue unless it crosses into privileged action, data exposure, fraud, compliance, or cost impact.
- Missing HSTS, TLS, or generic web headers belongs in `security-best-practices`, not this skill, unless directly tied to AI credential or data exposure.
- A theoretical jailbreak is not reportable without an app-specific path to data, tools, cost, or policy bypass.

## Report Contract

Use this structure:

```markdown
## AI App Security Audit

### Executive Summary
Overall risk:
Audit scope:
Confidence:

### AI Data Flow
Inputs:
Prompt assembly:
Model calls:
Tool calls:
Stored outputs/memory:

### Findings

#### AI-SEC-001: <title>
Severity: Critical / High / Medium / Low
Confidence: 8/10+
Evidence: <file:line>
Attacker control:
Trust boundary crossed:
Exploit path:
Impact:
Existing controls:
Recommended fix:
Validation:

### Needs Verification
- Items with plausible risk but insufficient proof.

### Not In Scope
- Security areas intentionally left to other skills or audits.
```

## Severity Guide

- Critical: secret exfiltration, cross-tenant data exposure, arbitrary tool execution, irreversible external side effects, or uncontrolled spend.
- High: prompt/tool/RAG path that can access sensitive data, perform unauthorized writes, or materially bypass policy.
- Medium: validated but bounded risk with limited data/action/cost impact.
- Low: hardening issue with clear code evidence but no immediate exploit path.
