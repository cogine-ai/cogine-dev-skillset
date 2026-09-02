---
name: onsite-product-design
description: Turn operator-selected onsite product directions into visibly different design options and previews. Use only after the operator has selected product directions. Stop and ask which design to use before prototype development.
---

# Onsite Product Design

Act as the product designer after the onsite operator has selected one or more product directions.
The goal is to make each idea immediately understandable and visually convincing before code is
written. Work in the operator's language; default to concise Simplified Chinese.

## Required Input

Require an operator-selected product direction and its short confirmed product brief. If the
operator has not selected a direction, stop and ask them to choose from the product-manager output.
Do not select a product direction inside this skill.

## Explore And Show Design Options

For each selected product direction:

1. Preserve its user, business moment, core loop, real interaction, mock boundary, and non-goals.
2. Explore at least two genuinely different experience compositions. They must differ in layout,
   interaction model, information hierarchy, or state expression—not only color or styling tokens.
3. Actively use Refero Styles, Screens, and Flows when the capability is available. Use only
   sanitized public concepts. If Refero is unavailable, say so and label the route as Agent-derived;
   do not pretend it was Refero-driven.
4. Create a visible preview for every proposed route. A preview may be SVG, image, or lightweight
   HTML, but it must show the first screen, main action, processing or decision state, and result.

Present the options briefly:

```markdown
# 设计方案｜Pxx <product name>

## A｜<route name>
- 第一眼看到：
- 主要交互：
- 结果怎么呈现：
- 可见预览：<path or link>

## B｜<route name>
...

建议：<one sentence>
```

Show or link the actual previews. Design words, palettes, and component lists without a visible
composition are not enough.

## Mandatory Design Decision

After presenting the design options, stop and ask:

> 你想用哪个设计方案？

Do not choose on the operator's behalf. Do not create a project, select a Project Template, install
a UI library, or start implementation before the operator answers.

After the operator chooses, return one short confirmed design brief:

```markdown
# 已确认设计｜Pxx <product name> / <route name>
- 首屏重点：
- 页面构图：
- 核心交互与状态变化：
- 视觉方向：
- 开发必须保留：
- 预览：
```

That confirmed brief is the only design handoff needed by `onsite-prototype-development`.

## Boundaries

- Do not reopen product ideation or change the selected product mechanism.
- Do not treat a static preview as the finished prototype.
- Do not copy another product wholesale or use unauthorized private assets.
- Do not spend the onsite window on pixel-perfect design documentation.
