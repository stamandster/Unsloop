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
| **Unsloop Audit** | Examine sources and evidence | Non-mutating, forensic, and explicitly bounded | “Compare this paper with these sources without changing it.” |

## Naming rules

- Use **Unsloop** when referring to the project, shared method, or core skill.
- Use the two-word mode names in user-facing prose.
- Reserve **Audit** for assessment that leaves the inspected artifact unchanged; call a later change **revision**, even when the user requests both in one workflow.
- Use lowercase hyphenated names for future skill folders: `unsloop-review`, `unsloop-write`, and `unsloop-audit`.
- Do not add new mode names for mere differences in depth. Use **brief**, **standard**, or **deep** as review-depth settings.
- Do not call a stylistic review an “AI detection” mode.
- Treat fiction as a workflow specialization within **Unsloop Write**, not as **Unsloop Fiction** or a fourth mode.
- Route fiction through **Unsloop Write**, **Unsloop Review**, or **Unsloop Audit** according to the requested job; “fiction” describes the specialization, not the mode.
- Use **story canon** for facts established inside fiction. Do not use “story bible” as the project-record name; `CANON.md` is topic-neutral and avoids a religious implication.
- Use **simulated reader response**, not “beta reader,” unless real beta-reader feedback is actually being analyzed.
- Treat sustained writing, provenance, revision control, collaboration, multilingual writing, and structured output as workflow specializations—not new Unsloop modes.
- Treat character voice continuity, documentary/documentation writing, and source acquisition as workflow specializations—not **Unsloop Character**, **Unsloop Documentary**, or **Unsloop Research** modes.
- Use **writing project** for persistent non-fiction state and **story project** for fiction state.
- Use **character voice profile** for a fictional speaker's author-approved personality and language contract; reserve **voice brief** or `VOICE.md` for the user's authorized author voice.
- Use **documentary narrative** for an evidence-led account and **documentation** or the specific form name for procedures, policies, plans, instructions, and technical artifacts.
- Use **source suitability** rather than permanently calling a website trusted or untrusted; use **source override** for an authorized inclusion, exclusion, or scope change.
- Use **skill composition** for shared authority across specialist skills; do not create a new public Unsloop mode for a domain or file format.
- Use **source safety** for untrusted-content isolation, **quantitative evidence** for reproducible numerical lineage, **interview evidence** for consent-controlled testimony, and **multimodal evidence** for original-to-derived transformations.
- Use **documentation system** for interconnected content with canonical ownership and dependencies; use **reader validation** only for the method actually performed, such as simulated hypothesis, automated check, expert review, or observed test.

## Split criteria

Keep the modes in the core `unsloop` skill until at least one of these is true:

- a mode needs materially different tools or permissions;
- its instructions cannot remain concise through progressive disclosure;
- its trigger language frequently activates the wrong workflow;
- users need to install or invoke it independently;
- forward-testing shows that separation improves reliability.

A split changes packaging and discovery, not the underlying integrity, voice, evidence, non-mutating Audit, or ethics contracts. Any proposed split must update the PRD, FSD, architecture, portability instructions, validator, and mode-specific acceptance tests together.
