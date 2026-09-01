# Design Output Bundle Contract

Produce one design bundle for one complete upstream comparison batch.

```text
<design-output-directory>/
  onsite-design-board.md
  design-context.md
  design-cards/
    P01.md
    P02.md
    ...
  previews/
    P01.*
    P02.*
    ...
```

## 1. Human-Facing Design Board

Write `onsite-design-board.md` in the operator's language; default to concise Simplified Chinese.
Use this exact structure:

```markdown
# 现场设计方向

状态：可以进入开发 / 等待确认 / 产品材料待补充 / 设计材料待补充
一句话判断：<这批设计怎样帮助老板看懂不同产品价值>
组合差异：<一句话说明不是同一套页面换皮>

## P01｜<产品名>｜<设计路线名>
- 产品形态：<工作台 / 流程 / 画布 / Dashboard / 插件 / 报告等实际形态>
- 第一眼：<老板最先看到什么，以及为什么>
- 核心画面：<主要对象、信息层级和构图>
- 关键交互：<动作、处理反馈、状态变化和结果>
- 设计识别点：<一个非颜色、字体或圆角层面的设计决定>
- 可见预览：<相对路径或可访问链接>
```

Repeat the six-field block for every product card. Apply these rules:

- show exactly one recommended route per product;
- keep every field to one short sentence;
- do not expose gate tables, rejected routes, long rationale, token lists, or technical choices;
- do not describe a preview as clickable or working unless it actually is;
- use customer and business language instead of design jargon where possible;
- include every product card in the comparison batch.

Map internal state to the board:

- `DESIGN READY` -> `可以进入开发`;
- `AWAITING DESIGN DECISION` -> `等待确认`;
- `PROVISIONAL - PRODUCT BLOCKED` -> `产品材料待补充`;
- `DESIGN NOT READY` -> `设计材料待补充`.

## 2. Internal Design Context

Use this structure for `design-context.md`:

```markdown
# Design Context

Design freeze ID:
Source product freeze path and ID:
Comparison batch ID:
Source product verdict and acknowledged risks:
Build Card paths and IDs:
Design sources available:
Operator design constraints:
Time boundary:

## Research Evidence
| ID | Source type | Exact reference or fallback artifact | Bounded role |
|---|---|---|---|
| D01 | Approved system / Refero Style / Refero Screen / Refero Flow / Other / Agent fallback | ... | ... |

## Portfolio Design Judgment
| Card | Selected route | Product-design fit | Non-token consequence | Nearest route and material difference | Preview |
|---|---|---|---|---|---|
| P01 | ... | ... | ... | ... | ... |

## Rejected Alternatives
- P01: <route> — <one material reason it lost>

## Readiness Gates
| Gate | State | Evidence or named risk |
|---|---|---|
| Upstream product | pass / fail / not proven / waived | ... |
| Visible evidence | pass / fail / not proven / waived | ... |
| Product-design fit | pass / fail / not proven / waived | ... |
| Portfolio design distinctness | pass / fail / not proven / waived | ... |
| State completeness | pass / fail / not proven / waived | ... |
| Reference lock | pass / fail / not proven / waived | ... |
| Mock honesty | pass / fail / not proven / waived | ... |
| Decision | pass / fail / not proven / waived | ... |
| Handoff | pass / fail / not proven / waived | ... |
| Stop boundary | pass / fail / not proven / waived | ... |
Overall state: DESIGN READY / AWAITING DESIGN DECISION / PROVISIONAL - PRODUCT BLOCKED / DESIGN NOT READY

## Operator Decision
<actual confirmation, concise correction, or explicit delegation; never Agent-authored approval>

## Risks And Unknowns
- <maximum five>
```

Keep source material anonymized. A Refero tool call, URL list, or completed field does not establish a
passing gate without visible evidence and a target consequence.

## 3. Design Cards

Write one independent `design-cards/Pxx.md` for every Build Card, using the same stable ID:

```markdown
# Design Card - <Pxx And Product Name>

- Sources: <Build Card path>; <product freeze path and ID>; <design-context path and design freeze ID>; <batch ID and card ID>
- Upstream states: <product verdict and risks>; <design overall state>; <required design gates>
- Fixed product: <actor + business moment + product mechanism + visible result>; <core loop reference>
- Selected design route: <name>; <product form and experience topology>; <why it fits>
- Visible preview: <path or accessible link>; <what state it shows>; <design-evidence label>
- Reference lock: <primary exact source or fallback>; <bounded secondary source and role or none>
- First-screen attention order: <first -> second -> third>
- State map: <entry -> action -> processing/decision -> result -> reset>
- Composition and hierarchy: <regions, main business object, primary action, result emphasis>
- Interaction choreography: <feedback, transition, control, correction, and reset behavior>
- Non-token consequence: <observable design decision tied to the business moment>
- Visual roles: <type/density/spacing>; <semantic color roles>; <component/media character>
- Reference mappings: <trait -> business reason -> target state consequence>
- Explicit rejects and reskin counterfactual: <rejects>; <what remains without surface tokens>
- Must preserve and acceptance: <critical content/behavior presentation>; <visible acceptance checks>
- Operator decision and development eligibility: <actual confirmation or delegation>; <DESIGN READY / BLOCKED with reason>
```

Each Design Card must be understandable with its Build Card and linked freezes, without private
meeting text or new design invention by the developer. Keep it to 20 lines or fewer by combining
related facts as shown.

The Build Card remains authoritative for what is built and validated. The Design Card is
authoritative for how that product experience is composed, behaves visually, and communicates its
state. A Design Card must not alter the product mechanism, mock boundary, validation question, or
non-goals.

Only a card whose final field says `DESIGN READY` may enter `onsite-prototype-development`.

## Response Contract

Return:

1. the complete concise contents of `onsite-design-board.md`;
2. the actual preview for every Pxx rendered inline when supported, otherwise one clickable exact
   preview link per Pxx;
3. one line with the `design-context.md` path;
4. one line with the `design-cards/` path;
5. one line with the `previews/` path.

Do not dump internal alternatives, evidence tables, gates, or full Design Cards into the response.

## Post-Build Portfolio Review

When the skill is explicitly used in post-build portfolio QA mode, write only one additional file:

```markdown
# Portfolio Runtime Review

Design freeze ID:
Comparison batch ID:

| Card | Actual run and screenshots | Own-route fidelity | Nearest-route runtime difference | State |
|---|---|---|---|---|
| P01 | ... | pass / drift / not proven | ... | pass / drift / not proven |

Overall state: PORTFOLIO READY / PORTFOLIO DRIFT / PORTFOLIO NOT PROVEN

## Required Corrections
- <Pxx: smallest failed Design Card acceptance check, or none>
```

Return the short table, overall state, required corrections, and the exact file path. Do not rewrite
the pre-development Design Cards or create new routes in this mode.
