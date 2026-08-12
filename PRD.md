# Product Requirements Document

> **Product:** Unsloop · **Status:** v0.1 baseline
>
> **Upstream:** [`BRD.md`](BRD.md)
>
> **Downstream:** [`FSD.md`](FSD.md)

## Product definition

Unsloop is one writing-integrity and human-voice skill with three modes:

- **Unsloop Review:** diagnose an existing draft constructively and selectively.
- **Unsloop Write:** draft or revise from an author-led brief while preserving evidenced voice.
- **Unsloop Audit:** perform an evidence-heavy comparison of writing, requirements, claims, sources, or a similarity report.

Review is the default for a broad request about existing writing. Depth—brief, standard, or deep—is independent of mode.

## Product principles

1. Judge observable writing and evidence, not presumed authorship or intent.
2. Diagnose before rewriting and preserve material that already works.
3. Ask only for information that could materially change the result.
4. Keep directions, factual evidence, and voice evidence separate.
5. Match voice through authorized, observable patterns—not identity claims or copied language.
6. State evidence limits, uncertainty, and readiness honestly.
7. Keep the project directory authoritative and portable.
8. Preserve one model- and harness-agnostic method; isolate discovery, invocation, metadata, and tool mappings as optional adapters.

## Primary use cases

| Use case | User input | Expected result |
|---|---|---|
| Review a draft | Draft plus optional brief and sources | Prioritized diagnosis, preserved strengths, and revision only if requested. |
| Draft new writing | Topic or topic path, purpose, audience, content, constraints, and optional voice samples | Requested artifact with material assumptions and limitations disclosed. |
| Revise in the user's voice | Draft, requested changes, and sufficient voice evidence | Meaning-preserving revision plus basis and confidence when fidelity is material. |
| Audit source use | Draft, sources or similarity report, and governing requirements | Evidence boundary, source map, claim checks, requirement coverage, and calibrated conclusion. |
| Brainstorm a topic | Interests or subject area, purpose, audience, and constraints | Distinct feasible options with angles, reader value, scope, and evidence needs. |

## Functional requirements

| ID | Product requirement | Business requirements |
|---|---|---|
| PR-001 | Select Review, Write, or Audit from the request; default broad draft review to Review and scale depth proportionately. | BR-006, BR-009 |
| PR-002 | For new writing, use an explicit topic when supplied; otherwise offer existing-topic, refine-direction, or brainstorm paths. | BR-003, BR-004 |
| PR-003 | Build a progressive brief covering topic, goal, audience, prior knowledge, context, governing directions, content roles, exclusions, references, voice target, and constraints. Mark material fields Known, Inferred, or Unknown. | BR-003, BR-004, BR-009 |
| PR-004 | Resolve direction priority; distinguish required, optional, background-only, and excluded content; distinguish hard constraints, working targets, allocations, and safety buffers. | BR-004, BR-012 |
| PR-005 | State the evidence boundary whenever it limits a conclusion, and separate the writing brief, factual evidence, voice samples, and verification status. | BR-001, BR-005, BR-007 |
| PR-006 | Review source relationships across wording, syntax, idea order, detail selection, and rhetorical architecture; classify supported relationships precisely. | BR-001, BR-005 |
| PR-007 | Review specificity, authorial presence, consistency, redundancy, formulaicity, abstraction, example function, emotional integrity, and useful irregularity without classifying AI authorship. | BR-002, BR-007 |
| PR-008 | When close voice fidelity matters, request representative authorized writing if evidence is thin; build a bounded voice brief, separate style from content, and report basis and confidence. | BR-002, BR-003, BR-007, BR-011 |
| PR-009 | Rank findings by consequence and confidence, identify material to preserve, rewrite only when requested, and apply an honest readiness label when unresolved matters affect use. | BR-003, BR-009, BR-012 |
| PR-010 | Score only on request or when it materially aids comparison; keep strength and risk families separate, use N/A when unsupported, and explain every score with evidence. | BR-005, BR-009 |
| PR-011 | When verification is requested, prefer the original source, inspect relevant context, report access status, and never represent partial access as full verification. | BR-001, BR-005, BR-007 |
| PR-012 | Use a structured choice control for two or three consequential mutually exclusive options when the active harness provides one; otherwise preserve the same decision in concise plain text without changing the host's collaboration or execution mode. | BR-003, BR-004, BR-013 |
| PR-013 | Enforce privacy, minimization, authorization, evidence, identity, emotional-integrity, and high-stakes human-review limits. | BR-005, BR-007, BR-011 |
| PR-014 | Operate from repository-local Markdown/YAML with relative links and no required service or package; support optional repository, user, or admin discovery through links or copies of the authoritative project skill. | BR-008, BR-010, BR-013 |
| PR-015 | Keep the operational core compliant with the portable Agent Skills shape and independent of vendor tool names, model IDs, invocation syntax, or proprietary frontmatter. Provide capability-based fallbacks and optional adapters for Codex, Claude, Pi, and other hosts. | BR-008, BR-010, BR-013 |

## Nonfunctional requirements

| ID | Requirement | Acceptance signal |
|---|---|---|
| NFR-001 Portability | The complete operational skill travels with the repository and contains no machine-specific operational path. | A copied or cloned project validates and the skill is discoverable below the repo root. |
| NFR-002 Reliability | Normative contracts are internally linked and checked by a dependency-free validator. | `python scripts/validate.py` passes. |
| NFR-003 Transparency | Material findings distinguish observation, supported inference, unverified concern, and out-of-scope judgment. | Output labels and evidence boundary are present when material. |
| NFR-004 Privacy | Voice samples and profiles are not persisted or externally transferred without explicit authorization. | Operational instructions prohibit default persistence and unnecessary reproduction. |
| NFR-005 Maintainability | The core skill remains concise; detailed procedures use one-level-deep references; project specifications stay outside the runtime bundle. | Skill validation passes and no auxiliary project docs are added inside the skill. |
| NFR-006 Accessibility | The workflow remains usable without a special UI control, external service, or scoring model. | Plain-text fallback and score-free review both remain defined. |
| NFR-007 Interoperability | The same `SKILL.md` and relative references run across standards-compatible text-capable models and harnesses; host metadata and discovery links remain optional. | Core validation passes independently of Codex metadata, and documented Codex, Claude, Pi, and generic adapter paths all resolve to the same core. |

## Interaction requirements

### Intake

- Reuse information already present; do not ask the user to repeat it.
- Ask the smallest useful question batch and normally no more than three structured questions at once.
- Use open conversation for topics, drafts, sources, context, and samples that cannot be reduced safely to fixed options.
- Pause only when a missing fact, authorization, source, or high-stakes choice cannot be inferred responsibly.
- Map semantic needs to the active harness's native capabilities and use the documented fallback when a tool is absent.

### Voice-sample request

When a closer match materially affects the result and evidence is weak, request two or three representative samples, preferably in the same genre and roughly 500–2,000 words total. If the user declines, continue where safe with a lower confidence label.

### Output

- Put the requested writing first in Write mode unless process notes were requested.
- In Review, lead with the overall assessment and highest-value findings.
- In Audit, include the evidence boundary before source-dependent conclusions.
- Keep findings passage-specific and corrections proportionate.
- Do not add scores, tables, or readiness labels when they would add ceremony rather than value.

## Acceptance criteria by workflow

### Review

Given an existing draft and a broad review request, Unsloop selects Review, infers the apparent brief, identifies the most consequential integrity and voice findings, preserves sound prose, states material evidence limits, and does not rewrite unless asked.

### Write

Given a clear topic and sufficient brief, Unsloop does not repeat the topic question, drafts toward the stated reader outcome, respects content roles and hard constraints, checks source-based claims and human voice, and discloses material assumptions or readiness limits.

### Audit

Given a draft and comparison sources, Unsloop records exactly what was inspected, maps supported textual relationships and claims, separates requirement satisfaction from source support, identifies unresolved checks, and does not infer intent or misconduct.

### Voice fidelity

Given authorized representative samples, Unsloop derives only observable task-relevant traits, does not import sample facts or memorable wording, adapts for the new genre and audience, and reports the basis and Low, Moderate, or High confidence when fidelity is material.

### Portability

Given a clean copy of the repository, the project validator passes without network access or third-party packages. Codex and Pi can use the canonical `.agents/skills` core directly; Claude and other hosts can link or load the same directory through their discovery adapters. Every linked entry resolves to the project skill rather than a divergent copy.

### Harness and model independence

Given a supported harness and any text-capable model with adequate context for the task, Unsloop follows the same evidence, voice, output, and ethics contracts. Missing structured input, browsing, file editing, memory, or token-counting capabilities trigger explicit fallbacks or narrower evidence claims—not a different method. Output quality may vary by model and available tools, and Unsloop does not claim otherwise.

## Release criteria

The v0.1 product baseline requires:

- complete BRD-to-PRD-to-FSD traceability;
- valid standard skill frontmatter and valid optional Codex UI metadata;
- working relative Markdown links;
- project-local validation with no unresolved placeholders;
- project-authoritative Codex, shared Agent Skills, Claude, and Pi linking with collision protection;
- explicit disclosure that scoring is interpretive and not empirically validated.

Calibration, benchmark fixtures, inter-reviewer agreement, privacy review, and mode-split evidence remain later release work in [`ROADMAP.md`](ROADMAP.md).

## Detailed normative documents

- [`docs/REVIEW-MODEL.md`](docs/REVIEW-MODEL.md)
- [`docs/SCORING-RUBRIC.md`](docs/SCORING-RUBRIC.md)
- [`docs/REVIEW-OUTPUT.md`](docs/REVIEW-OUTPUT.md)
- [`docs/ETHICS-AND-LIMITS.md`](docs/ETHICS-AND-LIMITS.md)
- [`docs/NAMING.md`](docs/NAMING.md)
