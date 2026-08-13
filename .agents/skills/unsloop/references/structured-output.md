# Structured Output

Read this file when the user or downstream system needs JSON, CSV, tables, issue records, or another machine-readable Unsloop result.

## Preserve the human contract

Structured output must preserve the same evidence, uncertainty, readiness, privacy, and ethics boundaries as prose. A valid schema does not make a finding correct or verified.

Use the supplied schema when one governs. Otherwise use the bundled `assets/schemas/unsloop-report.schema.json` as an optional interchange contract.

## Core record

Include:

- schema version and Unsloop mode;
- artifact identifiers and inspected boundary;
- requested outcome and review depth;
- evidence status and limitations;
- findings with stable IDs, locations, observation, classification, consequence, evidence, confidence, severity, preservation target, and smallest useful action;
- requirement, claim, source, quotation, or change records when relevant;
- readiness state and unresolved actions; and
- explicit out-of-scope judgments.

Use `null` or an omitted optional field when evidence is unavailable. Do not invent values to satisfy a schema. Keep human-readable labels alongside codes when interoperability benefits.

## Protect portability and privacy

Use relative project paths, stable IDs, UTF-8, and ISO 8601 dates when dates are required. Avoid embedding full drafts, voice samples, protected source passages, credentials, or unnecessary personal data. Link to authorized local records instead.

## Validate and deliver

Validate syntax and required fields with an available parser or schema validator. If unavailable, disclose that the structure was not mechanically validated. Return the requested structured artifact first, followed by only material limitations or integration notes.
