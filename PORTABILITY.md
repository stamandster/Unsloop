# Portability

## Guarantee

Unsloop's canonical skill lives at `.agents/skills/unsloop`. Copying or cloning the project preserves the skill, its UI metadata, all operational references, the product documentation, and the validation tool as one unit.

No file must be copied into a user profile or global Codex directory.

## Codex discovery

Codex scans `.agents/skills` from the current working directory upward to the repository root. Launch Codex anywhere inside this repository to make the root Unsloop skill available. If a host does not refresh after a file change, restart Codex.

This follows the [official OpenAI documentation for repository-scoped skills](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

## Runtime dependencies

The skill runtime consists only of:

- `SKILL.md`;
- relative Markdown references;
- `agents/openai.yaml` metadata.

It requires no package manager, build step, MCP server, memory service, API key, environment variable, absolute filesystem path, or user-level configuration. Durable project decisions live in the checked-in Markdown documents, so using Unsloop does not depend on MuninnDB or any other external memory system.

External access is optional and task-driven. A normal writing review works offline. An Audit that verifies online sources naturally requires access to those sources.

Interactive presentation adapts to the host. When Codex exposes a structured user-input control, Unsloop can use it for short choices. On hosts or modes without that capability, the same decision is presented as plain text; no UI-specific feature is required for the skill to function.

Voice samples are task inputs, not project dependencies. Unsloop does not place supplied samples or extracted voice profiles in the repository unless the user explicitly asks for that persistence.

## Validation

Run from the project root:

```text
python scripts/validate.py
```

The validator uses only the Python standard library and checks:

- repository-local skill placement;
- frontmatter and skill naming;
- expected UI metadata;
- required project documents and skill references;
- required writing-brief and voice-fidelity safeguards;
- unresolved placeholders;
- broken relative Markdown links;
- accidental machine-specific absolute paths.

Python is not required to use Unsloop; it is required only to run this optional maintenance check.

## Transfer checklist

After copying or cloning the project:

1. Open a terminal anywhere under the project root.
2. Run `python scripts/validate.py` if Python is available.
3. Start or restart Codex in the project.
4. Invoke `$unsloop`, or make a request that matches its description.

Do not create a second global copy with the same skill name. Codex does not merge same-named skills, so duplicate installations can make skill selection ambiguous.
