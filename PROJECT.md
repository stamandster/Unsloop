# Project Definition

> **Document role:** Concise project charter. [`BRD.md`](BRD.md) is authoritative for business requirements, [`PRD.md`](PRD.md) for product requirements, and [`FSD.md`](FSD.md) for functional behavior.

## Vision

Unsloop is an author-led writing lifecycle system. It helps people move from topic discovery and purpose through drafting, revision, review, audit, research, validation, maintenance, and handoff while preserving control, evidence provenance, human voice, continuity, and honest readiness.

The project coordinates four connected concerns:

1. **Author direction and control:** the goal, audience, meaning, constraints, voice, creative canon, and consequential decisions remain author-owned.
2. **Integrity and evidence:** attribution, paraphrase, claims, quotations, source dependence, research scope, provenance, and uncertainty remain inspectable and defensible.
3. **Voice and craft:** prose stays specific, readable, structurally coherent, emotionally responsible, and recognizably grounded in the writer's choices.
4. **Continuity and operation:** long-form state, versions, collaboration, delivery, derivative formats, validation, maintenance, and resumption remain explicit and portable.

These concerns overlap, but they are not interchangeable. Formulaic or AI-associated writing patterns are one evidence-bound Audit specialization within this larger lifecycle—not the project's defining category and never proof of machine authorship.

## Product promise

Unsloop supports writing from first direction through durable delivery and evaluates observable features when reviewing or auditing. It does not infer misconduct or machine authorship from style alone.

For substantial work, Unsloop first establishes what the writing is meant to accomplish for a particular audience. It uses a progressive brief, distinguishing what is known, reasonably inferred, and still unknown, so that missing context does not silently become invented content.

Every material review or audit finding should answer four questions:

1. What passage or claim is under review?
2. What concrete feature creates concern?
3. What evidence supports the finding?
4. What correction would preserve the writer's meaning and voice?

## Intended users

- Writers planning, drafting, revising, reviewing, maintaining, or delivering academic, professional, technical, religious, personal, persuasive, documentary, or creative work
- Editors and auditors who need repeatable, information-preserving diagnosis across integrity, voice, structure, continuity, and requirements
- Researchers, educators, and documentation teams managing claims, sources, versions, long-form state, or reader-facing systems
- Collaborators who want model-assisted writing to remain accountable, portable, resumable, and author-led

## Scope

Unsloop can:

- review a draft without rewriting it;
- compare a draft with supplied or verifiable sources;
- distinguish quotation, acceptable paraphrase, patchwriting, structural borrowing, and unattributed borrowing;
- assess evidence strength and citation placement;
- identify concrete forms of generic or formulaic prose;
- translate AI-score or machine-authorship requests into a non-mutating writing-pattern and assistance assessment with separate component scores, measurements, provenance, and detector-report boundaries;
- compare a draft with authorized writing samples for voice fidelity without treating similarity or mismatch as proof of identity, human authorship, or AI use;
- preserve strong passages and explain why they work;
- revise text when the user requests revision;
- draft new text from the user's purpose, position, facts, and natural vocabulary;
- accept an existing topic, help refine a rough direction, or brainstorm distinct and feasible topic options before drafting;
- establish topic, goal, audience, prior knowledge, context, governing directions, content roles, exclusions, reference material, voice target, and format or delivery constraints without forcing a full questionnaire when the answer is already available;
- use structured choice prompts for short, consequential decisions when the active harness exposes them, with an equivalent conversational fallback;
- extract governing directions and resolve material conflicts without treating instructions as factual evidence;
- classify supplied material as required, optional supporting, background only, or excluded;
- distinguish hard constraints, working targets, component allocations, and safety buffers;
- audit requirement coverage separately from claim and source verification;
- keep Audit non-mutating, preserve the authoritative inspected artifact, and separate findings from any later authorized revision;
- test examples for function and persuasive language for emotional integrity;
- write and review logical progression across chapters, headings, subheadings, scene breaks, and procedural phases by evaluating the preceding close, visible boundary, and next opening together;
- preserve purposeful hard breaks and avoid canned or unnecessary transitional sentences when hierarchy and sequence already orient the reader;
- plan and review spoken, timed, interactive, media-assisted, or recorded writing against the complete delivery and audience-attention cost rather than manuscript words alone;
- integrate quotations, data, readings, visuals, clips, and demonstrations through a clear audience need, orientation, accurate presentation, interpretation, and supported use without forcing a formula;
- use purposeful questions, mixed-audience entry points, consequential optional-media decisions, and genre-appropriate closing movement;
- identify authoritative content and keep required Markdown, DOCX, PDF, slide, web, audio, or other derivatives refreshed, validated, or explicitly stale;
- distinguish ready work from provisional work that still requires a decision, evidence, or authorization;
- request authorized examples of the user's previous writing when closer voice fidelity would materially improve the result;
- derive a bounded voice brief from observable traits and report the evidence basis and confidence of the match;
- select an evidenced-personal, historical or literary, custom, or genre-default Style Direction and keep it distinct from author, narrator, viewpoint, dialogue, and delivery voice;
- define period, region, form, authenticity, readability, corpus, modernization, and intentional-anachronism boundaries for historical style without reducing it to decorative markers;
- maintain Stable, Gradual, or Phase-based stylistic evolution through author-approved Proposed, Confirmed, and Superseded state;
- develop topic-neutral fiction inside Unsloop Write through discovery, creative contract, foundation, architecture, scene design, drafting, revision, and handoff;
- scale fiction controls from a minimal in-context scene brief to an author-approved portable `story/` and `manuscript/` project;
- offer Guided, Adaptive, or Autonomous collaboration while preserving locked author decisions and requiring explicit retcons for Confirmed canon;
- resume sustained fiction from compact Markdown state without treating conversational memory as authoritative;
- onboard existing manuscripts without destructive migration, assign stable internal units, and confirm extracted state before promotion;
- accept, partially accept, reject, revise, branch, merge, or retcon fiction while protecting active canon and recoverability;
- provide focused fiction Review and Audit contracts rather than an unfocused all-purpose critique;
- initialize, check, checkpoint, and assemble approved fiction projects through optional portable tooling;
- prepare bounded manuscript, synopsis, query, blurb, pitch, series-summary, and submission-checklist handoffs;
- maintain separate versioned personality, tone, and speaking-style profiles for recurring fictional characters, with author-defined settings, provisional contextual suggestions, drift review, and explicit override;
- maintain sustained non-fiction through Guided, Adaptive, or Autonomous collaboration, approved `writing/` and `manuscript/` state, stable units, bounded resumption, deterministic assembly, and recoverable revision;
- develop biography and documentary narratives plus procedures, policies, plans, directions, instructions, and technical documentation with form-specific authority and validation controls;
- acquire evidence from user-supplied material, approved sites, the broad web, or a hybrid corpus while retaining claim-specific source suitability, confidence, scope, and overrides;
- compose with domain, data, research, and artifact-format skills through explicit authority and non-duplicative intake;
- isolate instructions and active content embedded in retrieved or supplied evidence;
- preserve reproducible lineage for numerical claims, interview testimony, OCR, transcripts, images, audio/video, spreadsheets, and other transformed media;
- architect and maintain documentation systems through canonical ownership, navigation, dependencies, reader validation, correction, deprecation, withdrawal, and archival;
- link claims, sources, quotations, conflicting evidence, verification freshness, and manuscript locations without confusing citation presence with support;
- classify and disposition material changes while preserving accepted scope, strong prose, and prior recoverable state;
- reconcile multi-stakeholder directions and feedback through explicit authority, decision ownership, and version-specific approval;
- translate, localize, or adapt writing across languages while preserving meaning, claim strength, attribution, terminology, uncertainty, and bounded voice evidence;
- return optional machine-readable findings and project-state snapshots without weakening evidence, readiness, or privacy limits;
- run from the same portable Agent Skills core across Codex, Claude, Pi, other compatible harnesses, and manually adapted text-capable models without changing its integrity or voice method; and
- ask once before persistent writing whether to preserve append-only response batches or overwrite current artifacts, then carry that policy through portable project state without expanding revision authority.

Unsloop cannot:

- prove AI authorship from prose style;
- combine stylistic scores, text measurements, voice mismatch, provenance, or detector output into an AI-authorship probability;
- convert a similarity score into a plagiarism verdict;
- establish that no borrowing occurred when the comparison corpus is incomplete;
- verify a source it cannot access;
- decide institutional discipline, publication sanctions, or legal liability;
- disguise AI involvement or help evade detection systems;
- silently change confirmed story canon, locked creative decisions, or an existing fiction-project layout;
- guarantee manuscript originality or continuity beyond the sources and manuscript ranges actually inspected;
- infer batch acceptance from silence, overwrite an existing project or checkpoint, or claim simulated feedback represents real readers or a community;
- treat a bibliography entry, schema-valid file, addressed comment, or fluent translation as proof of source consultation, evidentiary support, approval, or cultural authority;
- claim that delivered writing was rehearsed, accurately timed, rendered, playable, accessible, synchronized, or platform-ready when the corresponding check was not performed;
- silently carry verification across a materially changed claim or apply rejected revision content;
- silently alter audited claims, positions, recommendations, conclusions, scope, certainty, evidence strength, chronology, quantities, attribution, causality, conditions, exceptions, or exclusions;
- promise exact replication of a person, infer identity from style, or use voice samples as authority for new facts or personal experiences;
- claim historical or cultural authenticity from surface conventions alone, flatten multiple periods into a preset, or silently change a Confirmed Style Direction; or
- claim that logical response-batch history is operating-system, tamper-proof, legal-records, or WORM immutability, or silently replace an existing history batch.

## Definition of success

A successful Unsloop result is:

- **Text-grounded:** findings point to actual language, structure, claims, or sources.
- **Calibrated:** conclusions do not exceed the available evidence.
- **Authorship-calibrated:** prose-only audits say authorship is not assessable, while direct assistance evidence is limited to the process stage and artifact range it actually documents.
- **Actionable:** the writer knows what to keep, investigate, and change.
- **Voice-preserving:** revision retains the writer's position and useful idiosyncrasies.
- **Perspective-honest:** useful author-supplied observations, interpretations, unresolved questions, and tentative perspectives remain scoped to their actual basis instead of being deleted for lacking external verification or mislabeled as fact.
- **Structurally coherent:** visible section boundaries express a legible relationship without forced smoothing or loss of intentional pacing.
- **Delivery-honest:** timing, media, interaction, questions, audience fit, and closing movement reflect the actual planned experience, while estimates remain distinct from observed delivery.
- **Format-consistent:** authoritative content and required derivatives expose freshness and actual validation rather than relying on filenames or export success.
- **Voice-defensible:** any claimed alignment identifies its sample basis, observable target traits, confidence, and limits.
- **Style-defensible:** selected conventions, authenticity stance, evidence basis, voice-channel boundaries, evolution state, and intentional deviations remain inspectable.
- **Economical:** the review does not bury important findings in commentary.
- **Transparent:** verified facts, inferences, and unknowns are clearly separated.
- **Goal-directed:** the result serves the stated reader outcome and is calibrated to the audience's prior knowledge and context.
- **Requirement-complete:** required directions and content are visibly satisfied or reported as unresolved.
- **Emotionally responsible:** warmth and conviction are proportionate; manipulation does not substitute for reasons or evidence.
- **Readiness-honest:** provisional work is not presented as final or fully verified.
- **Harness-neutral:** provider, model, and tool differences affect available capabilities and confidence, not the governing method.
- **Fiction-resumable:** sustained story work preserves accepted canon, proposed discoveries, current state, and the next action in portable author-readable Markdown.
- **Recoverable:** consequential story changes identify downstream impact and preserve a usable path back to the prior accepted state.
- **Stage-honest:** critique, assembly, and publication-support artifacts state what was actually inspected and do not imply professional, legal, market, or acceptance certification.
- **Non-fiction-resumable:** sustained factual writing preserves authoritative versions, accepted sections, relevant provenance, decisions, and the next action in portable Markdown.
- **Provenance-aware:** current claims and quotations expose their inspected support, conflicts, freshness, and unresolved actions.
- **Collaboration-honest:** comment resolution, contributor input, and schema validity do not masquerade as approval or verification.
- **Language-aware:** multilingual work preserves meaning and evidence while disclosing ambiguity, translation status, and voice limits.
- **Composable:** domain and artifact specialists retain their authority while Unsloop adds integrity and voice without duplicate intake.
- **Instruction-isolated:** retrieved evidence cannot redefine permissions, tools, scope, or project state.
- **Evidence-reproducible:** numerical, interview, and multimodal support retains its inputs, permissions, transformations, coverage, and uncertainty.
- **Operationally maintainable:** documentation dependencies, corrections, lifecycle state, and actual reader-validation method remain inspectable after publication.
- **Audit-preserving:** the inspected artifact remains unchanged and every proposed correction exposes its semantic effect, authorization, and disposition.
- **History-transparent:** persistent work identifies whether it preserves response batches or overwrites current artifacts; immutable batches expose their boundaries, paths, hashes, and lineage without changing revision permissions.

## Non-goals for v0.1

- A universal AI detector
- An automated plagiarism verdict
- A single opaque quality score
- A blacklist of forbidden vocabulary
- Random “humanizing” through errors, slang, fragments, or fabricated anecdotes
- Mechanical synonym substitution to reduce similarity
- A rigid intake questionnaire that repeats questions the user has already answered
- A mandatory plotting framework, moral, story formula, or novel-scale project setup for every fiction request
- Mandatory project files for short non-fiction, mandatory Git, or a required cloud research database
- Automatic approval, legal clearance, cultural representation, or schema-based quality certification
- A replacement for qualified domain, statistical, interview-ethics, security, accessibility, legal, or artifact-format validation
- A legal records-management, WORM-storage, backup, or disaster-recovery system

## Specification relationship

This charter summarizes the product intent without duplicating the normative requirement catalog. Proposed changes to scope or business outcomes begin in [`BRD.md`](BRD.md); user-visible behavior changes begin in [`PRD.md`](PRD.md); workflow and validation changes begin in [`FSD.md`](FSD.md). Durable tradeoffs belong in [`DECISIONS.md`](DECISIONS.md).
