# Design Decisions

> **Document role:** Accepted architectural and product tradeoffs. Requirement authority remains in [`BRD.md`](BRD.md), [`PRD.md`](PRD.md), and [`FSD.md`](FSD.md).

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

Store the canonical skill at `.agents/skills/unsloop`, a repository discovery location supported by Codex, Pi, and the Agent Skills ecosystem. Do not require installation into a user's home directory. Keep every operational reference relative and keep validation tooling inside the project.

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

Use the active harness's structured user-input control—including Codex's control—when it is available and a consequential question has two or three mutually exclusive choices. Keep recommendations contextual, ask no more than three questions at once, and use ordinary conversation for open-ended material. When the control is unavailable, preserve the same choices in a concise plain-text fallback. Never change the host's collaboration or execution mode solely to obtain the preferred interface.

## D-013 — Generalize production discipline without domain coupling

**Status:** Accepted

Strengthen Unsloop with reusable controls observed in mature writing workflows: governing-direction hierarchy, audience concerns and desired response, required/optional/background/excluded content roles, hard versus working constraints, compact decision briefs, requirement coverage, functional-example review, emotional-integrity review, and readiness labels. Keep domain-specific doctrine, terminology, timing formulas, and artifact rules in their owning skills.

## D-014 — Expose the project skill globally through one filesystem link

**Status:** Accepted

Keep `.agents/skills/unsloop` authoritative. When user-wide availability is wanted, link the selected Codex, shared Agent Skills, Claude, or Pi entry to that directory instead of copying it. Preserve Codex as the utility's default behavior. Provide a project-owned, idempotent utility that validates every target and refuses to overwrite unrelated content.

## D-015 — Use a three-level specification stack

**Status:** Accepted

Use a BRD for business intent and boundaries, a PRD for user-visible requirements and acceptance criteria, and an FSD for operational behavior, data concepts, validation, and test traceability. Keep these maintainer documents at the repository root, outside the runtime skill, so the skill remains concise. Treat the project directory as authoritative and use requirement IDs to connect the levels without duplicating full procedures.

## D-016 — Separate the portable core from harness adapters

**Status:** Accepted

Keep `SKILL.md`, standard frontmatter, and relative references model- and harness-agnostic. Treat discovery paths, invocation syntax, UI metadata, and tool names as adapters. Preserve the existing Codex adapter and global link; add Claude, Pi, and shared Agent Skills paths without copying or forking the method. When a capability is absent, use an explicit fallback and narrow the evidence boundary rather than changing the governing rules.

## D-017 — Keep fiction inside Write and make its state author-owned

**Status:** Accepted

Support every fiction form—from an isolated scene through a series—as a progressively loaded specialization of **Unsloop Write**, not a fourth mode. Scale intake and files to the work; use Guided, Adaptive, or Autonomous collaboration with Adaptive as the default; and preserve locked author decisions in every cadence.

For persistent fiction, use visible author-approved Markdown under `story/` and `manuscript/`, adopt coherent existing layouts, distinguish Proposed, Confirmed, and Superseded canon, and require explicit retcons. Use `story/STATUS.md` as a model-agnostic resume packet. Treat story canon as fictional state rather than real-world evidence, and keep author, narrative, viewpoint, and dialogue voice targets distinct.

## D-018 — Route fiction across the existing modes

**Status:** Accepted

Load the fiction workflow for every fiction request, then use Write for creation and packaging, Review for constructive manuscript diagnosis, and Audit for evidence-heavy project, continuity, research, or source comparison. Do not create a fourth fiction mode.

## D-019 — Make consequential fiction changes recoverable

**Status:** Accepted

Define explicit project, manuscript-unit, canon, batch, and branch states. Partial acceptance updates only the accepted scope. Require an impact map, explicit approval, and a recoverable checkpoint before retcons or large revisions. Preserve Superseded canon and keep rejected or abandoned details out of active state.

## D-020 — Bundle optional templates and fail-closed tooling

**Status:** Accepted

Provide author-readable Markdown templates and a standard-library project command for initialization, structural checking, checkpoints, and accepted-unit assembly. Keep the command optional, default mutation-capable actions to dry-run, require explicit application, confine paths to the chosen project, and refuse overwrites. Manual Markdown operation remains the portable baseline.

## D-021 — Bound fiction feedback and publication claims

**Status:** Accepted

Offer focused fiction review and publication-support workflows while distinguishing simulated reader hypotheses from real feedback, authenticity questions from community authority, and manuscript preparation from professional, legal, market, representation, publisher, or publication certification.
