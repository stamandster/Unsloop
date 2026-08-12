# Project Definition

> **Document role:** Concise project charter. [`BRD.md`](BRD.md) is authoritative for business requirements, [`PRD.md`](PRD.md) for product requirements, and [`FSD.md`](FSD.md) for functional behavior.

## Vision

Unsloop helps writing become more original, defensible, specific, readable, and recognizably human without sanding away the writer's character.

The project addresses two connected problems:

1. **Writing integrity:** plagiarism and patchwriting risk, incomplete attribution, source-dependent structure, weak evidence, and citation problems.
2. **Human voice:** generic phrasing, empty abstraction, formulaic structure, repetition, over-polishing, and loss of the writer's actual point of view.

These problems overlap, but they are not identical. A passage can be fully original and still sound generic. It can also avoid verbatim overlap while following a source's syntax, idea order, incidental details, and rhetorical architecture.

## Product promise

Unsloop evaluates observable features of writing. It does not infer misconduct or machine authorship from style alone.

For substantial work, Unsloop first establishes what the writing is meant to accomplish for a particular audience. It uses a progressive brief, distinguishing what is known, reasonably inferred, and still unknown, so that missing context does not silently become invented content.

Every material finding should answer four questions:

1. What passage or claim is under review?
2. What concrete feature creates concern?
3. What evidence supports the finding?
4. What correction would preserve the writer's meaning and voice?

## Intended users

- Writers revising academic, professional, technical, religious, personal, persuasive, or creative work
- Editors who need a repeatable integrity-and-voice review
- Researchers or educators comparing a draft with supplied sources
- Collaborators who want AI-assisted writing to remain accountable and author-led

## Scope

Unsloop can:

- review a draft without rewriting it;
- compare a draft with supplied or verifiable sources;
- distinguish quotation, acceptable paraphrase, patchwriting, structural borrowing, and unattributed borrowing;
- assess evidence strength and citation placement;
- identify concrete forms of generic or formulaic prose;
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
- test examples for function and persuasive language for emotional integrity;
- distinguish ready work from provisional work that still requires a decision, evidence, or authorization;
- request authorized examples of the user's previous writing when closer voice fidelity would materially improve the result;
- derive a bounded voice brief from observable traits and report the evidence basis and confidence of the match.
- run from the same portable Agent Skills core across Codex, Claude, Pi, other compatible harnesses, and manually adapted text-capable models without changing its integrity or voice method.

Unsloop cannot:

- prove AI authorship from prose style;
- convert a similarity score into a plagiarism verdict;
- establish that no borrowing occurred when the comparison corpus is incomplete;
- verify a source it cannot access;
- decide institutional discipline, publication sanctions, or legal liability;
- disguise AI involvement or help evade detection systems.
- promise exact replication of a person, infer identity from style, or use voice samples as authority for new facts or personal experiences.

## Definition of success

A successful Unsloop review is:

- **Text-grounded:** findings point to actual language, structure, claims, or sources.
- **Calibrated:** conclusions do not exceed the available evidence.
- **Actionable:** the writer knows what to keep, investigate, and change.
- **Voice-preserving:** revision retains the writer's position and useful idiosyncrasies.
- **Voice-defensible:** any claimed alignment identifies its sample basis, observable target traits, confidence, and limits.
- **Economical:** the review does not bury important findings in commentary.
- **Transparent:** verified facts, inferences, and unknowns are clearly separated.
- **Goal-directed:** the result serves the stated reader outcome and is calibrated to the audience's prior knowledge and context.
- **Requirement-complete:** required directions and content are visibly satisfied or reported as unresolved.
- **Emotionally responsible:** warmth and conviction are proportionate; manipulation does not substitute for reasons or evidence.
- **Readiness-honest:** provisional work is not presented as final or fully verified.
- **Harness-neutral:** provider, model, and tool differences affect available capabilities and confidence, not the governing method.

## Non-goals for v0.1

- A universal AI detector
- An automated plagiarism verdict
- A single opaque quality score
- A blacklist of forbidden vocabulary
- Random “humanizing” through errors, slang, fragments, or fabricated anecdotes
- Mechanical synonym substitution to reduce similarity
- A rigid intake questionnaire that repeats questions the user has already answered

## Specification relationship

This charter summarizes the product intent without duplicating the normative requirement catalog. Proposed changes to scope or business outcomes begin in [`BRD.md`](BRD.md); user-visible behavior changes begin in [`PRD.md`](PRD.md); workflow and validation changes begin in [`FSD.md`](FSD.md). Durable tradeoffs belong in [`DECISIONS.md`](DECISIONS.md).
