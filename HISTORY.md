# Project History

> **Document role:** Narrative history of how Unsloop developed and why its scope changed. This file is descriptive, not normative. [`BRD.md`](BRD.md), [`PRD.md`](PRD.md), and [`FSD.md`](FSD.md) define current requirements and behavior; [`DECISIONS.md`](DECISIONS.md) records durable design choices; [`ROADMAP.md`](ROADMAP.md) records planned work; and Git remains the detailed change record.

## Origin

Unsloop began with a narrow but important concern: help writers identify generic, formulaic, over-polished, or source-dependent prose without pretending those patterns prove AI authorship. The original idea combined two related disciplines:

- writing-integrity review grounded in observable text, sources, attribution, and evidence; and
- human-voice review grounded in specificity, authorial presence, natural language, and the writer's actual choices.

The project name left room for a broader family—**Unsloop Review**, **Unsloop Write**, **Unsloop Audit**, and **Unsloop** as the umbrella—without requiring separate products immediately.

## Foundation and portability

The first implementation established a repository-local skill and then documented a portable system around it. The project directory became authoritative, with optional user-level and harness-specific links pointing back to the same source rather than creating divergent copies.

The core method remained model- and harness-agnostic. Codex support was preserved, while Claude, Pi, other Agent Skills clients, and generic text-capable harnesses received documented discovery or fallback paths. Markdown instructions and relative references remained the baseline; optional scripts and host metadata could improve operation without becoming runtime requirements.

This stage also established the traceable specification stack:

- the BRD explains the business need and boundaries;
- the PRD defines user-visible behavior and acceptance criteria; and
- the FSD defines functions, state, failure handling, and validation.

## From review to an author-led writing lifecycle

Unsloop grew from a checker into a writing system by preserving three stable public modes:

- **Unsloop Review** diagnoses an existing artifact constructively;
- **Unsloop Write** creates or revises writing under author-owned direction; and
- **Unsloop Audit** performs non-mutating, evidence-heavy examination.

New capabilities became specializations inside these modes rather than new top-level products. Progressive intake was added so Unsloop could determine whether the user already had a topic, wanted to refine a direction, or needed genuinely different ideas. The writing brief expanded to include the goal, audience, prior knowledge, context, governing directions, supplied content, evidence, voice, exclusions, and material constraints without forcing a redundant questionnaire.

Voice matching became evidence-based and bounded. Unsloop may request representative samples when close fidelity matters, but it separates observable language traits from the samples' facts, anecdotes, opinions, identity, and distinctive wording. Samples remain unpersisted by default, and every material fidelity claim identifies its basis, confidence, and limitations.

## Fiction from scenes through series

Fiction became a specialization within Unsloop Write rather than a fourth mode. The workflow scales from a one-off scene with a minimal conversational brief to novels, serials, and series with portable author-readable state.

Long-form fiction introduced creative contracts, Guided/Adaptive/Autonomous collaboration, scene and chapter planning, Confirmed/Proposed/Superseded canon, chronology, arcs, research separation, acceptance and rejection, branches, retcon impact analysis, recovery checkpoints, deterministic assembly, and model-agnostic resumption. Existing manuscripts and coherent layouts remain authoritative and are never reorganized silently.

Recurring characters gained separate, versioned personality and dialogue profiles. The author may define each character directly or review contextual proposals. Confirmed profiles govern tone, syntax, diction, cadence, worldview, relationship posture, and permitted contextual variation until the author explicitly approves an evolution or retroactive override.

## Sustained nonfiction, documentation, and evidence

The same portability principles expanded to books, theses, reports, courses, biographies, documentary narratives, procedures, policies, plans, instructions, technical documentation, and research syntheses. Persistent work can track authoritative versions, accepted sections, claims, sources, quotations, requirements, decisions, revision state, stakeholders, terminology, validation, and compact resume context.

Evidence acquisition gained User-provided only, Scoped web, Broad web, and Hybrid boundaries. Source suitability, verification, independence, confidence, overrides, and freshness remain separate. Unsloop also added specific lineage controls for quantitative evidence, interviews and oral histories, scans and OCR, images, audio, video, spreadsheets, and other transformed material.

Documentation was treated as an operated system rather than a one-time deliverable. Content architecture, canonical ownership, dependencies, reader journeys, corrections, deprecation, withdrawal, archival, maintenance triggers, and actual reader-validation methods became part of honest readiness.

## Audit became explicitly information-preserving

Unsloop Audit was strengthened into a non-mutating invariant. An audit may change the assessment of information, but it does not silently change the inspected artifact. Findings identify evidence and the smallest responsible proposal; any revision occurs later under a separately authorized scope.

This boundary protects claims, positions, conclusions, recommendations, scope, certainty, evidence strength, chronology, quantities, attribution, causality, conditions, exceptions, and exclusions. It also prevents stylistic cleanup, grammar correction, or smoother flow from becoming accidental permission to alter meaning.

Authorized revision later gained a related distinction: useful author-supplied observations, interpretations, unresolved questions, and tentative perspectives should be scoped and labeled honestly, not deleted merely because they lack external verification. Embedded externally checkable claims remain independently accountable.

## Structure, delivery, and multiple formats

The section-flow contract extended review beyond individual sentences. Unsloop now evaluates the preceding close, visible heading or break, and next opening as one logical boundary. It supplies the smallest useful orientation while preserving purposeful hard breaks and avoiding canned transitional sentences.

Delivery-aware writing then expanded the artifact boundary again. Speeches, presentations, narrated scripts, lessons, podcasts, demonstrations, and media-assisted work account for readings, pauses, questions, responses, interactions, setup, playback, observation, accessibility, and safety buffers—not manuscript word count alone.

For Markdown, DOCX, PDF, slides, web, audio, or other parallel formats, Unsloop distinguishes authoritative content from derivatives. A successful export is not treated as proof of synchronization, rendering, playback, accessibility, rehearsal, or platform readiness.

## Writing-pattern and assistance assessment

When users requested an “AI score,” Unsloop did not become an authorship detector. It developed a non-mutating Writing-Pattern and Assistance Audit that separates:

- directional writing-quality components;
- transparent textual measurements;
- authorized voice comparison;
- direct process provenance; and
- external detector reports.

Prose alone receives the boundary that AI authorship is not assessable from prose alone. No pattern score, measurement, voice mismatch, provenance record, or detector percentage is combined into a fabricated authorship probability.

## Style Direction and evolution

Style Direction extended Unsloop beyond voice matching without turning styles into canned presets. Authors can select:

- their evidenced personal voice;
- a historical or literary tradition;
- a custom-designed style; or
- a restrained genre default.

The system keeps author voice, narrative or document style, viewpoint voice, character dialogue, translation choices, and form or delivery conventions distinct. Historical and literary work records the relevant period, region, form, corpus, authenticity/readability stance, modernization policy, intentional anachronisms, evidence, and confidence. Early Modern English dramatic verse is one worked example, not the limit of the system.

Style can remain Stable, evolve Gradually, or change through approved Phases. Proposed changes cannot silently alter Confirmed style, and named-author requests are translated into high-level, non-exclusive traits rather than signature imitation.

## What remained constant

Unsloop's scope expanded, but its governing commitments did not:

- the author owns the goal, meaning, position, voice, canon, and consequential decisions;
- observable evidence controls factual, attribution, provenance, and authenticity claims;
- voice and style evidence never authorize importing facts, experiences, or identity;
- Audit remains separate from revision and preserves the inspected artifact;
- strong material is preserved unless there is a concrete reason and authority to change it;
- project state remains visible, portable, recoverable, and model-agnostic;
- polished output is not mislabeled as verified, tested, approved, synchronized, rehearsed, accessible, or publication-ready; and
- stylistic patterns never become unsupported claims about authorship, misconduct, identity, or authenticity.

## How Unsloop has been developed

The project has followed a repeatable iteration loop:

1. identify a real writing need or failure mode;
2. clarify the author-owned decision and evidence boundary;
3. define the business, product, and functional requirements;
4. add proportionate runtime guidance, templates, or optional tooling;
5. encode failure cases and behavioral scenarios;
6. validate portability, links, state rules, and regression behavior; and
7. commit the completed increment to the authoritative Git history.

This approach allowed Unsloop to grow substantially without accumulating disconnected modes or abandoning its original integrity-and-human-voice purpose.

## Milestone record

| Date | Commit | Milestone |
|---|---|---|
| 2026-08-12 | `1e295e5` | Initial Unsloop project. |
| 2026-08-12 | `12b036c` | Portable skill system and specification foundation. |
| 2026-08-13 | `cced192` | Scalable fiction writing workflow. |
| 2026-08-13 | `da07fb3` | Complete fiction operations and continuity workflow. |
| 2026-08-13 | `1c41845` | Sustained writing, documentation, research, and evidence expansion. |
| 2026-08-14 | `076ac84` | Information-preserving Audit invariant. |
| 2026-08-14 | `ad6c0e1` | Logical section-flow contract. |
| 2026-08-20 | `e4bd672` | Delivery-aware presentation workflow. |
| 2026-08-20 | `d6b7d21` | Full writing-lifecycle positioning and expanded audits. |
| 2026-08-21 | `f6bcd15` | Personal-perspective preservation during authorized revision. |
| 2026-08-21 | `8986d7d` | Governed Style Direction and stylistic evolution. |

The table records major capability milestones rather than every documentation-only adjustment. Use Git for the complete file-level history.

## Current identity

Unsloop is now a portable, model- and harness-agnostic writing lifecycle system. It supports planning, drafting, revision, review, non-mutating audit, research, validation, maintenance, delivery, and handoff across creative, factual, technical, documentary, spoken, and structured writing while preserving author control, traceable evidence, defensible voice and style, portable continuity, and honest readiness.
