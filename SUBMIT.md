# Submit a result to EchoStreamBench

The 2026-11-24 reproducibility snapshot includes the public answer key, so every researcher can score a complete prediction file locally before sharing results.

## Required evaluation contract

Use all 657 public items, the frozen query cutoffs, and the scoring rules in [`evaluation_protocol.md`](evaluation_protocol.md). Do not mix canonical657 results with the historical 672-cell controlled architecture panel.

## Prediction file

Submit one JSON object per item in JSONL format:

```json
{"public_id":"ESB-0001","prediction":"E"}
```

For multiple-choice items, `prediction` is the selected option letter (the bundled scorer accepts a model response containing a standalone letter). For OpenQA items, `prediction` is the final text answer. Run `python answers/score.py --pred predictions.jsonl` and include the resulting report.

## Leaderboard submissions

Open a [GitHub result submission issue](https://github.com/tianyixian/EchoStreamBench/issues/new?template=result.yml), or a discussion in the [Hugging Face dataset repository](https://huggingface.co/datasets/tianyixian/echostreambench-canonical657/discussions) with the title `Leaderboard submission: <model>`. Include the prediction file or a public link, the local score report, model and revision, memory or streaming architecture, inference backend, decoding settings, source-media version, completed item count, evaluation date, and compute environment. State clearly whether OpenQA uses the bundled normalized exact-match baseline or another judge.

Do not upload unlicensed source videos, credentials, or internal filesystem paths. The answer key is already part of this reproducibility snapshot; future hidden-test submissions, if any, must use a separately announced version.
