# Writing Brief

Read this file before substantial drafting, revision, review, or audit. Use it progressively: extract what is already known, infer only low-risk details, and ask about material gaps rather than administering a fixed questionnaire.

The brief is an operational decision record, not a form the user must complete. Include only fields that affect the current artifact and keep unresolved material choices visible through delivery.

## Contents

- [Start with topic status](#start-with-topic-status)
- [Adapt the brief for fiction](#adapt-the-brief-for-fiction)
- [Build the brief](#build-the-brief)
- [Establish the direction hierarchy](#establish-the-direction-hierarchy)
- [Classify certainty](#classify-certainty)
- [Ask proportionately](#ask-proportionately)
- [Ask concisely](#ask-concisely)
- [Apply by mode](#apply-by-mode)
- [Run the success test](#run-the-success-test)

## Start with topic status

At the beginning of a new writing request, determine whether the user:

1. already has a topic;
2. has a rough subject or direction that needs refinement; or
3. wants to brainstorm topics from scratch.

If the request, draft, title, outline, or supplied material already makes the topic clear, use it and do not ask the user to repeat it. If the topic is not clear, begin with one compact question:

> Do you already have a topic, have a rough direction you want to refine, or would you like to brainstorm topics together?

When the host exposes a structured user-input tool—such as `request_user_input` in Codex—or an equivalent choice control in the current mode, use it instead of rendering that choice as ordinary prose. Use this structure:

- **Header:** `Topic path`
- **Question:** `How would you like to establish the topic for this writing?`
- **Option 1:** `Use my topic (Recommended)` — Use the topic the user already has and proceed to its boundaries and goal.
- **Option 2:** `Refine a direction` — Turn a rough subject or early idea into a focused topic.
- **Option 3:** `Brainstorm topics` — Generate distinct possibilities from the user's interests, purpose, and constraints.

Wait for the selection before following that branch. If the structured tool is unavailable, ask the same three-way choice conversationally. Do not change the host's collaboration or execution mode solely to obtain a structured prompt, and do not imply that a selector was shown when it was not.

Follow the selected path:

- **Existing topic:** capture the topic and any stated boundaries, then continue the brief.
- **Rough direction:** identify the central subject, intended outcome, and promising angle; offer a small set of clearer topic formulations when useful.
- **Brainstorm from scratch:** ask only for the minimum useful seed context—normally interests or subject area, purpose, audience, and important constraints. Then propose genuinely distinct topic options, not superficial rewordings of one idea.

For brainstormed options, briefly identify each topic's angle, likely reader value, scope, and evidence needs. Help the user choose based on fit with the goal, audience, available knowledge or sources, originality, and feasibility. Treat every option as a proposal, not as a verified factual claim. After the user selects or approves a topic, continue the progressive brief.

For Review or Audit of supplied writing, normally infer the topic from the material. Ask for confirmation only when ambiguity would materially affect the assessment.

## Adapt the brief for fiction

For fiction, treat a topic as any usable story seed: a premise, subject, image, conflict, character, setting, genre idea, or story question. Treat the goal as both the artifact outcome and the intended reader experience; do not force a moral, lesson, or market category.

For an isolated scene or short exploratory piece, ask only what is needed to write that unit. For sustained fiction, also resolve the form and scale, premise, genre and tonal range, narration, ending direction when material, content boundaries, research boundary, starting state, and collaboration cadence. Read [fiction-workflow.md](fiction-workflow.md) for the complete project workflow and portable state contract.

When brainstorming fiction, make the options differ in narrative engine, central pressure, likely form or genre, intended experience, scope, or research burden. Do not disguise one plot as several choices.

## Build the brief

Capture these fields when they matter:

1. **Topic:** the subject and its relevant boundaries.
2. **Goal:** what the reader should know, understand, believe, feel, decide, or do afterward.
3. **Audience:** the actual reader or decision-maker, including relevant needs, concerns, resistance, emotional situation, relationship to the writer, and desired response.
4. **Prior knowledge:** what the audience already knows, assumes, misunderstands, or needs explained.
5. **Context:** the occasion, channel, surrounding conversation, stakes, relationship, and reason the writing is needed now.
6. **Governing directions:** assignment notes, client or editor instructions, policies, templates, rubrics, cautions, required emphasis, and other directions that control the artifact.
7. **Content roles:** facts, claims, examples, evidence, quotations, arguments, conclusions, or calls to action classified as required, optional supporting, background only, or excluded.
8. **Exclusions:** information, claims, framing, disclosures, implications, or source uses to avoid.
9. **Reference material:** notes, documents, links, data, sources, and earlier discussions that may support the content; identify which are authoritative for facts and which merely provide leads.
10. **Voice target:** tone, formality, language style, emotional restraint, and any authorized writing samples.
11. **Style direction:** when material, the selected historical, literary, rhetorical, house, custom, or genre-default profile; authenticity stance; evidence basis; and stable, gradual, or phase-based evolution.
12. **Format and delivery constraints:** length or duration, structure, citation style, template, platform, deadline, live or recorded setting, pace when material, pauses, interaction, media, accessibility needs, authoritative source format, required derivatives, validation expectation, and any component allocations.
13. **Persistent write policy:** when files will be created or changed, Immutable versions or Overwrite current; response-batch scope and accepted native equivalent when applicable. Resolve it before the first write rather than treating it as a stylistic preference.

For fiction, map these general fields to the fiction-specific brief without duplicating them. In particular, keep real-world research references separate from story canon, and keep author voice evidence separate from narrative and character voice design.

Do not collapse these fields. Topic is not goal. Audience is not prior knowledge. Governing directions are not factual evidence. Factual references are not voice samples. Author voice is not a selected literary or historical style. Context is not permission to invent facts.

When style materially shapes the artifact, read [style-direction.md](style-direction.md). Use an explicit direction without a redundant question. If the direction is open, distinguish My evidenced voice, Historical or literary tradition, Custom designed style, and Genre default. A period label does not establish authenticity, and a named author does not authorize signature imitation.

### Classify content roles

- **Required:** must appear or be satisfied for the artifact to meet the brief.
- **Optional supporting:** may improve the artifact when it earns its space and serves the goal.
- **Background only:** informs understanding but should not be forced into the artifact.
- **Excluded:** must not appear or be used in the prohibited way.

Do not treat all supplied material as required. Do not criticize the omission of optional or background material merely because it was available.

### Classify constraints

- **Hard constraint:** a mandatory ceiling, floor, format, policy, deadline, or structural requirement.
- **Working target:** a preferred aim that may be adjusted transparently.
- **Allocation:** a section or component budget within the whole.
- **Safety buffer:** reserved capacity for quotations, citations, captions, delivery variation, or other real use.

When allocations exist, compare their total with the overall constraint. Do not silently redistribute them or solve an overrun by assuming hidden capacity.

For timed or performed work, count every material delivery element rather than equating manuscript word count with duration. Read [delivery-and-presentation.md](delivery-and-presentation.md) when pace, pauses, quotations, readings, questions, media, demonstrations, interaction, or synchronized formats affect feasibility or readiness.

## Establish the direction hierarchy

Use this order while respecting any higher-level safety or legal obligation:

1. non-waivable institutional, contractual, publication, or policy requirements;
2. the user's current explicit instructions;
3. applicable assignment, client, editor, template, rubric, or source-level directions;
4. user-confirmed brief decisions;
5. genre conventions and defaults.

When two directions conflict, identify the conflict instead of silently choosing. Ask the user when they have authority to resolve it; otherwise explain the controlling constraint. A direction can govern selection, tone, emphasis, or structure, but it does not verify a factual claim.

## Classify certainty

For each material field, use one of these states:

- **Known:** explicitly supplied by the user or authoritative material.
- **Inferred:** reasonably suggested by the request, draft, or genre but not confirmed.
- **Unknown:** absent, contradictory, or too uncertain to rely on.

Never upgrade an inference to known without support. When an inference matters, state it or ask for confirmation.

## Ask proportionately

Do not repeat questions the user has already answered. Ask only when the answer could materially change:

- factual accuracy or evidence requirements;
- the main claim, selection, or ordering of content;
- the expected level of explanation;
- tone, formality, or relationship risk;
- privacy, confidentiality, policy, or legal exposure;
- the artifact's format or practical usefulness.

For a short, low-stakes edit, infer the obvious brief and proceed. For substantial drafting, ask the smallest useful batch of missing questions before writing. If the user declines to answer, proceed where safe and label consequential assumptions.

Pause when a missing fact, authorization, required source, or high-stakes choice cannot be safely inferred. Do not use a plausible guess to fill a factual or policy gap.

For substantial, high-stakes, or tightly constrained work, confirm the intended direction in one short paragraph before drafting. Include the reader outcome, audience conditions, governing baseline, hard constraints, and any unresolved decision. Skip this confirmation for quick edits or when it would merely repeat settled information.

## Ask concisely

### Prefer structured choices when available

Use a native structured control, including `request_user_input` when Codex provides it, when all of these are true:

- the answer is needed before the next meaningful step;
- the question has two or three genuinely mutually exclusive choices;
- a short label and one-sentence description can explain each choice; and
- the structured tool is available in the current mode.

Ask no more than three short questions in one structured prompt. Put the recommended option first and mark it `(Recommended)`. Make the recommendation contextual rather than arbitrary. Do not use a selector for an open-ended response such as the user's actual topic, source material, draft text, factual background, or writing samples; request that material conversationally after the relevant choice.

For a consequential choice, give a compact decision brief before asking: state the recommendation, one reasonable alternative when one exists, the material tradeoff, and any effect on the goal, evidence, length, tone, or readiness. Do not invent balance when only one option is responsible or authorized.

If no structured input tool is available, present the same choices in concise plain text and wait for the user's answer. Preserve the same wording and decision structure across both interfaces. Never switch modes merely to gain a preferred question UI.

Treat the structure—not the tool name—as normative. Use a compact fallback prompt such as:

> I can use what you already supplied. The remaining points that would materially change the draft are: (1) what should the reader do or understand afterward, (2) what they already know, and (3) which facts or sources must be included. If you prefer, I can proceed with clearly stated assumptions.

Do not ask every brief field unless the request genuinely leaves all of them unresolved.

## Apply by mode

### Unsloop Write

Resolve topic status first. Establish the goal, governing baseline, content roles, audience knowledge and concerns, authoritative references, and hard constraints before substantial drafting. Make each section serve the goal. Explain only what the audience needs, and do not omit necessary context merely to sound concise.

### Unsloop Review

Infer the draft's apparent topic, goal, audience, and context. State a material uncertainty before judging effectiveness. Review against the intended outcome, not against a generic ideal of polished prose.

### Unsloop Audit

Record the intended function of the writing, governing directions, content roles, source or policy boundary, and authoritative inspected version. A persuasive, pastoral, commercial, academic, or personal goal never lowers the evidence standard. Distinguish required content supplied by the user from claims actually supported by sources. Leave the inspected artifact unchanged and treat correction as a separate revision decision.

## Run the success test

Before delivery, ask:

> Does this writing accomplish its stated goal for this audience, given their prior knowledge, concerns, and actual context, while following governing directions, including required content, using optional material selectively, and respecting the evidence, exclusions, voice, and hard constraints?

If not, revise or explain the unresolved limitation.

Also confirm that every required item and hard constraint has an observable place in the artifact or an explicit unresolved status. Do not treat fluent prose as evidence that the brief was satisfied.
