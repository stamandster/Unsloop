# Naming System

> **Specification role:** Normative naming sub-specification for the mode model in [`../PRD.md`](../PRD.md) and mode selection in [`../FSD.md`](../FSD.md). Naming changes that alter scope also require a business review in [`../BRD.md`](../BRD.md).

## Umbrella name

**Unsloop** is the main project and shared method.

The name covers the whole cycle: inspect source use, remove formulaic loops, recover the writer's point, and keep the result accountable.

## Mode names

| Name | Primary job | Default posture | Typical request |
|---|---|---|---|
| **Unsloop Review** | Diagnose a draft | Constructive and selective | “Review this without rewriting it.” |
| **Unsloop Write** | Draft or revise | Author-led and voice-preserving | “Rewrite this in my voice.” |
| **Unsloop Audit** | Examine sources and evidence | Forensic and explicitly bounded | “Compare this paper with these sources.” |

## Naming rules

- Use **Unsloop** when referring to the project, shared method, or core skill.
- Use the two-word mode names in user-facing prose.
- Use lowercase hyphenated names for future skill folders: `unsloop-review`, `unsloop-write`, and `unsloop-audit`.
- Do not add new mode names for mere differences in depth. Use **brief**, **standard**, or **deep** as review-depth settings.
- Do not call a stylistic review an “AI detection” mode.
- Treat fiction as a workflow specialization within **Unsloop Write**, not as **Unsloop Fiction** or a fourth mode.
- Route fiction through **Unsloop Write**, **Unsloop Review**, or **Unsloop Audit** according to the requested job; “fiction” describes the specialization, not the mode.
- Use **story canon** for facts established inside fiction. Do not use “story bible” as the project-record name; `CANON.md` is topic-neutral and avoids a religious implication.
- Use **simulated reader response**, not “beta reader,” unless real beta-reader feedback is actually being analyzed.

## Split criteria

Keep the modes in the core `unsloop` skill until at least one of these is true:

- a mode needs materially different tools or permissions;
- its instructions cannot remain concise through progressive disclosure;
- its trigger language frequently activates the wrong workflow;
- users need to install or invoke it independently;
- forward-testing shows that separation improves reliability.

A split changes packaging and discovery, not the underlying integrity, voice, evidence, or ethics contracts. Any proposed split must update the PRD, FSD, architecture, portability instructions, validator, and mode-specific acceptance tests together.
