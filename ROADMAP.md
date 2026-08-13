# Roadmap

> **Document role:** Delivery sequence for the baselines in [`BRD.md`](BRD.md), [`PRD.md`](PRD.md), and [`FSD.md`](FSD.md). Checked items indicate implemented documentation or controls, not empirical validation unless stated.

## v0.1 — Foundation

**Goal:** Turn the project vision into a coherent method and usable core skill.

- [x] Define Unsloop, Review, Write, and Audit
- [x] Separate integrity and human-voice lenses
- [x] Define source-dependence scoring
- [x] Define directional voice-profile scores
- [x] Define consent-aware voice sampling and evidence hierarchy
- [x] Define optional voice-fidelity scoring and confidence labels
- [x] Define the progressive writing brief and proportional intake rules
- [x] Add existing-topic, topic-refinement, and topic-brainstorming entry paths
- [x] Add capability-aware structured questions with a conversational fallback
- [x] Add governing-direction hierarchy and explicit content roles
- [x] Add hard-constraint, allocation, and safety-buffer handling
- [x] Add requirement-coverage and readiness contracts
- [x] Add functional-example and emotional-integrity review
- [x] Establish output, evidence, and ethics contracts
- [x] Create and validate the repo-local core skill under `.agents/skills`
- [x] Add dependency-free project-local validation
- [x] Initialize portable Git metadata and line-ending rules
- [x] Add optional global discovery through a link to the authoritative project skill
- [x] Establish BRD, PRD, and FSD baselines with requirement traceability
- [x] Align all project and operational Markdown with the specification hierarchy
- [x] Define a model- and harness-agnostic Agent Skills core
- [x] Preserve Codex support while documenting Claude, Pi, and generic harness adapters
- [x] Add capability negotiation and fallbacks for harness and model differences
- [x] Add a topic-neutral fiction workflow within Unsloop Write for scenes through series
- [x] Add Guided, Adaptive, and Autonomous fiction collaboration cadences
- [x] Add author-approved portable fiction state with resumable status and classified canon
- [x] Separate author, narrative, viewpoint, and dialogue voice targets
- [x] Add manuscript-scale context, continuity, research, retcon, and handoff controls

## v0.2 — Examples and calibration

**Goal:** Test whether different reviewers apply the method consistently.

- [ ] Build anonymized fixtures for quotation, paraphrase, patchwriting, structural dependence, and secondary-source problems
- [ ] Build voice fixtures covering multiple genres and levels of formality
- [ ] Test sparse, conflicting, cross-genre, and multilingual voice samples
- [ ] Test sparse, conflicting, over-specified, and high-stakes writing briefs
- [ ] Test topic discovery with no seed, a rough direction, and an already explicit topic
- [ ] Test equivalent decisions through structured and plain-text question interfaces
- [ ] Test conflicting governing directions and hard-versus-working constraints
- [ ] Test requirement coverage independently from factual support
- [ ] Test readiness labels against unresolved choices, evidence, and authorization
- [ ] Test emotional-integrity findings across persuasive, pastoral, commercial, and personal genres
- [ ] Add expected evidence notes without prescribing a single perfect rewrite
- [ ] Forward-test brief, standard, and deep reviews in clean contexts
- [ ] Revise ambiguous scale anchors
- [ ] Record common false positives, especially for second-language and highly conventional writing
- [ ] Convert the FSD verification matrix into reusable fixtures with expected boundaries and outputs
- [ ] Trace fixture results back to `PR-*`, `NFR-*`, and `FS-*` requirements
- [ ] Forward-test the same Review, Write, and Audit fixtures in Codex, Claude, Pi, and at least one manual Agent Skills adapter
- [ ] Compare model families and context sizes without treating one model's output as the reference truth
- [ ] Test missing-tool fallbacks for structured input, browsing, file editing, memory, and length measurement
- [ ] Test minimal scene, short-story, novel, serial, and series workflow scaling
- [ ] Test Guided, Adaptive, and Autonomous checkpoint behavior with consequential deviations
- [ ] Test Proposed-to-Confirmed canon promotion, explicit retcons, and manuscript-ledger conflicts
- [ ] Test cross-session fiction resumption from `story/STATUS.md` with partial manuscript context
- [ ] Test author, narrative, viewpoint, and dialogue voice separation across fiction genres
- [ ] Test historical fiction, named-author adaptation, real-person depiction, and incomplete research boundaries

## v0.3 — Assisted audit tooling

**Goal:** Reduce mechanical comparison work while keeping findings inspectable.

- [ ] Prototype passage alignment across draft and supplied sources
- [ ] Surface shared wording, syntax, idea order, and detail selection separately
- [ ] Export a source map without assigning misconduct
- [ ] Add citation and locator verification hooks
- [ ] Define privacy expectations for local and external processing
- [ ] Add adapter fixtures that verify identical evidence and ethics boundaries across harnesses

## v0.4 — Mode specialization

**Goal:** Decide whether observed use justifies separate skills.

- [ ] Evaluate trigger precision for Review, Write, and Audit
- [ ] Split only the modes that meet the criteria in `docs/NAMING.md`
- [ ] Add user-approved persistent personal-voice and publication-style profiles
- [ ] Support Markdown and machine-readable review reports

## v1.0 — Validated release

**Goal:** Publish a stable, documented method with known limits.

- [ ] Demonstrate acceptable inter-reviewer agreement on the core classifications
- [ ] Publish benchmark design and limitations
- [ ] Stabilize score anchors and output contracts
- [ ] Complete privacy, accessibility, and bias review
- [ ] Document installation and release packaging outside the skill bundle
- [ ] Publish a cross-harness compatibility matrix with tested versions and known limitations

## Open questions

- Should source dependence be reported per passage, per source, or both?
- Which genres need their own voice expectations?
- What minimum sample diversity supports High voice-fidelity confidence across genres?
- What minimum evidence should be required before assigning High or Critical severity?
- When does a separate mode skill improve reliability enough to justify maintenance cost?
- What evidence threshold should move the BRD/PRD/FSD baseline from documented to empirically validated?
