# Writing Brief

Read this file before substantial drafting, revision, review, or audit. Use it progressively: extract what is already known, infer only low-risk details, and ask about material gaps rather than administering a fixed questionnaire.

## Start with topic status

At the beginning of a new writing request, determine whether the user:

1. already has a topic;
2. has a rough subject or direction that needs refinement; or
3. wants to brainstorm topics from scratch.

If the request, draft, title, outline, or supplied material already makes the topic clear, use it and do not ask the user to repeat it. If the topic is not clear, begin with one compact question:

> Do you already have a topic, have a rough direction you want to refine, or would you like to brainstorm topics together?

When `request_user_input` or an equivalent structured user-input tool is available in the current mode, use it instead of rendering that choice as ordinary prose. Use this structure:

- **Header:** `Topic path`
- **Question:** `How would you like to establish the topic for this writing?`
- **Option 1:** `Use my topic (Recommended)` — Use the topic the user already has and proceed to its boundaries and goal.
- **Option 2:** `Refine a direction` — Turn a rough subject or early idea into a focused topic.
- **Option 3:** `Brainstorm topics` — Generate distinct possibilities from the user's interests, purpose, and constraints.

Wait for the selection before following that branch. If the structured tool is unavailable, ask the same three-way choice conversationally. Do not change collaboration mode solely to obtain a structured prompt, and do not imply that a selector was shown when it was not.

Follow the selected path:

- **Existing topic:** capture the topic and any stated boundaries, then continue the brief.
- **Rough direction:** identify the central subject, intended outcome, and promising angle; offer a small set of clearer topic formulations when useful.
- **Brainstorm from scratch:** ask only for the minimum useful seed context—normally interests or subject area, purpose, audience, and important constraints. Then propose genuinely distinct topic options, not superficial rewordings of one idea.

For brainstormed options, briefly identify each topic's angle, likely reader value, scope, and evidence needs. Help the user choose based on fit with the goal, audience, available knowledge or sources, originality, and feasibility. Treat every option as a proposal, not as a verified factual claim. After the user selects or approves a topic, continue the progressive brief.

For Review or Audit of supplied writing, normally infer the topic from the material. Ask for confirmation only when ambiguity would materially affect the assessment.

## Build the brief

Capture these fields when they matter:

1. **Topic:** the subject and its relevant boundaries.
2. **Goal:** what the reader should know, understand, believe, feel, decide, or do afterward.
3. **Audience:** the actual reader or decision-maker.
4. **Prior knowledge:** what the audience already knows, assumes, misunderstands, or needs explained.
5. **Context:** the occasion, channel, surrounding conversation, stakes, relationship, and reason the writing is needed now.
6. **Required content:** facts, claims, examples, evidence, quotations, arguments, conclusions, or calls to action that must appear.
7. **Exclusions:** information, claims, framing, disclosures, or implications to avoid.
8. **Reference material:** notes, documents, links, data, policies, sources, and earlier discussions that may support the content; identify which are mandatory or authoritative.
9. **Voice target:** tone, formality, language style, and any authorized writing samples.
10. **Format constraints:** length, structure, citation style, template, platform, deadline, and accessibility needs.

Do not collapse these fields. Topic is not goal. Audience is not prior knowledge. Factual references are not voice samples. Context is not permission to invent facts.

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

## Ask concisely

### Prefer structured choices when available

Use `request_user_input` or an equivalent structured control when all of these are true:

- the answer is needed before the next meaningful step;
- the question has two or three genuinely mutually exclusive choices;
- a short label and one-sentence description can explain each choice; and
- the structured tool is available in the current mode.

Ask no more than three short questions in one structured prompt. Put the recommended option first and mark it `(Recommended)`. Make the recommendation contextual rather than arbitrary. Do not use a selector for an open-ended response such as the user's actual topic, source material, draft text, factual background, or writing samples; request that material conversationally after the relevant choice.

If no structured input tool is available, present the same choices in concise plain text and wait for the user's answer. Preserve the same wording and decision structure across both interfaces. Never switch modes merely to gain a preferred question UI.

Use a compact prompt such as:

> I can use what you already supplied. The remaining points that would materially change the draft are: (1) what should the reader do or understand afterward, (2) what they already know, and (3) which facts or sources must be included. If you prefer, I can proceed with clearly stated assumptions.

Do not ask all ten fields unless the request genuinely leaves all ten unresolved.

## Apply by mode

### Unsloop Write

Resolve topic status first. Establish the goal, content boundary, audience knowledge, and authoritative references before substantial drafting. Make each section serve the goal. Explain only what the audience needs, and do not omit necessary context merely to sound concise.

### Unsloop Review

Infer the draft's apparent topic, goal, audience, and context. State a material uncertainty before judging effectiveness. Review against the intended outcome, not against a generic ideal of polished prose.

### Unsloop Audit

Record the intended function of the writing and the source or policy boundary. A persuasive, pastoral, commercial, academic, or personal goal never lowers the evidence standard. Distinguish required content supplied by the user from claims actually supported by sources.

## Run the success test

Before delivery, ask:

> Does this writing accomplish its stated goal for this audience, given their prior knowledge and the actual context, while including the required content and respecting the evidence, exclusions, voice, and format constraints?

If not, revise or explain the unresolved limitation.
