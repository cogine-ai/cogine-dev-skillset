# Product Direction Playbook

Use this reference when the user asks for a full product-direction analysis, when the idea is complex, or when a concise answer needs a more rigorous checklist behind it.

## Mode Templates

### Anti-Inertia Mode

Use for early ideas, broad directions, unclear problem framing, or "does this have opportunity?"

Output:

1. 我先还原真实观察
2. 当前表达混合了哪些层级
3. 隐含假设
4. 最值得挑战的假设
5. 主流 / 反向 / 极简 / 未来路线
6. 第一用户 / 付费用户 / 未来用户
7. 交互位置 vs 执行位置
8. 最大非共识机会
9. 下一步验证建议

### Red Team Mode

Use when the user asks for critique, says not to be agreeable, or has a strong preferred direction.

Output:

1. 这个方向最可能错在哪里
2. 用户为什么可能不买
3. 竞品 / 平台 / 模型厂商如何绕过
4. 当前最可能高估什么
5. 当前最可能低估什么
6. 哪些指标会证明它错了
7. 如何降低风险
8. 替代路线

### Future Capability Projection Mode

Use for AI, Agent, automation, model capability, or frontier technology questions.

Output:

1. 当前能力边界
2. 3 个月变化假设
3. 6 个月变化假设
4. 12 个月变化假设
5. 因能力跃迁会变强的产品形态
6. 会被商品化 / 内置化的能力
7. 应提前保留的架构弹性
8. 建议押注方向

### Wedge Market Mode

Use when first users, first paid users, or market entry are unclear.

Output:

1. 候选用户群
2. 痛点强度
3. 高频程度
4. 付费可能
5. 容忍粗糙程度
6. 成败是否容易判断
7. 最小产品形态
8. 从楔子市场扩展到大市场的路径

### Minimal Kernel Mode

Use when the product is becoming too complex or platform-like.

Output:

1. 当前方案有哪些功能膨胀
2. 如果只能保留 3-5 个能力，应保留什么
3. 哪些功能只是包装
4. 哪些功能会拖慢验证
5. 极简版本如何产生价值
6. 极简版本的验证实验

### Architecture Mode

Use only after direction has converged, or after a short assumption check if the user explicitly asks for architecture.

Output:

1. 产品定义
2. 非共识优势
3. 系统分层
4. 核心抽象
5. 输入 / 输出协议
6. 工具 / 插件协议
7. 数据 / 记忆策略
8. 安全 / 合规 / 审计
9. 成本 / 延迟策略
10. MVP 范围
11. 风险与边界

### Portfolio Strategy Mode

Use when there are several plausible routes and the user needs a strategy rather than one answer.

Output:

1. 主航道
2. 探索线
3. 防御线
4. 共享底座
5. 哪些实验并行
6. 哪些决策暂缓
7. 哪些决策必须尽早锁定
8. 每条路线的退出条件

## Layer Split Table

Use this table to separate mixed product thinking:

| Layer | Meaning | Default treatment |
|---|---|---|
| 观察 | 用户实际看到的现象 | Usually preserve |
| 判断 | 用户对现象的解释 | Challenge |
| 方案 | 用户提出的解决方式 | Expand alternatives |
| 形态 | Web / CLI / API / Agent / SaaS 等 | Strongly challenge |
| 架构 | 模块、协议、系统边界 | Decide after convergence |
| 商业 | 目标用户、付费、分发 | Validate separately |

## Hidden Assumption Checklist

Cover these categories and mark the 2-3 most dangerous:

- 用户假设: who uses, who pays, who gives fast feedback?
- 场景假设: when and why does usage happen?
- 交互假设: where does the user interact?
- 执行假设: where does the AI or system act?
- 技术假设: what must be technically reliable now?
- 模型能力假设: what changes if models improve soon?
- 数据假设: what data, memory, permissions, or freshness is required?
- 分发假设: how are first users reached?
- 成本假设: model calls, storage, tool calls, human review, support.
- 合规 / 安全假设: PII, enterprise data, audit, approval, permission boundary.
- 竞争假设: incumbents, model vendors, open source, platform owners.
- 商业模式假设: who has budget, what ROI is legible, what sales motion works?

## Route Space

Always include at least four routes unless the user explicitly narrows scope:

| Route | Meaning |
|---|---|
| 主流路线 | The market-inertia version that most teams would build |
| 反向路线 | The route that contradicts the obvious form or assumption |
| 极简路线 | The smallest product that proves core value |
| 未来路线 | The route that improves as model/platform capabilities jump |

Optional route lenses:

- 开发者优先
- 非技术用户优先
- 本地执行
- 云端平台
- 开源
- 垂直场景
- API-first
- Marketplace / ecosystem
- Services-first to productize later

## Interaction vs Execution

For AI and Agent products, always fill both sides:

| Question | Options |
|---|---|
| 用户在哪里交互 | Web, mobile, CLI, IDE, browser extension, Slack, Discord, Teams, Feishu, WeChat, email, API, voice, daemon |
| AI / Agent 在哪里执行 | cloud, local filesystem, terminal, repo, browser, database, enterprise SaaS, sandbox, phone, message thread, edge device |

Most non-obvious opportunities come from the execution environment, not from the visible UI.

## Natural Infrastructure Examples

| Scenario | Natural infrastructure |
|---|---|
| Code Agent | git, shell, repo, tests, package manager |
| Document collaboration | version history, comments, permissions |
| Data analysis | notebook, CSV, SQL, charts |
| Enterprise workflow | tickets, approval, audit trail |
| Browser task | DOM, cookies, history, forms |
| Messaging assistant | channel, thread, mentions, bot identity |
| Design collaboration | canvas, layers, components, versions |
| Finance / transaction | ledger, transaction, reconciliation |

Use natural infrastructure for state, permissions, rollback, audit, and context before proposing a full custom platform.

## Capability Leap Projection

Evaluate 3, 6, and 12 month shifts:

| Capability | Product implication if it improves |
|---|---|
| Code ability | CLI, IDE, local execution, and repo agents become more useful |
| Tool-call stability | More autonomous execution and lower review burden |
| Multi-step planning | Longer workflows and delegated background tasks become viable |
| Long context | Project-level and organization-level context becomes more valuable |
| Multimodal understanding | Screen, image, document, and video agents become viable |
| Real-time voice | Meeting, always-on, and field-work assistants become stronger |
| Browser / screen operation | Web operators and personal workflow automation improve |
| Local environment operation | Local agents can use real files, commands, and private state |
| Memory / personalization | Continuous projects and personal work patterns become defensible |
| Cost / latency | High-frequency automation and background agents become economical |

After the table, state:

- Which routes become stronger.
- Which features are likely to be commoditized by model vendors or open source.
- Which architecture decisions should stay flexible.

## Minimal Kernel Test

Ask:

> 如果只能保留 3-5 个能力，这个产品还成立吗？

Then classify:

- 最小核心能力
- 表层包装能力
- 可以暂缓的能力
- 不做反而更好的能力
- 极简版本如何验证价值

For Agent products, a common minimal kernel is:

1. Read context.
2. Write or edit an artifact.
3. Execute a command, tool, or API call.
4. Ask for approval at the right boundary.

If those abilities cannot create value, connectors, dashboards, marketplaces, and admin panels will not rescue the product.

## Red-Team Questions

Answer these before recommending the direction:

- Why might this direction fail?
- Why might users not buy?
- Which success signals may be fake?
- How can incumbents copy or bypass it?
- Can model vendors make it a built-in feature?
- Can open source commoditize it?
- What is most likely overestimated?
- What is most likely underestimated?
- If this fails in six months, what is the most likely reason?

## Reversibility

| Decision type | Examples | Treatment |
|---|---|---|
| Reversible | UI style, copy, model vendor, local tools | Test quickly |
| Semi-reversible | RAG approach, plugin protocol, deployment shape, data retention | Be deliberate |
| High-cost / near-irreversible | target user, execution environment, core protocol, permission boundary, data model, business model | Debate early |

Spend the most time on decisions that are costly to reverse.

## Minimum Validation Experiment

Every recommendation should end with an experiment:

| Field | Question |
|---|---|
| Key assumption | What must be true? |
| Target user | Who exactly participates? |
| Smallest product form | What is the smallest thing they can use? |
| Key behavior | What behavior proves value? |
| Success metric | What observable threshold is enough? |
| Failure signal | What means the hypothesis is probably wrong? |
| Next unlock | What do we build or decide after learning? |

## Bias Checklist

Before answering, check:

- 是否默认做成 Web SaaS?
- 是否默认 AI 产品就是聊天界面?
- 是否默认知识问题一定要 RAG?
- 是否默认连接器越多越强?
- 是否过早进入平台化设计?
- 是否默认非技术用户就是第一批用户?
- 是否忽略开发者 / power user / 专业用户?
- 是否忽略 CLI、IDE、本地执行、浏览器插件、消息渠道?
- 是否只基于当前模型能力，而没有做 3/6/12 个月推演?
- 是否把完整架构当成高级，而忽略极简内核?
- 是否忽略开源项目、模型厂商、平台方的替代风险?
- 是否因为用户偏好某个方向而迎合?
- 是否把用户给出的产品形态当成不可挑战前提?
- 是否过早输出 API、模块、MVP，而没有先拆假设?

## Decision Heuristics

If the idea sounds like Web SaaS, ask whether it should instead be CLI, IDE plugin, browser extension, local daemon, messaging bot, API-first infrastructure, or service-assisted product.

If the idea sounds like a chatbot, ask what the AI executes, where state lives, what workspace it can change, what is auditable, and what can be rolled back.

If the idea sounds like RAG, ask whether knowledge is really in documents or instead in files, logs, commands, code, tickets, browser state, or database records. Ask whether vector search is necessary or dynamic environment reading is better.

If the idea sounds like a connector platform, ask whether prebuilt connectors are needed, whether AI-generated scripts/tools are enough, whether OpenAPI import is enough, whether first users tolerate custom scripts, and whether connector count is truly the moat.

If the idea sounds like an Agent platform, ask who the first high-frequency user is, where execution happens, what minimal toolset creates value, what natural infrastructure provides audit/rollback, and whether platformization is premature.

## Default Full Template

```markdown
## 1. 我先还原你的真实观察

...

## 2. 当前想法混合了哪些层级

| 层级 | 内容 | 是否需要挑战 |
|---|---|---|

## 3. 隐含假设

...

## 4. 最值得挑战的 3 个假设

...

## 5. 至少 4 条路线

| 路线 | 描述 | 优点 | 风险 | 适合的第一用户 |
|---|---|---|---|---|

## 6. 第一用户 / 付费用户 / 未来大众用户

...

## 7. 用户在哪里交互，AI 在哪里执行

...

## 8. 模型能力跃迁推演

...

## 9. 红队意见

...

## 10. 最小验证实验

...

## 11. 如果方向收敛，下一步再进入架构
```
