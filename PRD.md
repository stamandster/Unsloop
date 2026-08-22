# Product Requirements Document

> **Product:** Unsloop · **Status:** v0.1 baseline
>
> **Upstream:** [`BRD.md`](BRD.md)
>
> **Downstream:** [`FSD.md`](FSD.md)

## Product definition

Unsloop is one portable, model-agnostic writing-lifecycle skill with three modes:

- **Unsloop Review:** diagnose an existing draft constructively and selectively.
- **Unsloop Write:** draft or revise from an author-led brief while preserving evidenced voice.
- **Unsloop Audit:** perform a non-mutating, evidence-heavy comparison of writing, requirements, claims, sources, or a similarity report.

Review is the default for a broad request about existing writing. Depth—brief, standard, or deep—is independent of mode.

Topic discovery, Style Direction and evolution, fiction, sustained non-fiction, documentary and controlled documentation, research, collaboration, multilingual work, delivery, structured output, and writing-pattern or assistance audit are specializations inside the three modes, not separate public products. Formulaic-writing review remains a useful capability, but it does not define Unsloop's category.

Fiction is a specialization within Unsloop Write, not a fourth mode. It supports isolated scenes, flash fiction, short stories, novellas, novels, serials, and series across any user-chosen subject or genre.

## Product principles

1. Judge observable writing and evidence, not presumed authorship or intent.
2. Diagnose before rewriting and preserve material that already works.
3. Ask only for information that could materially change the result.
4. Keep directions, factual evidence, and voice evidence separate.
5. Match voice through authorized, observable patterns—not identity claims or copied language.
6. State evidence limits, uncertainty, and readiness honestly.
7. Keep the project directory authoritative and portable.
8. Preserve one model- and harness-agnostic method; isolate discovery, invocation, metadata, and tool mappings as optional adapters.
9. Treat live delivery, audience attention, media, and required derivatives as part of the artifact when they affect actual use.
10. Support the writing lifecycle from topic discovery through maintenance and handoff; do not reduce Unsloop to a checker, detector, or rewriting filter.
11. Resolve how persistent writes should be retained before the first write when the project or request has not already established a policy.

## Primary use cases

| Use case | User input | Expected result |
|---|---|---|
| Review a draft | Draft plus optional brief and sources | Prioritized diagnosis, preserved strengths, and revision only if requested. |
| Draft new writing | Topic or topic path, purpose, audience, content, constraints, and optional voice samples | Requested artifact with material assumptions and limitations disclosed. |
| Revise in the user's voice | Draft, requested changes, and sufficient voice evidence | Meaning-preserving revision plus basis and confidence when fidelity is material. |
| Audit source use | Draft, sources or similarity report, and governing requirements | Unchanged inspected artifact, evidence boundary, source map, claim checks, requirement coverage, calibrated conclusion, and separately proposed corrections. |
| Brainstorm a topic | Interests or subject area, purpose, audience, and constraints | Distinct feasible options with angles, reader value, scope, and evidence needs. |
| Develop fiction | Story seed, premise, notes, outline, or manuscript plus author decisions | A proportionate path from discovery through planning, drafting, continuity, revision, and handoff. |
| Continue a fiction project | Existing manuscript and project records | Work resumed from accepted canon and current state without silently overwriting the author's layout or decisions. |
| Onboard an existing manuscript | Existing manuscript, notes, outlines, versions, and optional records | Proposed portable state extracted with locations and confidence, confirmed before creation or promotion. |
| Review or audit fiction | Manuscript boundary, intended experience, project stage, optional records and research | A focused developmental, craft, continuity, integrity, or authenticity assessment with preserved strengths and bounded claims. |
| Revise consequential story state | Accepted manuscript and proposed structural or canon change | Impact map, explicit decision, recoverable checkpoint, dependency-ordered revision, and reconciled state. |
| Assemble and package fiction | Accepted manuscript units and supplied submission requirements | Deterministic assembly or support artifact with explicit readiness and evidence limits. |
| Develop sustained non-fiction | Existing or new book, thesis, report, course, documentation set, policy, or research synthesis | Proportionate portable state, accepted manuscript units, bounded resume context, and recoverable handoff. |
| Maintain research provenance | Claims, sources, quotations, manuscript locations, and verification access | Inspectable support, conflict, freshness, and required-action records separated from citation formatting. |
| Control revision | Authoritative artifact, requested scope, protected material, and proposed changes | Classified, impact-aware, partially acceptable, recoverable changes without silent scope expansion. |
| Reconcile collaborators | Multiple directions, comments, roles, and approval authorities | Consolidated feedback, surfaced conflicts, decision ownership, and version-bounded approval state. |
| Translate or localize | Source artifact, target language or locale, audience, terminology, and evidence | Meaning- and evidence-preserving adaptation with explicit ambiguity, quotation, voice, and cultural limits. |
| Return structured results | Requested mode, artifact, evidence, and supplied or default schema | Machine-readable findings that preserve evidence, confidence, readiness, privacy, and human-readable meaning. |
| Select or evolve a Style Direction | Purpose, form, audience, optional period or tradition, desired reader experience, and optional evidence corpus | A confirmed `StyleBrief`, explicit channel boundaries, authenticity stance, evolution model, and evidence-bounded application or review. |
| Sustain a fictional cast | Character decisions, context, manuscript, and optional author-approved changes | Distinct versioned personality and speech profiles, drift review, and controlled evolution without silent mutation. |
| Develop documentary or controlled documentation | Topic, intended use, authority, supplied evidence and/or approved research scope | A form-specific biography, documentary, procedure, policy, plan, direction, instruction, or technical artifact with traceable evidence and validation status. |
| Combine Unsloop with another skill | Shared request, active skills, governing specifications, and authority | One non-duplicative workflow with explicit responsibility, conflict routing, and validation handoff. |
| Use heterogeneous evidence | Data, calculations, interviews, transcripts, scans, images, audio/video, spreadsheets, or extracted content | Claim-linked evidence records that preserve permissions, source lineage, transformation, reproduction, uncertainty, and inspection boundary. |
| Maintain a documentation system | Interconnected pages, versions, dependencies, reader tasks, issue reports, and owners | Navigable content architecture, synchronized changes, reader validation, corrections, deprecation, and lifecycle state. |
| Audit without changing the artifact | Draft, comparison evidence, governing requirements, and optional correction request | Non-mutating findings plus separately classified proposed corrections; revision occurs only under an explicit bounded authorization. |
| Prepare delivered writing | Speech, presentation, lesson, narrated script, podcast, voiceover, demonstration, or other delivered artifact plus audience and constraints | Delivery-aware writing whose full timing or attention budget, evidence flow, questions, media, audience layers, and closing movement fit the intended use. |
| Maintain synchronized output formats | Authoritative source artifact, required derivatives, accepted change, and available artifact validators | Refreshed or explicitly stale derivatives with recorded comparison, rendering, playback, accessibility, and format-specific validation boundaries. |
| Assess AI-related writing concerns responsibly | Draft, optional authorized writing samples, process records, and optional external detector report | Non-mutating writing-pattern profile, method-bounded measurements, assistance provenance, and a calibrated authorship boundary rather than an AI probability. |
| Preserve or overwrite persistent drafts | A file-writing request with no established write policy | One explicit choice between append-only response-batch history and current-file overwrite, applied without changing revision authority. |

## Functional requirements

| ID | Product requirement | Business requirements |
|---|---|---|
| PR-001 | Select Review, Write, or Audit from the request; default broad draft review to Review and scale depth proportionately. | BR-006, BR-009 |
| PR-002 | For new writing, use an explicit topic when supplied; otherwise offer existing-topic, refine-direction, or brainstorm paths. | BR-003, BR-004 |
| PR-003 | Build a progressive brief covering topic, goal, audience, prior knowledge, context, governing directions, content roles, exclusions, references, voice target, and constraints. Mark material fields Known, Inferred, or Unknown. | BR-003, BR-004, BR-009 |
| PR-004 | Resolve direction priority; distinguish required, optional, background-only, and excluded content; distinguish hard constraints, working targets, allocations, and safety buffers. | BR-004, BR-012 |
| PR-005 | State the evidence boundary whenever it limits a conclusion, and separate the writing brief, factual evidence, voice samples, and verification status. | BR-001, BR-005, BR-007 |
| PR-006 | Review source relationships across wording, syntax, idea order, detail selection, and rhetorical architecture; classify supported relationships precisely. | BR-001, BR-005 |
| PR-007 | Review specificity, authorial presence, consistency, redundancy, formulaicity, abstraction, example function, emotional integrity, useful irregularity, and logical flow across chapters, headings, subheadings, or other visible boundaries without classifying AI authorship or forcing artificial transitions. | BR-002, BR-007 |
| PR-008 | When close voice fidelity matters, request representative authorized writing if evidence is thin; build a bounded voice brief, separate style from content, and report basis and confidence. | BR-002, BR-003, BR-007, BR-011 |
| PR-009 | Rank findings by consequence and confidence, identify material to preserve, rewrite only when requested, and apply an honest readiness label when unresolved matters affect use. | BR-003, BR-009, BR-012 |
| PR-010 | Score only on request or when it materially aids comparison; keep strength and risk families separate, use N/A when unsupported, and explain every score with evidence. | BR-005, BR-009 |
| PR-011 | When verification is requested, prefer the original source, inspect relevant context, report access status, and never represent partial access as full verification. | BR-001, BR-005, BR-007 |
| PR-012 | Use a structured choice control for two or three consequential mutually exclusive options when the active harness provides one; otherwise preserve the same decision in concise plain text without changing the host's collaboration or execution mode. | BR-003, BR-004, BR-013 |
| PR-013 | Enforce privacy, minimization, authorization, evidence, identity, emotional-integrity, and high-stakes human-review limits. | BR-005, BR-007, BR-011 |
| PR-014 | Operate from repository-local Markdown/YAML with relative links and no required service or package; support optional repository, user, or admin discovery through links or copies of the authoritative project skill. | BR-008, BR-010, BR-013 |
| PR-015 | Keep the operational core compliant with the portable Agent Skills shape and independent of vendor tool names, model IDs, invocation syntax, or proprietary frontmatter. Provide capability-based fallbacks and optional adapters for Codex, Claude, Pi, and other hosts. | BR-008, BR-010, BR-013 |
| PR-016 | For fiction creation and requested revision, use a scalable Unsloop Write workflow that covers discovery, creative contract, foundation, architecture, scene design, drafting, revision, and handoff without forcing a single story framework or subject domain. | BR-003, BR-004, BR-006, BR-014 |
| PR-017 | For sustained fiction, offer Guided, Adaptive, and Autonomous collaboration; preserve author-owned locked decisions; maintain only an approved, proportionate, portable Markdown project; and distinguish Proposed, Confirmed, and Superseded canon. | BR-003, BR-008, BR-011, BR-012, BR-014 |
| PR-018 | Route fiction through Write, Review, or Audit according to the requested job, and load the applicable fiction workflow without creating a fourth mode. | BR-006, BR-009, BR-014, BR-016 |
| PR-019 | Onboard an existing manuscript by inventorying versions and boundaries, preserving its layout, assigning stable internal IDs, extracting state as Proposed with manuscript basis, and obtaining approval before creation or promotion. | BR-003, BR-005, BR-008, BR-015 |
| PR-020 | Support explicit project, manuscript-unit, canon, batch, and branch states; partial acceptance and rejection; retcon impact analysis; recoverable consequential revision; and state reconciliation. | BR-003, BR-009, BR-012, BR-014, BR-015 |
| PR-021 | Provide author-readable fiction templates and optional standard-library initialization, checking, checkpointing, and accepted-unit assembly with dry-run previews, relative paths, and overwrite refusal. | BR-008, BR-010, BR-011, BR-015 |
| PR-022 | Provide selectable fiction Review and Audit contracts for developmental, structural, character, continuity, POV, dialogue, theme, prose, line, copy, reader-response, research, adaptation, and authenticity work. | BR-002, BR-005, BR-009, BR-013, BR-016 |
| PR-023 | Support manuscript completion, deterministic assembly, synopsis, query, blurb, pitch, series summary, and submission-checklist handoff while distinguishing creative, editorial, assembly, and submission stages. | BR-003, BR-005, BR-009, BR-016 |
| PR-024 | For sustained non-fiction, offer Guided, Adaptive, or Autonomous collaboration and maintain only an approved proportionate Markdown project with authoritative versions, stable section IDs, accepted unit state, compact resume context, and non-destructive existing-work onboarding. | BR-003, BR-008, BR-012, BR-017 |
| PR-025 | Track sources, claims, quotations, draft locations, supporting and conflicting evidence, access level, verification status, freshness, and required action without treating bibliography presence as consultation or support. | BR-001, BR-005, BR-011, BR-018 |
| PR-026 | Establish bounded revision contracts; classify material changes; preserve and honestly scope useful author-supplied observations, interpretations, unresolved questions, and tentative perspectives instead of deleting them solely for lacking external verification; keep embedded factual claims subject to independent support; support partial acceptance and rejection; map downstream effects; checkpoint consequential revisions; and reconcile affected manuscript and project state. | BR-003, BR-005, BR-009, BR-012, BR-017, BR-018 |
| PR-027 | Model stakeholder roles, decision authority, organizational directions, feedback conflicts, owners, dispositions, and version-specific approval without inferring authority from seniority, recency, or silence. | BR-003, BR-004, BR-012, BR-019 |
| PR-028 | Support translation, localization, bilingual drafting, cross-language source use, and cross-language voice adaptation while preserving meaning, qualification, attribution, quotation status, terminology authority, and uncertainty. | BR-002, BR-003, BR-005, BR-011, BR-019 |
| PR-029 | Produce optional machine-readable results using supplied schemas or the portable Unsloop schema while preserving stable identifiers, evidence boundaries, confidence, readiness, privacy minimization, and human-readable semantics. | BR-005, BR-009, BR-010, BR-011, BR-019 |
| PR-030 | Provide optional standard-library sustained-writing project initialization, checking, checkpointing, Accepted-unit assembly, and JSON state export with dry-run previews, path confinement, hashes, and overwrite refusal. | BR-008, BR-010, BR-017, BR-018, BR-019 |
| PR-031 | Maintain a versioned `CharacterVoiceProfile` for each recurring speaking character, using user-defined traits first and keeping contextual suggestions Proposed until author acceptance; distinguish personality, narrative viewpoint, and dialogue behavior. | BR-003, BR-014, BR-020 |
| PR-032 | Detect character voice drift and require an explicit, impact-aware author disposition before a prospective evolution or retroactive override can replace a Confirmed profile. | BR-003, BR-009, BR-015, BR-020 |
| PR-033 | Route biography, documentary narrative, procedure, policy, plan, direction, instruction, and technical documentation through form-specific contracts inside Write, Review, or Audit. | BR-004, BR-006, BR-009, BR-021 |
| PR-034 | Establish user-provided-only, scoped-web, broad-web, or hybrid source acquisition; assess claim-specific suitability, provenance, independence, currency, and corroboration; and record user overrides without upgrading evidence. | BR-001, BR-003, BR-005, BR-018, BR-021 |
| PR-035 | Validate and hand off documentary and controlled documents using form-appropriate chronology, authority, requirement, procedure, policy, plan, technical, test, approval, maintenance, and readiness evidence. | BR-005, BR-009, BR-012, BR-017, BR-021 |
| PR-036 | When another skill or qualified specialist applies, assign domain, artifact, integrity, voice, and approval responsibility explicitly; reuse intake and route conflicts to the narrowest authorized owner. | BR-003, BR-004, BR-012, BR-022 |
| PR-037 | Treat all retrieved or supplied source content as untrusted evidence; prevent embedded instructions, redirects, active content, or credential requests from changing tools, permissions, research scope, or project data. | BR-005, BR-007, BR-011, BR-018, BR-022 |
| PR-038 | Track and verify numerical claims through source version, population, period, units, inputs, filters, transformations, reproduced result, displayed result, uncertainty, and recalculation state. | BR-001, BR-005, BR-018, BR-023 |
| PR-039 | Govern interview and oral-history evidence through consent, attribution, record type, transcript range, quotation rights, corrections, corroboration, subject response, privacy, and retention. | BR-003, BR-005, BR-007, BR-011, BR-023 |
| PR-040 | Preserve the original-to-derived transformation and inspection boundary for scans, OCR, audio, video, images, screenshots, diagrams, spreadsheets, and extracted text. | BR-005, BR-011, BR-023 |
| PR-041 | Model documentation sets through audiences, reader tasks, content types, canonical ownership, navigation, dependencies, reused content, versions, states, and change-impact relationships. | BR-004, BR-009, BR-017, BR-024 |
| PR-042 | Maintain published documentation through scheduled and event-driven review, issue intake, correction, errata, change notice, deprecation, withdrawal, supersession, retention, and archival. | BR-005, BR-009, BR-012, BR-024 |
| PR-043 | Validate comprehension, findability, task performance, accessibility, plain language, and localization while distinguishing simulated hypotheses, automated checks, expert review, and observed human tests. | BR-004, BR-005, BR-009, BR-019, BR-024 |
| PR-044 | Make Audit non-mutating by default; preserve material information fields; separate findings from revision; and require explicit bounded authorization before applying presentation-only or meaning-changing corrections. | BR-003, BR-005, BR-009, BR-012, BR-025 |
| PR-045 | For live, recorded, timed, interactive, or media-assisted writing, establish a delivery contract; reconcile the overall constraint with section allocations and all audience-time elements; integrate evidence through need, orientation, presentation, interpretation, and use; and review questions, audience layers, optional media, and closing movement proportionately. | BR-003, BR-004, BR-005, BR-009, BR-012, BR-026 |
| PR-046 | For required multi-format outputs, identify the authoritative source or synchronization rule; map derivative impact; refresh required derivatives after accepted changes; route rendering, playback, accessibility, and format checks to the applicable artifact capability; and report only validation actually performed. | BR-003, BR-005, BR-009, BR-022, BR-024, BR-026 |
| PR-047 | When asked for an AI score, machine-authorship judgment, AI-like pattern analysis, writing-sample comparison, assistance assessment, or detector-report interpretation, run a non-mutating Writing-Pattern and Assistance Audit that separates component style scores, method-declared measurements, authorized voice comparison, direct process provenance, and external detector results; never combine them into an AI-authorship probability or automatic decision. | BR-002, BR-005, BR-007, BR-009, BR-011, BR-027 |
| PR-048 | When a writing style materially affects the work, establish a `StyleBrief` from the author's evidenced voice, a historical or literary tradition, a custom design, or a restrained genre default; separate all voice and form channels; and define authenticity, readability, evidence, and imitation boundaries before consequential drafting or revision. | BR-002, BR-003, BR-004, BR-005, BR-007, BR-028 |
| PR-049 | Support Stable, Gradual, or Phase-based stylistic evolution with Proposed, Confirmed, and Superseded state, author-approved transitions, scoped application, portable optional `STYLE.md` records, and drift-aware Review or non-mutating Audit. | BR-003, BR-008, BR-009, BR-012, BR-017, BR-028 |
| PR-050 | Before the first persistent write when policy is unknown, ask the user to choose **Immutable versions** or **Overwrite current** through the available structured selector or an equivalent concise prompt. Immutable versions preserve a baseline when needed and one append-only batch containing every persistent artifact written in each assistant response; overwrite current creates no automatic response snapshots. Persist the choice for sustained projects, avoid redundant questions, refuse history collisions, and never treat either policy as authorization to revise meaning, locked state, or an audited artifact. | BR-003, BR-008, BR-009, BR-011, BR-012, BR-025, BR-029 |

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
| NFR-008 Long-form resilience | A sustained fiction or non-fiction project can resume without loading the full conversation or manuscript, while conclusions remain bounded to the records and prose actually inspected. | `story/STATUS.md` or `writing/STATUS.md` identifies the current phase, accepted checkpoint, immediate state, open decisions, next action, and required context. |
| NFR-009 Recoverability | Every consequential manuscript or canon revision has a resolved affected scope and a usable path back to the prior accepted state. | A version-control checkpoint or project-local file-and-hash manifest exists before mutation, and overwrite collisions fail closed. |
| NFR-010 Behavioral consistency | Critical fiction decisions are tested as behavior rather than inferred from documentation presence. | Deterministic tests and clean-context scenarios cover routing, onboarding, state transitions, retcons, recovery, review, and assembly. |
| NFR-011 Evidence freshness | Material changes to a claim, quotation, source version, or inspected boundary cannot silently inherit an earlier verification state. | Provenance records identify last checked basis and require recheck after a material change. |
| NFR-012 Editorial recoverability | Consequential sustained-writing changes preserve the prior accepted state, author-owned perspective, and accepted scope. | A version-control checkpoint or affected-file snapshot exists, collisions fail closed, rejected changes do not enter the active artifact, and useful author-supplied perspective is not dropped solely because it lacks external verification. |
| NFR-013 Structured interoperability | Machine-readable Unsloop results remain syntactically checkable, semantically explicit, privacy-minimized, and equivalent in limits to human-readable output. | The bundled schema parses, required evidence and readiness fields exist, and missing evidence remains null or omitted rather than invented. |
| NFR-014 Character continuity | Accepted character identity remains stable across units, sessions, and models until an author-approved version change. | Each recurring speaker has at most one applicable Confirmed profile per scope, and drift or change is surfaced rather than silently normalized. |
| NFR-015 Research transparency | Source scope, suitability, overrides, claim confidence, currency, and actual validation remain inspectable and non-interchangeable. | Persistent research records distinguish acquisition mode, corpus, verification, suitability, confidence, testing, and approval, and scoped research never broadens silently. |
| NFR-016 Instruction isolation | Evidence content cannot redefine user intent, permissions, tool use, or governing workflow. | Runtime instructions state that embedded source instructions are data, and project checks require the source-policy boundary. |
| NFR-017 Evidence reproducibility | Material quantitative or transformed evidence retains enough lineage to identify inputs, method, coverage, result, and uncertainty. | Data and media records distinguish source-reported, reproduced, extracted, checked, and unavailable states. |
| NFR-018 Documentation operability | A documentation set remains navigable, maintainable, and honestly validated after publication. | Content ownership, dependencies, lifecycle state, review triggers, issue disposition, reader-validation type, and retest state remain visible. |
| NFR-019 Semantic preservation | Audit cannot silently alter the information conveyed by the inspected artifact. | Audit output identifies the unchanged artifact version; every proposed correction records whether it is presentation-only or meaning-changing, its semantic effects, authorization, and disposition. |
| NFR-020 Delivery readiness | A delivered or multi-format artifact cannot appear ready by prose polish alone. | Readiness identifies the duration or attention basis, unresolved media or interaction decisions, authoritative format, derivative freshness, and actual rehearsal, comparison, render, playback, accessibility, or format validation boundary when material. |
| NFR-021 Authorship calibration | Textual pattern assessment cannot overstate what prose, samples, process evidence, or detector reports establish about AI involvement. | Draft-only output states “Not assessable from prose alone”; every score names its direction and evidence; every measurement states method and coverage; provenance and detector results remain separate; no composite AI score is produced. |
| NFR-022 Style traceability | A consequential selected style and its evolution remain stable and inspectable across sections, sessions, models, languages, and collaborators without implying authenticity beyond the evidence. | The active `StyleBrief`, applicable phase, evidence basis, approved deviations, and channel boundaries can be identified; Confirmed style changes require an explicit disposition. |
| NFR-023 Write-history integrity | Response history remains portable, inspectable, append-only by contract, and bounded to the artifacts actually written in a response. | Each immutable batch has a unique ID, kind, relative paths, hashes, reason, and optional parent; existing batches cannot be replaced, and another session can reconstruct what was written without relying on hidden host memory. |

## Interaction requirements

### Intake

- Reuse information already present; do not ask the user to repeat it.
- Ask the smallest useful question batch and normally no more than three structured questions at once.
- Use open conversation for topics, drafts, sources, context, and samples that cannot be reduced safely to fixed options.
- Pause only when a missing fact, authorization, source, or high-stakes choice cannot be inferred responsibly.
- Map semantic needs to the active harness's native capabilities and use the documented fallback when a tool is absent.
- For sustained fiction, ask for Guided, Adaptive, or Autonomous collaboration only when the cadence is not already clear; use Adaptive by default and let the user change it later.
- Propose persistent fiction files once when they become useful and require approval before creating a new layout.
- For an existing manuscript, inventory and propose state before creating files or promoting inferred facts.
- For a broad fiction critique, default to a standard developmental review rather than applying every review contract at maximum depth.
- For sustained non-fiction, propose project files once only when they improve resumability; preserve an existing coherent layout and require approval before creation or reorganization.
- For persistent non-fiction, ask for Guided, Adaptive, or Autonomous collaboration only when cadence is not already clear; use Adaptive by default and pause in every cadence before changing locked author, evidence, requirement, privacy, commitment, terminology, or approval decisions.
- For collaboration, ask only about unresolved authority conflicts that materially affect the artifact and route decisions to the documented owner.
- For translation or localization, establish the source/target language, audience, translation mode, and terminology authority before choices that could alter meaning.
- For recurring fictional characters, accept author-defined personality and speech settings or offer materially different context-based proposals; lock only accepted profiles and pause before changes.
- When style is consequential and not already specified, offer evidenced personal voice, historical or literary tradition, custom design, or genre default; resolve authenticity and evolution only to the depth needed.
- For documentary and controlled documents, establish the artifact family and source acquisition mode before research; never leave an approved scoped corpus silently.
- When another skill applies, identify responsibility once, reuse its resolved intake, and do not override specialized domain or format validation.
- For numerical, interview, or multimodal evidence, ask only for missing permissions, originals, inputs, ranges, or transformations that materially affect support.
- For documentation systems, establish canonical ownership, supported versions, dependencies, maintenance triggers, and required reader-validation type before a consequential release.
- For delivered work, resolve the setting, hard duration or length, pace basis when material, section allocations, audience interaction, required and optional media, authoritative source format, required derivatives, and expected validation without asking for details already supplied by a governing specialist.

### Voice-sample request

When a closer match materially affects the result and evidence is weak, request two or three representative samples, preferably in the same genre and roughly 500–2,000 words total. If the user declines, continue where safe with a lower confidence label.

### Output

- Put the requested writing first in Write mode unless process notes were requested.
- In Review, lead with the overall assessment and highest-value findings.
- In Audit, include the evidence boundary before source-dependent conclusions.
- In Audit, leave the inspected artifact unchanged and separate every proposed correction from the finding; if revision is also requested, preserve a distinct audit stage and state the authorized revision scope.
- Keep findings passage-specific and corrections proportionate.
- Do not add scores, tables, or readiness labels when they would add ceremony rather than value.

## Acceptance criteria by workflow

### Review

Given an existing draft and a broad review request, Unsloop selects Review, infers the apparent brief, identifies the most consequential integrity and voice findings, preserves sound prose, states material evidence limits, and does not rewrite unless asked.

### Write

Given a clear topic and sufficient brief, Unsloop does not repeat the topic question, drafts toward the stated reader outcome, respects content roles and hard constraints, checks source-based claims and human voice, and discloses material assumptions or readiness limits.

### Audit

Given a draft and comparison sources, Unsloop records exactly what was inspected, maps supported textual relationships and claims, separates requirement satisfaction from source support, identifies unresolved checks, and does not infer intent or misconduct. It leaves the audited artifact unchanged, even when information appears incorrect or unsupported; it identifies the passage, evidence, and smallest responsible proposal without applying it.

Given a request for Audit plus revision, Unsloop preserves the Audit result as a distinct stage, establishes the authoritative version and allowed revision scope, classifies proposals as presentation-only or meaning-changing, identifies semantic and downstream effects, and applies only authorized changes. Grammar, cleanup, clarity, tone, or formatting authority does not permit changing claims, positions, recommendations, conclusions, scope, certainty, evidence strength, chronology, quantities, attribution, causality, conditions, exceptions, or exclusions.

### Voice fidelity

Given authorized representative samples, Unsloop derives only observable task-relevant traits, does not import sample facts or memorable wording, adapts for the new genre and audience, and reports the basis and Low, Moderate, or High confidence when fidelity is material.

### Style direction and evolution

Given an explicit style request, Unsloop does not ask the author to select a style again. It builds a `StyleBrief` that separates author voice, selected narrative or document style, viewpoint voice, character dialogue, and form or delivery conventions. For historical or literary traditions, it records period, region, form, corpus boundary, authenticity stance, readability target, evidence basis, confidence, modernization policy, and intentional anachronisms; it does not infer authenticity from decorative markers or collapse related periods into one preset.

Given no selected direction when style materially affects the outcome, Unsloop offers evidenced personal voice, historical or literary tradition, custom design, or a restrained genre default through a structured selector when available and an equivalent conversational fallback otherwise. Named-author requests become bounded high-level, non-exclusive traits without signature imitation.

Given a Stable, Gradual, or Phase-based evolution, each consequential transition has scope, trigger, trait diff, rationale, state, and author decision. Proposed changes do not alter Confirmed style; Review identifies drift and the smallest intervention; Audit leaves the artifact and style state unchanged.

### Cross-section flow

Given a manuscript with chapters, headings, subheadings, scene breaks, procedural phases, or comparable divisions, Unsloop evaluates each material boundary through the preceding close, the heading or break, and the next opening. It identifies the actual relationship, uses the smallest necessary bridge, preserves a purposeful hard break, and does not equate coherence with an added transitional sentence. Review returns the boundary, consequence, and smallest intervention; Audit leaves the manuscript unchanged; Write revises only within the authorized scope without changing substantive information merely for smoothness.

### Delivery and presentation writing

Given a live, recorded, timed, interactive, or media-assisted artifact, Unsloop confirms the delivery contract and reconciles the overall limit with section allocations and every element that consumes delivery time or audience attention. It does not solve an overrun through assumed speed, omitted pauses, invisible media handling, or silent redistribution. Material evidence receives enough need, orientation, accurate presentation, interpretation, and supported use to function for the audience without imposing a fixed prose formula. Questions have a purpose, placement, answer path, and payoff rather than a quota. Mixed audiences receive a shared entry point and appropriate depth. Consequential optional media receives a decision brief and remains unselected until authorized; unresolved choices that affect use keep the artifact provisional. The closing produces the intended final audience state without forcing action or adding a new major point.

### Multi-format artifact synchronization

Given required parallel formats, Unsloop identifies the authoritative source or explicit synchronization rule, includes derivatives in change-impact analysis, and uses the applicable artifact capability for generation and validation. After accepted changes, required derivatives are refreshed and checked or marked stale. Handoff distinguishes comparison, rendering, playback, accessibility, rehearsal, and other validations actually performed; a successful export, matching filename, or polished manuscript does not establish synchronization or usability.

### Writing-pattern and assistance audit

Given a request for an AI score, AI detection, or a judgment that prose was machine-generated, Unsloop uses Audit and leaves the inspected artifact unchanged. With prose alone it states **AI authorship determination: Not assessable from prose alone** and substitutes a directional component profile: Specificity and Authorial voice as strengths; Redundancy, Formulaicity, and Abstraction as risks; optional Voice fidelity only with authorized comparison samples; and optional Slop density only as writing-quality risk. It cites passage evidence and never creates one combined AI number.

Given calculable textual features, Unsloop reports only values actually measured and identifies the method, unit, inspected range, exclusions, comparison baseline, and material limitations. Given revision history, metadata, prompts, model outputs, disclosures, or other process records, it reports the exact assistance scope directly supported without inferring the remainder of the workflow. Given an external detector report, it records the tool, version, date, inspected input, settings or threshold, vendor result, and limits as an **External detector result**; it does not restate the result as authorship probability or average it with Unsloop scores.

Given authorized writing samples, Unsloop may assess voice alignment with a confidence label but cannot treat either similarity or mismatch as proof of identity, human authorship, AI use, ghostwriting, or misconduct. Genre, language, translation, templates, collaboration, editing, disability-related patterns, and institutional requirements remain part of interpretation. A request to lower a detector score is redirected to genuine quality goals and cannot authorize detector evasion.

### Fiction

Given a clear isolated scene request, Unsloop uses a minimal fiction brief, writes the requested unit, and does not require novel-scale planning or files. Given sustained fiction, it confirms a creative contract and cadence, proposes the smallest useful `story/` and `manuscript/` layout once, and creates it only after approval. It preserves accepted manuscript and Confirmed canon, marks unaccepted discoveries Proposed, requires an explicit retcon to supersede canon, keeps research separate from invented story facts, and returns the requested creative artifact before checkpoint notes.

Given Autonomous cadence, Unsloop works only through the approved batch and pauses before changing the premise, ending direction, POV system, content boundaries, real-person treatment, Confirmed canon, or another locked author decision. Given limited model context, it resumes from `story/STATUS.md`, relevant ledgers, and the necessary manuscript range and does not claim global consistency from partial inspection.

### Existing-manuscript onboarding and recovery

Given an established manuscript, Unsloop inventories supplied versions and project materials, records the inspection boundary, resolves the working authority, preserves the existing layout, assigns stable internal unit IDs without renaming files, and presents extracted state as Proposed with manuscript locations and confidence. It creates only approved missing records and promotes only accepted or clearly established state.

Given partial acceptance, rejection, a branch, a retcon, or a consequential revision, Unsloop updates only the accepted scope, prevents rejected details from entering active state, maps downstream effects before changing Confirmed canon, creates a recoverable checkpoint before mutation, and reconciles the manuscript and ledgers afterward.

### Fiction review and audit

Given a focused fiction-review request, Unsloop selects Review or Audit and the smallest applicable contract. It identifies the manuscript boundary and project stage, ranks manuscript-level causes before symptoms, preserves strong material, names downstream impact, and distinguishes simulated reader hypotheses and authenticity questions from actual reader research or lived-experience authority. When Audit is selected, manuscript and story state remain unchanged and corrections remain separate proposals.

### Completion and publication handoff

Given Accepted Markdown manuscript units, Unsloop previews deterministic assembly, excludes non-Accepted or branch material by default, refuses overwrite, and returns an output manifest. Supporting artifacts follow supplied requirements and manuscript evidence. Unsloop distinguishes creative completion, structural revision, line editing, copyediting, assembly, and submission-package preparation without certifying legal, market, professional-editor, agent, publisher, or platform acceptance.

### Sustained non-fiction

Given substantial multi-session non-fiction, Unsloop selects Guided, Adaptive, or Autonomous collaboration, using Adaptive by default; proposes the smallest useful `writing/` and `manuscript/` profile once; preserves a coherent existing layout; creates files only after approval; uses stable section IDs without automatic renaming; and resumes from `writing/STATUS.md` plus only relevant ledgers and manuscript ranges. Accepted units and current directions remain authoritative. Autonomous work stops at the approved batch and cannot silently change locked author positions, evidence conclusions, requirements, privacy boundaries, external commitments, terminology, or approval state.

### Research provenance

Given research-dependent writing, Unsloop keeps source access, claim support, conflicting evidence, quotations, manuscript locations, and verification freshness distinct. A changed claim is rechecked rather than inheriting stale verification. Citation formatting follows supplied requirements but does not upgrade source or claim status.

### Character voice continuity

Given multiple recurring speakers, Unsloop gives each character a versioned personality and dialogue profile. The author may define it directly or approve one of several context-based proposals. Once Confirmed, the profile governs drafting across units and sessions; emotional context may vary within its stated range, while prospective evolution and retroactive override require an explicit diff, impact map, checkpoint, and author disposition.

### Documentary and documentation writing

Given a biography, documentary narrative, procedure, policy, plan, direction, instruction, or technical-documentation request, Unsloop establishes the form, outcome, audience, authority, scope, version, evidence-acquisition policy, validation standard, owner, and maintenance cycle. It may use supplied evidence, approved sites, broad web research, or a hybrid corpus. Source overrides remain recorded limitations rather than verification upgrades, and handoff does not overclaim factuality, testing, safety, compliance, approval, completeness, or currentness.

### Skill composition and source safety

Given overlapping domain or artifact skills, Unsloop reuses their intake and preserves explicit responsibility: the user and governing owner retain decisions, the narrow specialist controls domain facts or artifact mechanics, and Unsloop controls writing integrity, voice, provenance, and readiness. Retrieved content remains untrusted evidence. Embedded instructions, active content, redirects, or credential requests cannot expand tool use, permissions, corpus, or data disclosure.

### Quantitative, interview, and multimodal evidence

Given numerical claims, Unsloop records inputs, population, period, unit, formula, filters, transformations, reproduced result, displayed result, uncertainty, and status without confusing source reporting with recalculation. Given interviews, it preserves consent, attribution, transcript type, permissions, corrections, corroboration, subject response, and restrictions. Given extracted media, it preserves the original artifact, range, method, derived artifact, transformation, missing content, and inspection status.

### Documentation systems and reader validation

Given a documentation set, Unsloop inventories audiences, reader tasks, content types, canonical ownership, versions, dependencies, links, state, and review triggers. Consequential changes map downstream pages and reused content. Published work supports correction, deprecation, withdrawal, supersession, and archival. Comprehension, findability, task, accessibility, plain-language, and localization results identify whether they came from simulated hypotheses, automated checks, expert review, or observed participants.

### Revision and collaboration

Given a consequential revision, Unsloop establishes the version and scope, protects strong or locked material, maps downstream claim, citation, requirement, terminology, and dependent-artifact effects, checkpoints affected files, and applies only accepted changes. It distinguishes externally checkable claims from useful author-supplied observations, interpretations, unresolved questions, and tentative perspectives; preserves the latter through proportionate scoping and evidence-status framing; and verifies or qualifies any embedded factual claim separately. Given conflicting feedback, it identifies authority and decision ownership, consolidates duplicates without erasing distinct reasons, and does not infer approval from addressed comments or silence.

### Multilingual writing

Given translation, localization, or cross-language voice work, Unsloop establishes the translation mode, locale, audience, terminology, quotation policy, and evidence boundary. It preserves claim strength and attribution, distinguishes author voice from translator and genre conventions, reports unresolved ambiguity, and does not infer identity or cultural authority.

### Structured output

Given a machine-readable request, Unsloop uses the supplied schema or its portable schema, validates syntax when tooling permits, preserves stable locations, evidence, confidence, readiness, and out-of-scope limits, and does not invent values merely to make the artifact schema-valid.

### Persistent write policy and response history

Given a request that will create or modify persistent artifacts and no established policy, Unsloop asks once whether to use **Immutable versions** or **Overwrite current**. Chat-only drafting, read-only Review, and non-mutating Audit do not trigger the question. Under immutable versions, Unsloop preserves the pre-write baseline when necessary, keeps current working files usable, and stores one collision-resistant batch for all files written in each assistant response. Under overwrite current, it updates the current artifacts without manufacturing historical snapshots. Both paths continue to enforce revision scope, checkpoints, canon and decision locks, collision safeguards, and Audit non-mutation.

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
- validated fiction routing, cadence, portable-state, canon, voice-separation, and manuscript-resumption contracts.
- validated Style Direction, authenticity, voice-channel separation, evolution, portable-state, and drift-control contracts.
- passing deterministic fiction-project operations and behavioral fixtures for cross-mode routing, onboarding, state lifecycles, retcons, recovery, review, and assembly.
- passing deterministic sustained-writing project operations and behavioral fixtures for onboarding, provenance, revision, collaboration, multilingual boundaries, assembly, export, and path safety.
- passing character-profile, documentary-form, source-acquisition, override, scoped-corpus, and validation-status behavioral contracts.
- passing skill-composition, untrusted-source, quantitative, interview, multimodal, documentation-system, maintenance, and reader-validation behavioral contracts.
- passing delivery-budget, evidence-integration, question-function, mixed-audience, optional-media, closing, derivative-synchronization, and delivery-readiness behavioral contracts.
- passing writing-pattern profile, measurement-method, authorized-sample, process-provenance, external-detector, fairness, and anti-evasion behavioral contracts.

Calibration, benchmark fixtures, inter-reviewer agreement, privacy review, and mode-split evidence remain later release work in [`ROADMAP.md`](ROADMAP.md).

## Detailed normative documents

- [`docs/REVIEW-MODEL.md`](docs/REVIEW-MODEL.md)
- [`docs/SCORING-RUBRIC.md`](docs/SCORING-RUBRIC.md)
- [`docs/REVIEW-OUTPUT.md`](docs/REVIEW-OUTPUT.md)
- [`docs/ETHICS-AND-LIMITS.md`](docs/ETHICS-AND-LIMITS.md)
- [`docs/NAMING.md`](docs/NAMING.md)
