# Voice Fidelity

Read this file when the user asks to preserve, recover, match, or write in their voice, or when a review evaluates fidelity to a known voice target.

Make every voice conclusion auditable from authorized evidence: name the sample basis, describe observable traits, distinguish adaptation from mismatch, and state confidence without claiming identity.

## Establish authority and scope

Treat the user's request to match their own writing as sufficient authorization unless the materials create a concrete reason for doubt. If samples appear to belong to someone else, ask whether the user is authorized to use that voice and describe the task as style adaptation rather than identity impersonation.

Do not promise exact imitation. Aim for evidence-based alignment with observable language choices while keeping the user responsible for the final text.

## Gather enough evidence

Use this evidence order when sources conflict:

1. current explicit instructions;
2. a voice brief the user confirms;
3. representative samples in the same genre and audience;
4. broader samples by the user;
5. the current draft and conversation;
6. genre defaults.

For a substantial or style-sensitive task with weak evidence, request two or three representative samples, preferably about 500–2,000 words total. Ask for samples the user wrote or is authorized to provide, ideally close to the requested genre, audience, and degree of formality.

Do not require samples for a short, low-stakes edit when the current draft already provides enough evidence. If the user declines or cannot provide them, proceed from available evidence and lower the confidence label.

Use a concise request such as:

> If you want a closer voice match, send two or three pieces you wrote—ideally in a similar setting. About 500–2,000 words total is enough. I will use them to infer style, not import their facts or personal details.

## Build a bounded voice brief

Extract only observable, task-relevant traits:

- register and degree of formality;
- directness and typical level of explanation;
- sentence and paragraph cadence;
- vocabulary range and technical density;
- first-, second-, or third-person habits;
- certainty, hedging, warmth, humor, and emotional restraint;
- transition and signposting habits;
- punctuation, typography, and contraction preferences;
- rhetorical habits such as examples, questions, contrast, or repetition;
- preferred expressions and expressions the user avoids;
- useful irregularities that should survive editing.

Separate stable traits from genre effects. A formal report and a personal message by the same person may legitimately sound different.

Summarize the brief internally before writing. Show it to the user when the task is long, high-stakes, the samples conflict, or the user asks to approve the profile.

For each material target trait, retain a simple basis: an explicit instruction or a recurring pattern across the authorized evidence. Drop a trait that rests on one incidental phrase unless the user confirms it.

## Keep style separate from content

Use samples to learn how the user writes, not what to claim in a new piece.

- Do not import facts, opinions, anecdotes, biographical details, quotations, or expertise from samples unless the user supplies them for the current task.
- Do not lift memorable sentences or distinctive phrases merely to increase resemblance.
- Treat requested reuse of the user's prior language as self-reuse and flag publication or disclosure concerns when relevant.
- Do not infer sensitive or protected personal attributes from stylistic features.
- Do not invent errors, slang, personal memories, or emotional disclosures as identity signals.

## Separate fiction voices

For fiction, keep these targets distinct:

- **Author voice evidence:** observable tendencies supported by the user's authorized writing samples.
- **Narrative voice:** the designed register, distance, texture, rhythm, and reliability of this story.
- **Viewpoint voice:** the perceptions, vocabulary, assumptions, and attention available to the current viewpoint character.
- **Dialogue voice:** character-specific speech shaped by background, relationship, immediate objective, and emotional state.

The narrative voice may intentionally differ from the user's ordinary nonfiction or conversational voice. Prefer fiction samples in a similar form when close author fidelity matters, but follow the approved project design over irrelevant habits from another genre.

When a historical, literary, rhetorical, house, or custom style also applies, keep it in a separate `StyleBrief` through [style-direction.md](style-direction.md). The selected style may adapt the user's voice for a form or period, but it does not replace the evidence basis for author-voice fidelity.

For multiple recurring speakers, separate viewpoint-character interior voice from spoken dialogue and maintain a versioned profile for each character. A Confirmed profile is immutable for drafting until the author approves a named evolution or retroactive override. Stress, intimacy, deception, formality, or character growth can change surface expression only within the profile's accepted range. Read [character-voice-continuity.md](character-voice-continuity.md).

When asked to write in the style of another identifiable author, convert the request into broad, non-exclusive traits such as pacing, formality, sentence movement, narrative distance, imagery density, or humor. Prefer a tradition-level profile or a representative multi-source corpus when the user wants a historical style. Do not reproduce signature phrases, protected characters, distinctive worlds, or recognizable rhetorical sequences, and do not describe the result as an exact imitation.

## Resolve conflicts

Follow the current request over older samples. Follow purpose and audience over habits that would make the new artifact ineffective or inappropriate. When a conflict would materially change the result, name it and ask the user which direction to prefer.

## Report basis and confidence

When fidelity is material, record:

- **Basis:** which instructions, draft, and sample types informed the result;
- **Target traits:** the few observable traits that drove the writing;
- **Confidence:** Low, Moderate, or High;
- **Limits:** conflicting genres, insufficient text, heavy source constraints, or missing context.

Use **High** only when multiple representative samples agree with the current instructions. Use **Moderate** when one adequate sample or a strong current draft defines the target. Use **Low** when relying mainly on brief conversation, generic preferences, or conflicting samples.

Never turn confidence into a claim that the result is indistinguishable from the user's unaided writing.

## Protect samples

Use the minimum sample text needed. Do not reproduce unnecessary passages in the output. Do not place samples or extracted profiles in project files, memory, or external services unless the user explicitly authorizes that storage or transfer.

For a persistent fiction project, do not create `story/VOICE.md` without explicit authorization. If authorized, store only the approved distilled traits, evidence basis, confidence, and limits—not the source samples or their private content.
