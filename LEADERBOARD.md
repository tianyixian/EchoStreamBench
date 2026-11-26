# EchoStreamBench leaderboards

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

## Reference comparison: OneStreamer-4B on canonical657

This is the public EchoStreamBench benchmark: 657 frozen items, consisting of 647 multiple-choice questions and 10 open-ended questions. All four rows use the same canonical657 item set and scoring contract.

| Rank | Configuration | Correct / total | Overall accuracy | MCQ | OpenQA | Evaluation date |
|---:|---|---:|---:|---:|---:|---|
| 1 | **OneStreamer-4B V2 + RHM-X** | 411 / 657 | 62.56% | 406/647 (62.75%) | 5/10 (50.00%) | 2026-11-17 |
| 2 | **OneStreamer-4B V1 + RHM-X** | 370 / 657 | 56.32% | 365/647 (56.41%) | 5/10 (50.00%) | 2026-11-17 |
| 3 | OneStreamer-4B V1 + PHCM | 291 / 657 | 44.29% | 286/647 (44.20%) | 5/10 (50.00%) | 2026-11-17 |
| 4 | OneStreamer-4B V2 + PHCM | 290 / 657 | 44.14% | 286/647 (44.20%) | 4/10 (40.00%) | 2026-11-17 |

These are single evaluation snapshots. The benchmark is now answer-released for reproducibility and remains media-free; see [`evaluation_protocol.md`](evaluation_protocol.md) and [`MEDIA_ACCESS_GUIDE.md`](MEDIA_ACCESS_GUIDE.md).

## Supplementary full-set result: MOSS-VL

MOSS-VL reports 347/657 (52.82%), with 344/647 MCQ (53.17%) and 3/10 OpenQA (30.00%). The 657-item result combines 623 original-condition items and 34 items run with explicitly disclosed repairs. It is included in the complete configuration ranking above with its conditions disclosed. The four-row OneStreamer reference comparison is retained separately. Full details are in [`results/moss_vl_canonical657.md`](results/moss_vl_canonical657.md).

## Controlled architecture comparison: historical 672-cell panel

This table reports the earlier controlled architecture experiment. Every system used the same frozen panel of 56 questions from 32 videos, evaluated at four evidence placements and three native settings (`56 x 4 x 3 = 672` cells per system). It is a shared-panel native-system comparison, not an equal-backbone or equal-resource leaderboard: systems retain different backbones and native resource units. It is therefore reported separately from canonical657.

| Rank | System | Native control | Backbone | Correct / 672 | Overall accuracy | Long-delay accuracy (D >= 120 s) |
|---:|---|---|---|---:|---:|---:|
| 1 | **RHM-X** | Evidence readout q=6/12/24 | OneStreamer-4B | 442/672 | 65.77% | 69/96 (71.88%) |
| 2 | FluxMem | Short/mid residence | Qwen2.5-VL-7B Instruct | 404/672 | 60.12% | 56/96 (58.33%) |
| 3 | StreamForest | Long-term quota | StreamForest Qwen2-7B | 403/672 | 59.97% | 61/96 (63.54%) |
| 4 | Flash-VStream | Temporal/spatial capacity | Flash-VStream Qwen-7B | 395/672 | 58.78% | 62/96 (64.58%) |
| 5 | StreamingVLM | Window length | StreamingVLM | 377/672 | 56.10% | 45/96 (46.88%) |
| 6 | StreamKV | Retention fraction | LLaVA-OV Qwen2-0.5B | 302/672 | 44.94% | 53/96 (55.21%) |
| 7 | ReKV | Retrieval top-k | LLaVA-OV Qwen2-0.5B | 279/672 | 41.52% | 51/96 (53.13%) |
| 8 | StreamTTT | Recent KV | StreamTTT-4B | 262/672 | 38.99% | 35/96 (36.46%) |
| 9 | HERMES | KV capacity | LLaVA-OV Qwen2-0.5B | 202/672 | 30.06% | 31/96 (32.29%) |

The 672-cell panel is not the canonical657 benchmark: its question pool, interventions, and evaluation contract are different. The 65.77% RHM-X result and the 62.56% canonical657 result are not contradictory; they answer different evaluation questions.

## Supplementary and archived results

Earlier OVO-Bench Backward and StreamArena-HR results use additional protocols, partial valid denominators, or proxy judging. They are retained in the research record but are not included in the canonical657 ranking or historical 672-cell panel.

## Provenance

- Canonical657 source: [`results/benchmark_report.md`](results/benchmark_report.md).
- Controlled-panel source: the verified historical 672-cell architecture table dated 2026-10-13; this public table reproduces its reported aggregate values and protocol boundary.
- The released answer key is provided separately under `answers/`; this file does not include per-item predictions, raw traces, or third-party videos.
