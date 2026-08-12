# Business Requirements Document

> **Product:** Unsloop · **Status:** v0.1 baseline
>
> **Authority:** Defines why Unsloop exists, who it serves, and the business outcomes it must protect. Product behavior belongs in [`PRD.md`](PRD.md); implementation behavior belongs in [`FSD.md`](FSD.md).

## Purpose

Unsloop is a portable writing-integrity and human-voice system. It helps a writer, editor, researcher, or collaborator produce writing that is original, supportable, specific, readable, and recognizably theirs without turning stylistic signals or similarity scores into unsupported verdicts.

## Business problem

AI-assisted and source-informed writing creates two related but distinct risks:

1. **Integrity risk:** attribution, paraphrase, evidence, citation, or structure may remain too dependent on a source.
2. **Voice risk:** prose may become generic, formulaic, over-polished, emotionally manufactured, or detached from the writer's actual judgment.

Existing detector-centered approaches do not solve either problem reliably. A useful system must evaluate observable text and available evidence, preserve accountable human authorship, and clearly state what it cannot establish.

## Vision and value proposition

Unsloop should make writing more defensible without laundering its origins, more human without manufacturing quirks, and more polished without erasing the writer. Its value is a repeatable method that combines integrity review, voice-aware drafting, and evidence-bounded auditing in one coherent system.

## Stakeholders and users

| Stakeholder | Need |
|---|---|
| Writer | Improve a draft or create new writing while retaining intent, position, and natural language. |
| Editor or collaborator | Diagnose high-value problems consistently without rewriting sound prose unnecessarily. |
| Researcher or educator | Compare drafts with sources and separate textual evidence from misconduct judgments. |
| Project maintainer | Evolve one portable, testable source of truth without divergent skill copies. |
| Affected reader or institution | Receive writing whose evidence, attribution, uncertainty, and authorship claims are not misrepresented. |

## Business requirements

| ID | Requirement | Business outcome |
|---|---|---|
| BR-001 | Evaluate writing integrity through observable source relationships, attribution, evidence quality, and source dependence. | Material integrity risks become inspectable and correctable. |
| BR-002 | Evaluate human voice through specificity, authorial presence, consistency, formulaicity, abstraction, redundancy, example function, and emotional integrity. | Generic or manipulative prose improves without crude word bans. |
| BR-003 | Keep the writer in control of meaning, claims, voice, and final acceptance. | Assistance remains author-led and accountable. |
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

## Scope

### In scope

- Constructive review of supplied writing.
- Author-led drafting and revision.
- Source comparison, attribution review, claim checking, and evidence-bounded audit.
- Topic use, refinement, or brainstorming for new writing.
- Evidence-based matching of the user's authorized voice.
- Requirement coverage, constraint checking, calibrated scoring, and readiness reporting.
- Repository-local discovery, optional global linking, and dependency-free validation.
- Standards-based use across compatible harnesses, with capability fallbacks for hosts that lack a preferred tool or UI.

### Out of scope

- AI-authorship classification from prose style.
- Automated plagiarism, disciplinary, legal, hiring, or publication verdicts.
- Guaranteed originality against an incomplete source corpus.
- Exact voice replication or unauthorized impersonation.
- Detector evasion, fabricated citations, experiences, emotions, or verification.
- Mandatory cloud services, persistent user profiles, or collection of writing samples by default.

## Success measures

For v0.1, success is demonstrated through traceable documentation, passing structural validation, and controlled use in which outputs are text-grounded, calibrated, actionable, voice-preserving, goal-directed, requirement-complete, emotionally responsible, and readiness-honest.

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
