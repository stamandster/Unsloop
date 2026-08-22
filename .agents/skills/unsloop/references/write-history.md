# Persistent Write Policy and Response History

Read this file before creating or modifying persistent writing artifacts when the user's write policy is not already explicit or recorded for the current project.

## Decide before the first write

Ask once for the applicable task, project, or approved batch:

- **Immutable versions (Recommended):** preserve one append-only snapshot of every persistent writing response or write batch, including every artifact written in that response, while keeping designated current files usable.
- **Overwrite current:** update the designated current artifacts without automatic per-response snapshots. Existing revision authorization, Audit non-mutation, collision refusal, and consequential-change checkpoint rules still apply.

Use a structured selector when the host provides one and a concise plain-text question otherwise. Do not ask when the user already chose a policy or a coherent project record states it. Do not ask for chat-only drafting, read-only Review, non-mutating Audit, or a task that will not write persistent artifacts.

This choice governs storage behavior, not permission to change content. Resolve the authoritative files, revision scope, and semantic authorization separately.

## Define the response batch

A response batch contains all persistent writing artifacts created or materially updated during one assistant response after the user's latest instruction or disposition. Use one stable batch ID for the whole response, including synchronized Markdown, DOCX, PDF, slide, web, audio, ledger, or other writing outputs when they are in scope.

Prefer a portable ID such as `WRT-20260822T143015Z-001`. Do not rely on timestamps alone to determine authority. Record the parent batch when known.

## Preserve immutable versions

For ordinary file projects, use this visible default unless the project already has a coherent version layout:

```text
unsloop-history/
  WRT-20260822T143015Z-001/
    manifest.json
    files/
      manuscript/
        001-opening.md
```

Each batch manifest records:

- batch ID, kind (`baseline` or `response`), creation time, reason, and optional parent batch;
- the write policy and authoritative project root;
- every archived relative path, byte size, and content hash; and
- the fact that current working artifacts are maintained separately from immutable history.

The snapshots are logically immutable: never edit, replace, rename, delete, or reuse an existing batch directory through Unsloop. Do not claim operating-system, WORM-storage, cryptographic-signature, or legal-record immutability unless those controls were actually applied and verified.

Before the first in-place change under this policy, capture a `baseline` batch for every existing writing artifact in scope unless an equivalent accepted baseline already exists. After each writing response, capture one `response` batch containing all artifacts written in that response. New files appear in the response batch; a deleted or intentionally retired artifact remains recoverable from its last recorded batch and its disposition should be reported.

Current working files may be updated so existing tools, links, and manuscript ledgers continue to function. Immutability applies to the historical response snapshots, not to the designated current files. Record the current authoritative version in the applicable status or handoff record without treating the newest timestamp as automatic authority.

If the project uses Git, native document history, tracked changes, or another version system, use it as the response history only when it preserves each requested response batch, exposes the affected files and versions for review, and the user accepts that mapping. A repository commit or document autosave is not automatically equivalent to the selected policy.

## Overwrite current safely

Under **Overwrite current**:

- update only the authorized current files and ranges;
- do not create `unsloop-history/` solely for this policy;
- preserve unrelated user changes;
- retain ordinary before/after explanation when material; and
- still checkpoint consequential, bulk, canon-changing, requirement-changing, evidence-changing, or externally committed revisions.

Overwrite selection never authorizes silent semantic change, Audit mutation, checkpoint replacement, or collision replacement in project tools.

## Persist and change the policy

For a persistent project, record the confirmed policy in `BRIEF.md` or `STATUS.md` after project-file persistence is authorized. For a one-off task, keep it task-local.

The user may change the policy prospectively. Record the effective response or batch. Changing to Overwrite current does not delete earlier history. Changing to Immutable versions begins with a baseline of the then-current artifacts before the next in-place write.

## Use optional tooling

When Python and filesystem access are available, the dependency-free `scripts/write_history.py` helper can preview or create a baseline or response snapshot:

```text
python scripts/write_history.py snapshot --root PATH --batch-id WRT-ID --kind response --reason "Draft response" --include manuscript/001-opening.md
```

The command previews by default and requires `--apply`. It confines paths to the selected root, refuses missing inputs and existing batch destinations, copies all included files beneath `files/`, and writes hashes in `manifest.json`.

When the helper is unavailable, create the same append-only structure manually or use an accepted equivalent native version mechanism. If the selected history cannot be completed, stop further persistent writes, preserve what already exists, and report the incomplete batch honestly rather than claiming full version coverage.

## Return the result

Do not bury the requested writing under version bookkeeping. After the artifact, report only what materially aids review:

- selected write policy;
- current authoritative artifact or version;
- response batch ID and history location when immutable versions apply;
- files included or omitted;
- incomplete snapshot, collision, or validation concerns; and
- the next disposition or write action when needed.
