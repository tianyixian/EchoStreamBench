# EchoStreamBench

**A benchmark for studying memory in streaming video understanding.**

[![Dataset](https://img.shields.io/badge/Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/tianyixian/echostreambench-canonical657)
[![Release](https://img.shields.io/github/v/release/tianyixian/EchoStreamBench)](https://github.com/tianyixian/EchoStreamBench/releases/latest)
[![Validation](https://github.com/tianyixian/EchoStreamBench/actions/workflows/validate.yml/badge.svg)](https://github.com/tianyixian/EchoStreamBench/actions/workflows/validate.yml)

[中文说明](README.zh-CN.md) · [Dataset Viewer](https://huggingface.co/datasets/tianyixian/echostreambench-canonical657/viewer/default/train) · [Quickstart](#quickstart) · [Full leaderboard](#complete-canonical657-ranking) · [Download ZIP](https://github.com/tianyixian/EchoStreamBench/releases/latest) · [Submit a result](SUBMIT.md) · [Sharing images & post](docs/share/README.md)

EchoStreamBench studies how video-language models and memory architectures retain and use earlier visual information as a video unfolds. The motivating question is whether a correct answer relies on older evidence or can be recovered from recent frames alone.

EchoStreamBench canonical657 contains **657 questions, 591 source videos, and 8 source benchmarks**, with public reference answers and a local scorer. The suite has 647 multiple-choice questions and 10 open-ended questions. It covers LongVideoBench, LVBench, MLVU, OVO-Bench backward, RTV-Bench, StreamingBench, SVBench, and Video-MME.

This repository provides the question manifest, answer key, evaluation protocol, scoring code, and aggregate results for **17 configurations across 11 methods**. The same data is available on [Hugging Face](https://huggingface.co/datasets/tianyixian/echostreambench-canonical657), including a Dataset Viewer. Source videos are obtained separately from their original releases; see the [media access guide](MEDIA_ACCESS_GUIDE.md).

## Complete canonical657 ranking

Updated: 2026-11-25 · **17 evaluated configurations across 11 methods** · 657 questions per row.

This table orders reported accuracy on the same canonical657 question set. Systems use different backbones, memory budgets, sampling pipelines, and MCQ readout methods; the ranks describe these evaluated configurations and do not isolate architecture effects.

| Rank | System / configuration | Correct / total | Accuracy | Result notes |
|---:|---|---:|---:|---|
| 1 | Qwen3.5-9B reservoir 256 | 413 / 657 | 62.86% | Historical, provisional |
| 2 | **OneStreamer-4B V2 + RHM-X** | 411 / 657 | 62.56% | Reference protocol |
| 3 | Qwen3.5-9B reservoir 128 | 395 / 657 | 60.12% | Historical, provisional |
| 4 | Qwen3.5-9B reservoir 64 | 392 / 657 | 59.67% | Historical, provisional |
| 5 | Qwen3.5-9B reservoir 32 | 385 / 657 | 58.60% | Historical, provisional |
| 6 | FluxMem | 377 / 657 | 57.38% | Historical, provisional |
| 7 | **OneStreamer-4B V1 + RHM-X** | 370 / 657 | 56.32% | Reference protocol |
| 8 | MOSS-VL | 347 / 657 | 52.82% | 34 disclosed repairs |
| 9 | Qwen3.5-9B reservoir 16 | 346 / 657 | 52.66% | Historical, provisional |
| 10 | StreamForest | 335 / 657 | 50.99% | Historical, provisional |
| 11 | Flash-VStream | 324 / 657 | 49.32% | Provisional; 1 repaired item |
| 12 | OneStreamer-4B V1 + PHCM | 291 / 657 | 44.29% | Reference protocol |
| 13 | OneStreamer-4B V2 + PHCM | 290 / 657 | 44.14% | Reference protocol |
| 14 | StreamKV medium | 273 / 657 | 41.55% | Historical, provisional |
| 15 | StreamingVLM | 260 / 657 | 39.57% | Historical, provisional |
| 16 | ReKV medium | 252 / 657 | 38.36% | Historical, provisional |
| 17 | HERMES medium | 240 / 657 | 36.53% | Historical, provisional |

MOSS-VL ranks 8th of the 17 configurations. Its 347/657 includes 344/647 MCQ and 3/10 OpenQA. The result combines 623 original-condition items and 34 items completed with disclosed repairs.

Rows marked provisional retain their source records' scientific-acceptance limitations. Qwen's five configurations retain 190 failure/replacement records in their combined provenance; Flash-VStream combines 656 original runs with one repaired run. See the [comparison notes](results/canonical657_comparison.md) for details and the [MOSS-VL report](results/moss_vl_canonical657.md) for its protocol.

[Download all 17 rows (CSV)](results/canonical657_ranking.csv) · [All result tables (JSON)](leaderboard.json) · [Reference and historical tables](LEADERBOARD.md)

## Quickstart

Python 3.10+ is sufficient for reading JSON and scoring predictions; these steps use only the standard library.

```bash
git clone https://github.com/tianyixian/EchoStreamBench.git
cd EchoStreamBench
python scripts/validate_public_release.py
python scripts/verify_checksums.py
```

Alternatively, download and extract the [release ZIP](https://github.com/tianyixian/EchoStreamBench/releases/latest), then open a terminal in the extracted folder.

Read the questions:

```python
import json
from pathlib import Path

items = json.loads(Path("manifest.json").read_text(encoding="utf-8"))["items"]
print(len(items))                  # 657
print(items[0]["public_id"])        # ESB-0001
print(items[0]["question"])
```

1. Obtain the source videos following [MEDIA_ACCESS_GUIDE.md](MEDIA_ACCESS_GUIDE.md). Match `source_benchmark`, `video_id`, and `media_locator` to each record.
2. Run your model on each question using the recorded `query_cutoff_seconds`. Model loading, video decoding, and inference are supplied by your model's own implementation.
3. Save one JSON object for each of the 657 items to `predictions.jsonl`. Return an option letter for MCQ, or answer text for OpenQA:

```json
{"public_id":"ESB-0001","prediction":"E"}
```

4. Score the complete file:

```bash
python answers/score.py --pred predictions.jsonl --output scores.json
```

The scorer reports MCQ exact match and **normalized exact match for OpenQA**. Historical OpenQA leaderboard scores used a frozen GLM-5.3 judge, so a local exact-match score is not interchangeable with those reported scores. See [the evaluation protocol](evaluation_protocol.md) and [answer-release notes](ANSWERS_RELEASE.md).

## Files and reproducibility

| File | Purpose |
|---|---|
| [manifest.json](manifest.json) | All 657 questions, options, source identifiers, cutoffs, and hashes |
| [answers/answers.jsonl](answers/answers.jsonl) | Public reference answers, keyed by `public_id` |
| [answers/score.py](answers/score.py) | Local scorer with no third-party dependencies |
| [data/](data/) | JSONL and Parquet copies of the public question records |
| [LEADERBOARD.md](LEADERBOARD.md) | Full ranking, OneStreamer reference comparison, and separate historical 672-cell results |
| [leaderboard.json](leaderboard.json) | Machine-readable result tables |
| [MEDIA_ACCESS_GUIDE.md](MEDIA_ACCESS_GUIDE.md) | Official upstream media download locations |
| [UPSTREAM_SNAPSHOT.json](UPSTREAM_SNAPSHOT.json) | Hugging Face source revision and hashes of the shared data |
| [checksums/SHA256SUMS.txt](checksums/SHA256SUMS.txt) | Integrity hashes for this GitHub release |

The published answers make this a reproducibility release, rather than a hidden test set. Source videos, model weights, and per-model inference runtimes are not bundled. The historical 672-cell panel uses a different item set and remains separate from canonical657.

## Share results and report issues

Use the [result submission guide](SUBMIT.md) to share a complete evaluation. [Open an issue](https://github.com/tianyixian/EchoStreamBench/issues/new/choose) for questions, reproducibility problems, or source-data corrections. Include the dataset version and model settings so that others can reproduce your result.

## Citation

For this public dataset release, cite the repository and the source benchmarks you use:

```bibtex
@misc{echostreambench2026,
  author = {{EchoStreamBench contributors}},
  title = {EchoStreamBench canonical657: Public Reproducibility Release},
  year = {2026},
  howpublished = {\url{https://github.com/tianyixian/EchoStreamBench}},
  note = {Version 1.1.0; 657 questions with public reference answers}
}
```

See [CITATION.cff](CITATION.cff) for machine-readable citation metadata and [DATASET_CITATIONS.md](DATASET_CITATIONS.md) for upstream sources. This citation identifies the dataset release.

## License

Original Python utilities in `answers/` and `scripts/` are released under the [MIT License](LICENSE). Third-party question text, options, answers, and media references remain subject to their upstream licenses and terms; the code license does not relicense them. See [NOTICE.md](NOTICE.md), [TERMS_OF_USE.md](TERMS_OF_USE.md), and the [media license audit](MEDIA_LICENSE_AUDIT_20261121.md).
