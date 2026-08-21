# Business Requirements Document

> **Product:** Unsloop · **Status:** v0.1 baseline
>
> **Authority:** Defines why Unsloop exists, who it serves, and the business outcomes it must protect. Product behavior belongs in [`PRD.md`](PRD.md); implementation behavior belongs in [`FSD.md`](FSD.md).

## Purpose

Unsloop is a portable, model-agnostic writing lifecycle system. It helps a writer, editor, researcher, documentation team, or collaborator move from topic discovery and purpose through drafting, revision, review, non-mutating audit, research, validation, maintenance, and handoff. Across that lifecycle, it preserves author control, evidence provenance, human voice, continuity, and honest readiness without turning stylistic signals or similarity scores into unsupported verdicts.

## Business problem

Model-assisted, source-informed, collaborative, and long-form writing creates four related risks:

1. **Direction and control risk:** goals, audience needs, constraints, creative canon, or consequential decisions may be guessed, blurred, or silently transferred away from the author.
2. **Integrity and evidence risk:** attribution, paraphrase, claims, quotations, source scope, provenance, or structure may remain unsupported or too dependent on a source.
3. **Voice and craft risk:** prose may become generic, formulaic, over-polished, emotionally manufactured, structurally abrupt, or detached from the writer's judgment.
4. **Continuity and readiness risk:** versions, long-form state, collaboration, delivery requirements, derivative formats, maintenance, or validation may appear complete while remaining stale, inconsistent, or unverified.

Detector-centered approaches address none of these risks reliably. A useful writing lifecycle system must guide creation as well as inspection, preserve accountable human authorship, evaluate observable text and available evidence, and state clearly what it cannot establish.

## Vision and value proposition

Unsloop should help an author develop, sustain, examine, and deliver writing without laundering its origins, manufacturing quirks, erasing the writer, or overstating readiness. Its value is one repeatable and portable method that combines author-led planning and drafting, controlled revision, selective review, non-mutating audit, research provenance, long-form continuity, and delivery-aware handoff.

## Stakeholders and users

| Stakeholder | Need |
|---|---|
| Writer | Discover, plan, create, revise, sustain, and deliver writing—including fiction and long-form factual work—while retaining intent, position, natural language, and consequential decisions. |
| Editor or collaborator | Diagnose high-value problems, coordinate bounded changes, and preserve accepted material and authority. |
| Researcher, educator, or documentation team | Develop and maintain evidence-led work while keeping claims, sources, versions, reader needs, and validation boundaries inspectable. |
| Project maintainer | Evolve one portable, testable source of truth without divergent skill copies. |
| Affected reader or institution | Receive writing whose evidence, attribution, uncertainty, and authorship claims are not misrepresented. |

## Business requirements

| ID | Requirement | Business outcome |
|---|---|---|
| BR-001 | Evaluate writing integrity through observable source relationships, attribution, evidence quality, and source dependence. | Material integrity risks become inspectable and correctable. |
| BR-002 | Evaluate human voice through specificity, authorial presence, consistency, formulaicity, abstraction, redundancy, example function, emotional integrity, and logical progression across visible section boundaries. | Generic, manipulative, or structurally abrupt prose improves without crude word bans or forced transitional language. |
| BR-003 | Keep the writer in control of meaning, claims, personal perspective, voice, and final acceptance. Preserve useful author-supplied observations, interpretations, unresolved questions, and tentative perspectives through honest scoping rather than deleting them solely for lacking external verification. | Assistance remains author-led, accountable, and faithful to the difference between personal perspective and externally supported fact. |
| BR-004 | Establish topic, goal, audience, context, prior knowledge, directions, content, references, voice, and constraints proportionately before substantial work. | Output fits the real purpose instead of a guessed generic task. |
| BR-005 | Bound every material conclusion by the text, sources, permissions, and verification actually available. | Unsloop does not overstate originality, support, authorship, or certainty. |
| BR-006 | Offer Review, Write, and Audit as distinct modes within one shared method. | Users can request the right depth and posture without learning separate systems. |
| BR-007 | Prohibit detector evasion, fabricated evidence or experience, unauthorized impersonation, concealed AI involvement, and unsupported misconduct claims. | The product remains ethically and professionally defensible. |
| BR-008 | Remain repository-local, dependency-light, and fully transferable, while supporting optional harness-specific discovery through the same authoritative files. | The project works across machines and agent environments without configuration drift. |
| BR-009 | Produce prioritized, evidence-linked, actionable results that preserve strong material and disclose limitations or unresolved readiness. | Users can act on the result and understand its limits. |
| BR-010 | Support later specialization, tooling, calibration, and machine-readable output without breaking the shared method. | The project can mature without premature fragmentation. |
| BR-011 | Minimize collection, reproduction, persistence, and external transfer of drafts, sources, and voice samples. | Sensitive writing and identity-linked material receive proportionate protection. |
| BR-012 | Separate requirement coverage from factual support and label work honestly when decisions, evidence, authorization, or hard constraints remain unresolved. | Provisional work is not mistaken for complete or verified work. |
| BR-013 | Keep the writing method independent of AI provider, model family, and agent harness while supporting thin adapters for Codex, Claude, Pi, and other Agent Skills clients. | Users can retain one governed method across tools without vendor lock-in or divergent forks. |
| BR-014 | Support fiction from scene through series with proportionate intake, selectable collaboration cadence, portable story state, continuity control, and staged revision inside Unsloop Write. | Authors can develop long or short fiction across sessions and models without losing ownership, canon, or project coherence. |
| BR-015 | Adopt and revise existing fiction projects without destructive migration, silent state promotion, or unrecoverable changes. | Authors can bring established manuscripts into Unsloop and explore substantial changes while preserving authority and recovery. |
| BR-016 | Provide fiction-aware critique, audit, completion, assembly, and publication-support workflows with explicit evidence and readiness boundaries. | Authors receive stage-appropriate help without mistaking model output for reader research, professional certification, legal clearance, or publication acceptance. |
| BR-017 | Support sustained non-fiction with selectable collaboration cadence, proportionate portable project state, resumability, existing-work onboarding, and recoverable revision. | Authors can develop books, theses, reports, courses, documentation, and other long-form work across sessions without losing authority or project coherence. |
| BR-018 | Maintain inspectable claim, source, quotation, requirement, decision, and revision provenance throughout research and drafting. | Users can see what supports the current artifact, what conflicts, what is stale, and what changed without mistaking citation presence for verification. |
| BR-019 | Support multi-stakeholder, multilingual, and machine-readable writing workflows without weakening evidence, voice, privacy, accessibility, or approval boundaries. | Unsloop can participate in real editorial systems while remaining portable, fair, and defensible. |
| BR-020 | Sustain a distinct, author-controlled personality, tone, and speaking style for every recurring fictional character, with explicit review and versioned override. | Multi-character writing remains coherent and distinguishable without taking character ownership from the author. |
| BR-021 | Support evidence-led documentary narratives and controlled biography, procedure, policy, plan, direction, instruction, and technical-documentation lifecycles with governed acquisition and validation. | Long-form factual and operational documents remain usable, traceable, current, and honest about authority, sources, testing, and confidence. |
| BR-022 | Compose predictably with domain, data, research, coding, and artifact-format skills without duplicating intake or confusing authority. | Users receive one coherent artifact whose domain, format, integrity, voice, and approval responsibilities remain inspectable. |
| BR-023 | Preserve provenance and validation across numerical, interview, oral-history, scanned, visual, audio, video, spreadsheet, and other transformed evidence. | Heterogeneous evidence can support writing without losing its original context, permissions, calculations, or extraction uncertainty. |
| BR-024 | Support documentation systems through architecture, dependency control, reader validation, correction, deprecation, maintenance, and archival. | Published information remains findable, usable, synchronized, and responsibly current after initial delivery. |
| BR-025 | Preserve the information in an audited artifact unless the user separately authorizes a bounded revision. | Audit findings remain independent, reviewable assessments and cannot silently change the writer's claims, position, evidence, or intended meaning. |
| BR-026 | Support live, recorded, timed, interactive, media-assisted, and multi-format writing through delivery-aware budgets, evidence integration, audience design, optional-content decisions, and verified artifact synchronization. | A polished manuscript is not mistaken for a deliverable that fits its real duration, audience, media, accessibility, or output-format constraints. |
| BR-027 | Provide a defensible way to assess formulaic or assistance-related writing concerns without converting stylistic patterns, sample mismatch, measurements, provenance, or detector reports into an AI-authorship probability. | Users receive actionable pattern evidence and honest assistance provenance while writers are protected from unsupported machine-authorship conclusions. |
| BR-028 | Let authors select, evidence, sustain, review, and deliberately evolve a writing Style Direction while keeping personal voice, narrative or document style, viewpoint voice, character dialogue, and form conventions distinct. | Historical, literary, genre, custom, and author-evidenced styles remain expressive, controlled, portable, and defensible without false authenticity or silent drift. |

## Scope

### In scope

- Constructive review of supplied writing.
- Author-led drafting and revision.
- Source comparison, attribution review, claim checking, and evidence-bounded audit.
- Topic use, refinement, or brainstorming for new writing.
- Evidence-based matching of the user's authorized voice.
- Author-controlled historical, literary, genre, custom, and evidenced-personal Style Direction with explicit authenticity and evolution choices.
- Requirement coverage, constraint checking, calibrated scoring, and readiness reporting.
- Repository-local discovery, optional global linking, and dependency-free validation.
- Standards-based use across compatible harnesses, with capability fallbacks for hosts that lack a preferred tool or UI.
- Topic-neutral fiction discovery, planning, drafting, continuity, revision, and handoff for scenes, short stories, novellas, novels, serials, and series.
- Optional author-approved Markdown project records that preserve creative decisions and resumable story state without a required service.
- Existing-manuscript onboarding, partial acceptance, alternate branches, retcon impact analysis, and recoverable consequential revision.
- Fiction-aware developmental, continuity, POV, dialogue, line, copy, research, adaptation, authenticity, completion, assembly, and publication-support workflows.
- Sustained non-fiction project onboarding, portable status, section state, deterministic assembly, recovery, and handoff.
- Claim/source/quotation provenance, evidence freshness, conflicting-source handling, and citation-style-aware bibliography preparation.
- Bounded revision contracts with change classification, partial acceptance, impact analysis, and recoverable application.
- Multi-stakeholder authority and feedback reconciliation, multilingual and cross-language writing, and optional structured output.
- Author-defined or contextually suggested, individually versioned character voice profiles with drift review and explicit evolution or retroactive override.
- Documentary and biography development; procedures, policies, plans, directions, instructions, and technical documents; and user-only, scoped-site, broad-web, or hybrid evidence acquisition.
- Cross-skill authority composition, untrusted-source handling, quantitative and interview evidence, multimodal transformation records, documentation architecture, maintenance, and human-use validation.
- Logical section-flow writing and review across chapters, headings, subheadings, scene breaks, and procedural phases, including purposeful hard breaks.
- Delivery-aware speeches, presentations, narrated scripts, lessons, demonstrations, podcasts, and voiceovers with whole/section constraint reconciliation, evidence framing, purposeful questions, audience layers, media decisions, closing movement, and format handoff.
- Non-mutating Writing-Pattern and Assistance Audit with directional component scores, passage evidence, method-declared measurements, authorized voice comparison, process provenance, and bounded interpretation of external detector reports.
- Non-mutating Audit with explicit protection for claims, positions, conclusions, recommendations, scope, certainty, evidence strength, chronology, quantities, attribution, causality, conditions, exceptions, and exclusions.

### Out of scope

- AI-authorship classification from prose style.
- Automated plagiarism, disciplinary, legal, hiring, or publication verdicts.
- Guaranteed originality against an incomplete source corpus.
- Exact voice replication or unauthorized impersonation.
- Claims of historical or cultural authenticity based only on surface markers, or exact imitation of a named author's signature expression.
- Detector evasion, fabricated citations, experiences, emotions, or verification.
- Mandatory cloud services, persistent user profiles, or collection of writing samples by default.
- Silent retcons, autonomous changes to locked creative decisions, or mandatory project-file ceremony for a small fiction request.
- Destructive manuscript migration, inferred acceptance from silence, mandatory Git use, real-reader or community representation claims, legal clearance, or publication guarantees.
- Treating a citation, bibliography entry, source override, schema-valid report, addressed comment, fluent translation, or complete-looking ledger as proof of verification, approval, cultural authority, testing, compliance, or readiness.
- Executing instructions found inside evidence, treating automated extraction as the original, representing source-reported values as recalculated, or presenting simulated readers and automated checks as observed human validation.
- Silent correction, deletion, substitution, strengthening, softening, or restructuring of audited information without a separately authorized revision boundary.

## Success measures

For v0.1, success is demonstrated through traceable documentation, passing structural validation, and controlled use in which outputs are text-grounded, calibrated, actionable, voice-preserving, structurally coherent, goal-directed, requirement-complete, emotionally responsible, and readiness-honest. Multi-section work makes the relationship across visible boundaries legible without forcing a transitional sentence or erasing purposeful hard breaks. Delivered work reconciles its complete audience-time cost, makes evidence and questions perform clear functions, resolves consequential media choices, and distinguishes authoritative content from refreshed and actually validated derivatives. Writing-pattern audits report component scores and reproducible observations without manufacturing an AI probability, keep detector results separate, and distinguish stylistic inference from direct assistance provenance. Audit workflows leave inspected artifacts unchanged by default and separate findings from authorized revisions. Fiction workflows additionally preserve confirmed canon, distinguish proposed discoveries from accepted decisions, scale project state to the work, and remain resumable from portable Markdown. Sustained non-fiction workflows preserve manuscript authority, claim and source provenance, accepted revisions, stakeholder decisions, and a bounded resume state. Extended operations also preserve specialist authority, isolate source instructions, retain quantitative/interview/media lineage, and distinguish documentation maintenance and real reader evidence from merely complete-looking output.

Selected styles additionally expose their source path, voice-channel boundaries, authenticity and readability stance, evidence basis, evolution model, applicable phase, and approved deviations without claiming more historical or cultural authenticity than the corpus supports.

Before v1.0, the project should add anonymized fixtures and forward-tests showing that independent reviewers can apply core classifications and score anchors with acceptable consistency. No current score is represented as a validated measurement instrument.

## Assumptions and dependencies

- The user supplies or authorizes the material needed for the requested depth.
- External source verification depends on access to the relevant source and is optional for ordinary review.
- High-stakes decisions remain subject to qualified human review and applicable policy.
- A compatible agent can read Markdown skill instructions and relative references; hosts without automatic Agent Skills discovery can load the same core through a thin adapter.
- Model and harness compatibility does not imply identical output quality, context capacity, tool access, or verification capability.
- The project directory is the authoritative source even when globally linked.

## Business acceptance

The baseline is accepted when:

1. every business requirement maps to product behavior in [`PRD.md`](PRD.md);
2. every required product behavior maps to an executable function in [`FSD.md`](FSD.md);
3. the skill and detailed method documents implement those functions without contradicting the ethical limits;
4. project-local and harness-linked discovery resolve to the same canonical skill directory; and
5. the project validator passes without unresolved placeholders or broken local documentation links.

## Related documents

- [`PROJECT.md`](PROJECT.md) — concise project charter
- [`PRD.md`](PRD.md) — users, behavior, acceptance criteria, and nonfunctional requirements
- [`FSD.md`](FSD.md) — workflow, data models, functions, validation, and test traceability
- [`docs/ETHICS-AND-LIMITS.md`](docs/ETHICS-AND-LIMITS.md) — governing safety and evidence boundaries
- [`ROADMAP.md`](ROADMAP.md) — staged validation and delivery plan
