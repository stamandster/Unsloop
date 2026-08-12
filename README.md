# Unsloop

**Writing integrity and human-voice review.**

Unsloop is a writing-quality project built around a simple idea: judge the text and the evidence, not a detector score or a stylistic hunch.

For new writing, Unsloop begins by determining whether the user already has a topic, has a rough direction to refine, or wants to brainstorm distinct topic options. If the topic is already clear, it does not ask the user to repeat it. When Codex exposes a structured choice control, Unsloop uses it for short, consequential decisions; otherwise it presents the same choices conversationally without changing modes. It then builds a progressive writing brief from what the user has already supplied: topic, goal, audience, prior knowledge, context, required content, exclusions, reference material, voice target, and format constraints. It marks material details as known, inferred, or unknown and asks only about gaps that could change the result.

It supports three related jobs:

- **Unsloop Review** — diagnose clarity, integrity, specificity, and voice.
- **Unsloop Write** — draft or revise while preserving the writer's intent and matching their evidenced tone and language style.
- **Unsloop Audit** — examine source use, attribution, evidence, and source dependence in depth.

The initial implementation is one extensible, repository-scoped Codex skill at [`.agents/skills/unsloop/SKILL.md`](.agents/skills/unsloop/SKILL.md). Codex discovers it from the project itself; no user-level installation or machine-specific path is required. The names above are modes within the shared method and may become separate skills or interfaces once real use shows that separation is useful.

## Start here

- [`PROJECT.md`](PROJECT.md) — vision, principles, scope, and users
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — project and skill structure
- [`docs/NAMING.md`](docs/NAMING.md) — naming system and mode boundaries
- [`docs/REVIEW-MODEL.md`](docs/REVIEW-MODEL.md) — the two-part method
- [`docs/SCORING-RUBRIC.md`](docs/SCORING-RUBRIC.md) — source-dependence and voice-profile scales
- [`docs/REVIEW-OUTPUT.md`](docs/REVIEW-OUTPUT.md) — output contracts
- [`docs/ETHICS-AND-LIMITS.md`](docs/ETHICS-AND-LIMITS.md) — claims Unsloop may and may not make
- [`docs/SOURCES.md`](docs/SOURCES.md) — research and guidance behind v0.1
- [`ROADMAP.md`](ROADMAP.md) — path from v0.1 to a validated release
- [`DECISIONS.md`](DECISIONS.md) — durable design decisions
- [`PORTABILITY.md`](PORTABILITY.md) — discovery, dependencies, and transfer guarantees

## Validate locally

Run the dependency-free project check from the repository root:

```text
python scripts/validate.py
```

The Unsloop skill itself contains only Markdown and YAML and requires no runtime packages. The optional validator uses only the Python standard library.

## Voice matching

For a close match, Unsloop may request two or three representative pieces previously written by the user, ideally in a similar genre. It derives an observable voice brief from those samples while keeping their facts, anecdotes, and distinctive wording out of the new work unless the user explicitly makes them relevant. Voice matching always reports its evidence basis and confidence; it never claims exact replication.

Factual references and voice samples have different jobs: references support what the writing says; samples help establish how it should sound. Unsloop does not treat a sample's claims or experiences as evidence for the new work.

## Status

Version 0.1 is a documented, portable foundation. It is ready for controlled use and forward-testing, but its scoring model is an interpretive rubric—not a validated measurement instrument.
