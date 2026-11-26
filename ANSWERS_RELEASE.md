# Public answer release

This repository now contains a reproducibility snapshot dated 2026-11-24. It releases 657 reference answers: 647 MCQ letters and 10 OpenQA reference texts. The clean answer file is [`answers/answers.jsonl`](answers/answers.jsonl); it contains only `public_id`, `eval_mode`, `answer`, and `question_sha256`.

The source answer package was audited without exporting private provenance, media paths, judge prompts, job records, or credentials. Mapping preferred the frozen `source_item_id` for 644 entries. The 13 intentionally redacted RTV source IDs were mapped by their unique question hash. The question hash is not globally unique across the full set because some source datasets reuse question templates, so it must not be used as a global item key.

The bundled scorer provides MCQ exact match and normalized exact match for OpenQA. The original four OneStreamer reference results were completed on 2026-11-17, before this answer release, using a frozen GLM-5.3 judge for OpenQA. The published configuration ranking retains frozen reported scores and their disclosed evaluation conditions; these scores should not be interpreted as scores recomputed by the public normalized-exact scorer.

Because answers are public, this version should not be used as a hidden test set or as a contamination-resistant leaderboard. A future hidden evaluation must be versioned and announced separately. Third-party videos remain excluded and must be obtained under their original licenses.
