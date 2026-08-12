# Design Decisions

## D-001 — Use Unsloop as the umbrella name

**Status:** Accepted for v0.1

Use **Unsloop** for the project and core skill. Reserve **Unsloop Review**, **Unsloop Write**, and **Unsloop Audit** as clear modes and possible future skill names.

## D-002 — Build one extensible skill first

**Status:** Accepted for v0.1

Keep the three modes in one repo-local skill while the method is still being tested. Split them only when observed workflows justify it.

## D-003 — Separate integrity from voice

**Status:** Accepted

Run two lenses. The integrity lens evaluates sources, attribution, evidence, and dependence. The voice lens evaluates specificity, authorial presence, redundancy, formulaicity, abstraction, and rhetorical padding.

## D-004 — Do not classify AI authorship from style

**Status:** Accepted

Report concrete textual patterns. Never turn those patterns into a claim that a passage is AI-generated.

## D-005 — Keep source dependence separate from plagiarism

**Status:** Accepted

Use a dedicated source-dependence scale because wording overlap alone misses retained syntax, idea order, detail selection, and rhetorical architecture.

## D-006 — Use directional score families

**Status:** Accepted for v0.1; requires validation

Score positive qualities and risk qualities separately so “5” does not silently change meaning within one total:

- Strengths: specificity, authorial voice, source independence; higher is better.
- Risks: redundancy, formulaicity, abstraction; higher is worse.
- Source dependence: a separate 1–5 risk scale; higher means stronger dependence.

Do not combine them into one authoritative number.

## D-007 — Preserve good prose

**Status:** Accepted

Every standard or deep review identifies what should remain unchanged. Revision is opt-in unless the user explicitly asks for rewriting.

## D-008 — Keep the canonical skill repository-scoped

**Status:** Accepted

Store the canonical skill at `.agents/skills/unsloop`, the repository discovery location supported by Codex. Do not require installation into a user's home directory. Keep every operational reference relative and keep validation tooling inside the project.

## D-009 — Make voice matching evidence-based and bounded

**Status:** Accepted

Allow Unsloop to request representative writing the user authored or is authorized to provide. Derive a bounded profile from observable traits, keep sample style separate from sample content, follow current instructions over older samples, and report basis, confidence, and limits. Do not claim exact imitation, infer identity, or persist samples without explicit authorization.

## D-010 — Use a progressive writing brief

**Status:** Accepted

Before substantial work, extract topic, goal, audience, prior knowledge, context, required content, exclusions, reference material, voice target, and format constraints from what the user already supplied. Mark consequential fields as known, inferred, or unknown. Ask only about gaps that could materially change the result, state consequential assumptions, and keep factual references separate from voice samples.

## D-011 — Branch on topic status first

**Status:** Accepted

At the beginning of new writing, determine whether the user has an existing topic, wants to refine a rough direction, or wants to brainstorm from scratch. Skip the question when the topic is already explicit. Brainstorm distinct, feasible options from minimal seed context, explain their angle and evidence needs, and continue the writing brief only after a topic is selected or approved.

## D-012 — Use capability-aware structured questions

**Status:** Accepted

Use Codex's structured user-input control when it is available and a consequential question has two or three mutually exclusive choices. Keep recommendations contextual, ask no more than three questions at once, and use ordinary conversation for open-ended material. When the control is unavailable, preserve the same choices in a concise plain-text fallback. Never change collaboration mode solely to obtain the preferred interface.
