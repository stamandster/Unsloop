# Harness and Model Compatibility

Read this file when adapting Unsloop to a new agent harness, when a preferred tool is unavailable, or when model capability limits affect the requested depth.

## Preserve the portable contract

Keep `SKILL.md` and its relative `references/` as the authoritative operational package. Do not make the method depend on a provider, model family, proprietary tool name, hidden reasoning format, invocation syntax, or UI control.

Harness adapters may define discovery paths, invocation commands, optional metadata, and tool mappings. They must not change Unsloop's evidence rules, voice safeguards, classifications, readiness states, or prohibitions.

## Negotiate capabilities

At the start of a task, use the capabilities already exposed by the host. Map the semantic need to any equivalent native mechanism:

| Need | Preferred capability | Required fallback |
|---|---|---|
| Short consequential choice | Structured choice or question tool | Ask the same options in concise plain text. |
| Read a draft or source | File, attachment, repository, or document access | Ask the user to paste or attach the needed material. |
| Verify an external source | Browser, search, retrieval, or connector | Mark the claim unverified and request the source or permission to continue elsewhere. |
| Enforce a scoped research corpus | Domain/site filter or navigation restricted to approved locators | Request exact pages or visit only approved locators; do not substitute general web search. |
| Edit an artifact | Native patch, file-edit, or document tool | Return a clearly delimited revision for the user to apply. |
| Persist a voice profile | Authorized memory or storage mechanism | Keep the profile task-local; do not persist it. |
| Maintain a writing project | Repository or document editing | Return the proposed or updated Markdown records for the user to save; keep all paths relative. |
| Extract or inspect non-text evidence | Format, document, media, spreadsheet, OCR, or transcription tool | Request a native export or mark extraction incomplete; preserve the original-to-text transformation boundary. |
| Count or constrain output | Reliable tokenizer, document statistics, or validation tool | Use a disclosed estimate and retain a safety buffer. |

Do not switch harnesses, models, execution modes, or accounts merely to obtain a preferred interface. Ask before a switch that changes cost, privacy, permissions, or external data handling.

## Adapt to model capability

- Use any text-capable model that can follow the skill and access the necessary materials. Multimodal input is optional unless the task depends on an image or scanned page.
- Scale task size, evidence volume, and review depth to the available context and tool limits. Process sections explicitly when the full corpus cannot fit safely.
- Prefer direct evidence and compact intermediate records over reliance on long conversational recall.
- For manuscript-scale fiction, resume from `story/STATUS.md` and only the relevant story records and manuscript range. State the inspected boundary and do not make global continuity claims from partial context.
- For sustained non-fiction, resume from `writing/STATUS.md` and only the relevant claims, sources, requirements, decisions, changes, and manuscript range. Do not carry verification or approval across uninspected revisions.
- For recurring fictional speakers, load only applicable Confirmed `CVP-*` profiles and current relationship or knowledge state; keep model suggestions Proposed.
- For documentary or controlled documentation, preserve the artifact family, authority, source policy, exact corpus, validation status, and maintenance state across model or harness transfers.
- When another skill owns domain or artifact behavior, apply [skill-composition.md](skill-composition.md); do not duplicate its intake or overrule its specialized validation.
- Do not weaken integrity, attribution, privacy, authorization, or uncertainty rules for a smaller or less capable model.
- Treat model-generated judgments as decision support. Different models may vary in precision and consistency; compatibility does not guarantee equivalent output quality.
- Never request or expose private chain-of-thought. Report conclusions, evidence, assumptions, and concise rationale instead.

## Harness notes

- **Codex:** Keep repository discovery at `.agents/skills/unsloop`. Retain `agents/openai.yaml` as optional Codex UI metadata. Use `$unsloop` or implicit invocation and use Codex-native tools when available.
- **Claude Code:** Link or copy the same core to `.claude/skills/unsloop`. Invoke with `/unsloop` or allow description-based activation. Do not add Claude-only frontmatter to the portable core.
- **Pi:** Use `.agents/skills/unsloop`, `.pi/skills/unsloop`, `~/.agents/skills/unsloop`, or `~/.pi/agent/skills/unsloop`. Invoke explicitly with `/skill:unsloop` when needed.
- **Other Agent Skills clients:** Point the harness at the directory containing `SKILL.md` and preserve relative references. Follow the host's documented discovery and invocation rules.
- **Harnesses without Agent Skills discovery:** Load `SKILL.md` as a project or system instruction and make the adjacent `references/` readable on demand. Treat this as an adapter, not a fork of the method.

When a host extension supports extra metadata, tools, hooks, subagents, or dynamic context, keep those enhancements optional. The skill must remain usable from its standard frontmatter, Markdown body, and relative references alone.
