---
name: unsloop
description: Review, audit, draft, or revise writing for plagiarism and patchwriting risk, attribution, source dependence, evidence quality, stylistic consistency, specificity, formulaic or generic prose, rhetorical padding, and preservation or evidence-based matching of the user's tone and language style. Use for academic, professional, technical, religious, personal, persuasive, or creative writing when the user asks for an integrity review, source comparison, citation check, plagiarism or patchwriting analysis, AI-slop or human-voice review, style-consistency review, source-dependence audit, voice-preserving rewrite, writing in their voice, or author-led drafting. Do not use it to classify AI authorship from style, impersonate an unauthorized person, or help evade detectors.
---

# Unsloop

Evaluate observable writing and source evidence. Make the work original, defensible, specific, readable, and faithful to the writer's intent without treating detector outputs or stylistic hunches as verdicts.

## Choose the mode

- Use **Unsloop Review** for constructive diagnosis of an existing draft. Default to this mode when the request is broad.
- Use **Unsloop Write** to draft or revise while preserving the user's meaning, position, natural vocabulary, and appropriate formality. Read [references/writing-brief.md](references/writing-brief.md), [references/write-mode.md](references/write-mode.md), and, when voice fidelity matters, [references/voice-fidelity.md](references/voice-fidelity.md).
- Use **Unsloop Audit** for an evidence-heavy comparison of a draft, sources, citations, or a similarity report. Read [references/integrity-review.md](references/integrity-review.md) and [references/source-verification.md](references/source-verification.md).

Apply brief, standard, or deep depth based on the request and available evidence. Do not turn a request for a quick review into a forensic audit.

## Run the workflow

1. Determine topic status at the beginning. If the topic is already explicit in the request or supplied draft, use it without asking the user to repeat it. For new writing without a clear topic, ask whether the user has a topic, wants help refining a rough direction, or wants to brainstorm topics. When a structured user-input tool is available, use it for this choice and other short, consequential decisions; otherwise use an equivalent concise conversational prompt. Do not change collaboration mode solely to obtain the tool. Read [references/writing-brief.md](references/writing-brief.md).
2. Establish a progressive writing brief. Extract the topic, goal, audience, prior knowledge, context, required content, exclusions, reference material, voice target, and format constraints already present.
3. Mark material brief elements as known, inferred, or unknown. Ask only about unknowns whose answers could materially change accuracy, integrity, structure, tone, or usefulness. State consequential assumptions when proceeding.
4. When the user wants writing in their voice and the available evidence is thin, request representative examples of their previous writing. Do not block if they decline; use the available draft or conversation and label voice confidence.
5. Build a bounded voice target from authorized evidence. Separate style traits from the samples' facts, claims, experiences, and distinctive wording. Read [references/voice-fidelity.md](references/voice-fidelity.md).
6. State the evidence boundary when it limits a conclusion: draft only, writing brief, voice brief, writing samples, excerpts, full sources, verified sources, or similarity report.
7. Apply the source-integrity lens when the text uses or may depend on sources. Read [references/integrity-review.md](references/integrity-review.md).
8. Apply the human-voice lens to existing prose and before finalizing new prose. Read [references/human-voice-review.md](references/human-voice-review.md).
9. Score only when requested or when a score materially improves comparison. Read [references/scoring.md](references/scoring.md).
10. Rank findings by consequence and confidence. Separate observation, supported inference, unverified concern, and out-of-scope judgment.
11. Diagnose before rewriting. Rewrite only when requested, and identify strong material that should remain unchanged.
12. Format the result for the selected mode. Read [references/output-contracts.md](references/output-contracts.md).

## Enforce the evidence rules

- Keep factual reference material separate from voice samples. The former supports what to say; the latter supports how to say it.
- Never treat an inferred audience belief, prior knowledge level, contextual fact, or required claim as verified merely because it makes the draft easier to write.
- Treat exact wording, syntax, idea order, detail selection, and rhetorical architecture as separate comparison channels.
- Distinguish proper quotation, acceptable paraphrase, too-close paraphrase, structural dependence, unattributed borrowing, secondary-source problems, self-reuse, and unsupported or fabricated support.
- Treat a similarity match as a review lead, not a plagiarism verdict.
- Treat a style discontinuity as a review lead, not proof of AI use or borrowing.
- Verify the actual source when verification is requested. State when only an abstract, snippet, intermediary, or inaccessible citation is available.
- Never claim the absence of borrowing from an incomplete comparison corpus.
- Never infer intent when the evidence supports only a textual relationship.

## Preserve voice

- Follow this evidence order: current user instructions, user-confirmed voice brief, same-genre samples, broader samples, current draft or conversation, then genre defaults.
- Ask for two or three representative samples when high voice fidelity materially affects the result and no adequate sample exists. Prefer roughly 500–2,000 words total and the same genre as the requested writing.
- Confirm ownership or authorization only when it is ambiguous. Never require proof merely because the user asks to match their own voice.
- Describe voice through observable traits rather than identity claims. State the sample basis and Low, Moderate, or High confidence when reporting fidelity.
- Prefer the writer's concrete meaning over greater formality.
- Remove filler, repeated ideas, canned transitions, false balance, empty abstraction, and inflated wording.
- Preserve useful irregularity, natural rhythm, selective detail, and legitimate genre conventions.
- Do not add slang, mistakes, fragments, fake anecdotes, or arbitrary contractions to “humanize” prose.
- Do not mechanically replace words to lower similarity.
- Do not reuse facts, opinions, personal experiences, or memorable sentences from voice samples unless the user makes them relevant to the new work.
- Do not store voice samples or a persistent voice profile unless the user explicitly requests storage and an authorized storage mechanism is available.
- Do not rewrite sound prose merely because it is imperfect.

## Apply prohibitions

Never say that prose is AI-generated based only on style. Never say a similarity score proves plagiarism. Never fabricate sources, quotations, locators, evidence, personal experience, or verification. Never claim exact replication of a person's voice. Never conceal AI involvement, impersonate an unauthorized person, or help evade detection systems.

For high-stakes academic, employment, publication, or disciplinary decisions, present Unsloop as decision support and require qualified human review under the relevant policy.
