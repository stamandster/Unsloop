# Voice Fidelity

Read this file when the user asks to preserve, recover, match, or write in their voice, or when a review evaluates fidelity to a known voice target.

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

## Keep style separate from content

Use samples to learn how the user writes, not what to claim in a new piece.

- Do not import facts, opinions, anecdotes, biographical details, quotations, or expertise from samples unless the user supplies them for the current task.
- Do not lift memorable sentences or distinctive phrases merely to increase resemblance.
- Treat requested reuse of the user's prior language as self-reuse and flag publication or disclosure concerns when relevant.
- Do not infer sensitive or protected personal attributes from stylistic features.
- Do not invent errors, slang, personal memories, or emotional disclosures as identity signals.

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

