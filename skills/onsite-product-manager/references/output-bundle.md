# Output Bundle Contract

Produce one product bundle per meeting context freeze. It is a product-hypothesis portfolio and
prototype experiment plan, not a PRD. Separate the three audiences instead of compressing everything
into one long document.

```text
<output-directory>/
  onsite-product-board.md
  context-freeze.md
  build-cards/
    P01.md
    P02.md
    ...
```

## 1. Human-Facing Product Board

`onsite-product-board.md` is the only artifact shown by default in the response. Write it in the
operator's language; default to concise Simplified Chinese. Use this exact structure:

```markdown
# 现场产品方向

状态：可以进入原型 / 可以进入原型，但有风险 / 材料待补充
一句话判断：<这些方向共同在验证什么>
建议演示顺序：P01 → P02 → P03

## P01｜<具体产品名称>
- 谁在用：<角色和使用时机>
- 解决什么：<现在最具体的问题>
- 怎么演示：<一个动作到一个结果>
- 老板看到：<两分钟内可识别的业务变化>
- 要确认：<一个会改变决策的问题>
- 暂时模拟：<数据、智能或外部系统边界>
```

Repeat the direction block for every supported proposition. Apply these rules exactly:

- use exactly the six bullet fields for every direction; do not add paragraphs or sub-sections;
- keep every field to one short sentence and one meaning;
- use the customer's business language, not product-management or engineering terminology;
- do not show evidence IDs, gate names, scores, portfolio roles, detailed risks, or reasoning steps;
- avoid labels such as `Product proposition`, `Evidence Gate`, `Distinct mechanism`, `Context Freeze`,
  and `Build Card` on this board;
- name what the user does and what changes; avoid generic claims such as “AI empowers efficiency”;
- keep a 3-5 direction board to roughly one or two screens, normally about 40 lines;
- the suggested sequence is an internal presentation order, not a reduction of the comparison batch.

Map the internal verdict to plain language:

- `READY` -> `可以进入原型`;
- `READY WITH RISKS` -> `可以进入原型，但有风险`;
- `NOT READY` -> `材料待补充`.

Do not make the board sound more certain than the internal evidence. If the bundle is `NOT READY`,
the board may still show provisional directions, but its one-line judgment must name the single most
important missing material in ordinary language.

## 2. Internal Context Freeze

`context-freeze.md` preserves the evidence and decisions needed for audit, later correction, and
downstream execution. It is never shown to the customer by default. Use this structure:

```markdown
# Context Freeze

Freeze ID:
Source status: full-transcript / summary-only / notes-only
Sources:
Operator focus:
Customer context:
Target prototype count:
Comparison batch ID:
Time boundary:

## Evidence Index
| ID | Type | Evidence or unknown | Source |
|---|---|---|---|
| E01 | Fact / Operator interpretation / Product hypothesis / Unknown | ... | ... |

## Portfolio Judgment
Product opportunity:
Recommended internal sequence:
Coverage: Anchor / Contrast / Stretch

| ID | Role | Evidence | Mechanism difference | Visible business result | Key unknown |
|---|---|---|---|---|---|
| P01 | Anchor | E01, E03 | ... | ... | ... |

## Readiness Gates
| Gate | State | Evidence or named risk |
|---|---|---|
| Evidence | pass / fail / not proven / waived | ... |
| Product distinctness | pass / fail / not proven / waived | ... |
| Validation | pass / fail / not proven / waived | ... |
| Demonstrability | pass / fail / not proven / waived | ... |
| Portfolio execution | pass / fail / not proven / waived | ... |
| Mock honesty | pass / fail / not proven / waived | ... |
| Handoff | pass / fail / not proven / waived | ... |
| Stop boundary | pass / fail / not proven / waived | ... |
Overall verdict: READY / READY WITH RISKS / NOT READY

## Decision-Changing Risks And Unknowns
- <maximum five>
```

Keep `Fact`, `Operator interpretation`, `Product hypothesis`, and `Unknown` distinct. Every material
portfolio claim must link to an evidence label. Keep source excerpts minimal, redact unnecessary
customer details, and do not copy a private transcript into this artifact.

Use the gate states consistently:

- `READY`: every gate is `pass` and no named risk changes downstream execution;
- `READY WITH RISKS`: `Evidence`, `Product distinctness`, `Validation`, `Mock honesty`, `Handoff`, and
  `Stop boundary` are `pass`; `Demonstrability` is `pass` with a named execution risk, or `Portfolio
  execution` is `waived` by the operator, or another named risk remains without failing a gate;
- `NOT READY`: any required gate is `fail` or `not proven`, or a required gate other than `Portfolio
  execution` is `waived`.

Write the exact state and short evidence for every gate. Do not use descriptive substitutes such as
“mostly ready” or “acceptable.” A `READY WITH RISKS` bundle must name the risks that the operator must
acknowledge when assigning a Build Card downstream.

## 3. Downstream Build Cards

Write one independent file per proposition under `build-cards/`, named by stable ID such as `P01.md`.
Use [prototype-handoff.md](prototype-handoff.md) exactly. Each card links to `context-freeze.md` and
carries the internal verdict, all seven downstream gate states, and named risks required by the
downstream development skill.

The Build Cards are canonical for development scope. The product board is canonical for the short
human explanation. Do not make either artifact carry the other audience's detail.

## Product Proposition Test

A proposition is not a feature. It names a product mechanism that changes a business state for a
specific actor at a specific moment. Use this internal check:

> When **actor** reaches **business moment**, the product uses **distinct mechanism** to change
> **present state** into **observable result**, producing **business value**.

Reject a candidate when it is only:

- a feature extracted from the conversation;
- a generic AI capability with no business mechanism;
- a page, dashboard, chat, agent, canvas, report, plugin, or workflow shell;
- the same loop with a different layout, visual theme, role label, or amount of detail;
- an idea whose value requires an unproven production integration to be visible;
- an impressive animation that does not test a consequential assumption.

## Distinctness And Portfolio Test

Two propositions are materially distinct only when their product mechanism and customer-visible
result differ. In addition, at least two of actor, trigger, decision ownership, next action, or
business result should differ. Product form may support a distinction but does not establish one.

The portfolio should provide an evidence-grounded `Anchor`, a mechanism-level `Contrast`, and a
credible `Stretch` when the context supports it. Rank the internal sequence by evidence strength,
visible value, learning value, honest demonstrability, and complementarity. Do not use numeric scores
to manufacture precision or force ten weak ideas.

## Core Demo And Validation Test

Each proposition gets exactly one repeatable, two-minute-or-shorter causal moment:

```text
business input
-> one meaningful user action
-> distinct product mechanism
-> visible state change
-> recognizable business result
```

A page view, navigation tour, fake loading animation, static dashboard, or future-capability list does
not qualify. Name one largest unknown and one question that could change the product decision. Define
positive and negative observable signals before the prototype is shown; visual preference alone is
not product validation.

## Mock Boundary Test

Infrastructure may be mocked; the causal relationship under validation may not be mocked. Record in
every Build Card:

- `Real interaction`: behavior and state change that truly run in the prototype;
- `Synthetic data`: anonymized or invented business data;
- `Simulated intelligence`: precomputed recognition, agent, retrieval, or model output;
- `Not claimed`: production properties such as integration, accuracy, security, or persistence.

If a proposition promises that one correction changes a later decision, that correction and changed
result must actually happen in prototype state. A static success screen is insufficient.

## Response Contract

Return:

1. the complete, concise contents of `onsite-product-board.md`;
2. one line with the `context-freeze.md` path;
3. one line with the `build-cards/` path.

Do not repeat the internal context, gates, risks, or card details in the response. Think deeply in the
internal artifacts; let the operator and customer read the simple board.

## Post-Demo Response Contract

Append the full evidence to `context-freeze.md`, but return only this short human-facing structure:

```markdown
# 现场验证结果

一句话结论：<这轮演示让我们确认了什么>
建议下一步：<一个产品实验或商务动作>

## P01｜<产品名称>
- 现场反应：<一句可观察的反应，不扩写会议过程>
- 判断：继续 / 调整 / 暂停 / 未验证
- 下一步：<一个动作>
```

Repeat the three-line result block only for prototypes actually shown. Do not reproduce the evidence
index, gate analysis, full conversation, or long risk narrative in the response.
