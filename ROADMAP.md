# Roadmap

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
- [x] Establish output, evidence, and ethics contracts
- [x] Create and validate the repo-local core skill under `.agents/skills`
- [x] Add dependency-free project-local validation
- [x] Initialize portable Git metadata and line-ending rules

## v0.2 — Examples and calibration

**Goal:** Test whether different reviewers apply the method consistently.

- [ ] Build anonymized fixtures for quotation, paraphrase, patchwriting, structural dependence, and secondary-source problems
- [ ] Build voice fixtures covering multiple genres and levels of formality
- [ ] Test sparse, conflicting, cross-genre, and multilingual voice samples
- [ ] Test sparse, conflicting, over-specified, and high-stakes writing briefs
- [ ] Test topic discovery with no seed, a rough direction, and an already explicit topic
- [ ] Test equivalent decisions through structured and plain-text question interfaces
- [ ] Add expected evidence notes without prescribing a single perfect rewrite
- [ ] Forward-test brief, standard, and deep reviews in clean contexts
- [ ] Revise ambiguous scale anchors
- [ ] Record common false positives, especially for second-language and highly conventional writing

## v0.3 — Assisted audit tooling

**Goal:** Reduce mechanical comparison work while keeping findings inspectable.

- [ ] Prototype passage alignment across draft and supplied sources
- [ ] Surface shared wording, syntax, idea order, and detail selection separately
- [ ] Export a source map without assigning misconduct
- [ ] Add citation and locator verification hooks
- [ ] Define privacy expectations for local and external processing

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

## Open questions

- Should source dependence be reported per passage, per source, or both?
- Which genres need their own voice expectations?
- What minimum sample diversity supports High voice-fidelity confidence across genres?
- What minimum evidence should be required before assigning High or Critical severity?
- When does a separate mode skill improve reliability enough to justify maintenance cost?
