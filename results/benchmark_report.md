# OneStreamer-4B canonical657 benchmark results

Evaluation snapshot: 2026-11-17. All four columns completed 657/657 items; each column contains 647 MCQ items and 10 open-ended items.

| Metric | V1 PHCM | V1 RHM-X | V2 PHCM | V2 RHM-X |
|---|---:|---:|---:|---:|
| Overall correct / total (accuracy) | 291/657 (44.29%) | 370/657 (56.32%) | 290/657 (44.14%) | 411/657 (62.56%) |
| MCQ correct / total (accuracy) | 286/647 (44.20%) | 365/647 (56.41%) | 286/647 (44.20%) | 406/647 (62.75%) |
| Open-ended correct / total (accuracy) | 5/10 (50.00%) | 5/10 (50.00%) | 4/10 (40.00%) | 5/10 (50.00%) |
| Retained historical results | 602 | 310 | 606 | 329 |
| New exact-frame results | 55 | 347 | 51 | 328 |

The final 2,628 cells consist of 1,847 retained historical results and 781 new exact-frame results. The two provenance classes remain separate in the internal audit ledger.

## Per-source benchmark results

| Benchmark | Items | V1 PHCM | V1 RHM-X | V2 PHCM | V2 RHM-X |
|---|---:|---:|---:|---:|---:|
| longvideobench | 172 | 93/172 (54.07%) | 100/172 (58.14%) | 93/172 (54.07%) | 113/172 (65.70%) |
| lvbench | 57 | 22/57 (38.60%) | 32/57 (56.14%) | 22/57 (38.60%) | 38/57 (66.67%) |
| mlvu | 204 | 75/204 (36.76%) | 112/204 (54.90%) | 75/204 (36.76%) | 138/204 (67.65%) |
| ovo_backward | 8 | 5/8 (62.50%) | 5/8 (62.50%) | 5/8 (62.50%) | 5/8 (62.50%) |
| rtv_bench | 13 | 8/13 (61.54%) | 8/13 (61.54%) | 8/13 (61.54%) | 9/13 (69.23%) |
| streamingbench | 8 | 7/8 (87.50%) | 7/8 (87.50%) | 7/8 (87.50%) | 7/8 (87.50%) |
| svbench | 10 | 5/10 (50.00%) | 5/10 (50.00%) | 4/10 (40.00%) | 5/10 (50.00%) |
| video_mme | 185 | 76/185 (41.08%) | 101/185 (54.59%) | 76/185 (41.08%) | 96/185 (51.89%) |

This report is an aggregate snapshot of one evaluation pass. It does not claim statistical significance, multi-seed performance, or paper changes.
