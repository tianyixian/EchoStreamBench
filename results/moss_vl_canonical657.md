# MOSS-VL canonical657 result

This supplementary result reports MOSS-VL on all 657 EchoStreamBench canonical items.

| System | Items | Correct | Accuracy |
| --- | ---: | ---: | ---: |
| MOSS-VL | 657 | 347 | 52.82% |

## Score breakdown

| Component | Items | Correct | Accuracy |
| --- | ---: | ---: | ---: |
| Multiple choice | 647 | 344 | 53.17% |
| OpenQA (frozen GLM-5.3 judge) | 10 | 3 | 30.00% |

## By source benchmark

| Source | Items | Correct | Accuracy |
| --- | ---: | ---: | ---: |
| LongVideoBench | 172 | 86 | 50.00% |
| LVBench | 57 | 27 | 47.37% |
| MLVU | 204 | 117 | 57.35% |
| OVO-Bench backward | 8 | 5 | 62.50% |
| RTV-Bench | 13 | 8 | 61.54% |
| StreamingBench | 8 | 5 | 62.50% |
| SVBench | 10 | 3 | 30.00% |
| Video-MME | 185 | 96 | 51.89% |

## Evaluation condition

- Evaluation date: 2026-11-24.
- MOSS-VL-Realtime with HF resize512 input preprocessing, 1 fps sampling, and a 2-second raw window.
- The final 657-item result combines 623 items under the original condition with 34 items run under explicitly disclosed repairs. The repairs include real EOF display-span handling, an official played-at fallback for one item, corrected cutoff/grid handling, and selective no-cuDNN SDPA fallback.
- All 657 items have retained result, process-exit, and strict acceptance evidence. The repaired-condition qualification is complete; the unchanged original condition alone remains 623/657.

## Comparability boundary

This is a descriptive supplementary result and is not merged into the four-row primary canonical657 ranking. The disclosed repairs, selective backend fallback, generated-text MCQ parsing, and MOSS-specific input pipeline mean that this row should not be interpreted as a strictly matched-backbone, matched-backend, or causal architecture comparison. Historical leaderboard rows remain unchanged.

The full private execution ledger, raw media paths, and internal job records are not included in this public card. Researchers can reproduce the public answer scoring using [`answers/score.py`](../answers/score.py) after obtaining source videos under their original licenses.
