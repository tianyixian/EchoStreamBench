# EchoStreamBench canonical657 evaluation protocol

## Item set

The fixed item set contains 657 items: 647 multiple-choice items and 10 open-ended items. `public_id` is the stable identifier. The public reference answers are distributed in [`answers/answers.jsonl`](answers/answers.jsonl), with a release hash in [`answers/answers_manifest.json`](answers/answers_manifest.json).

## Media

Media files are not mirrored here. Obtain each source video from the official source benchmark under its license, then use `source_benchmark`, `video_id`, `media_locator`, and `query_cutoff_seconds` in `manifest.json`.

## Multiple choice

A model should output an option label. The bundled scorer extracts the first standalone A--E option label and compares it exactly with the released answer. The option order is the order in the manifest.

## Open-ended questions

The 10 open-ended items use free-text answers. The bundled scorer reports normalized exact match as a transparent local baseline. The historical leaderboard used a frozen GLM-5.3 judge; local exact match is not a replacement for that historical judging contract. Researchers may implement and report their own semantic judge, but should state it explicitly.

## Reporting

Report overall accuracy, MCQ accuracy, OpenQA scoring rule, model revision, media version, and evaluation date. Do not combine canonical657 with the historical 672-cell controlled architecture panel.

## Release boundary

This is a reproducibility snapshot with public answers. It is suitable for downloading, running a model, and checking results locally. It is not a hidden or contamination-resistant test set after this release.
