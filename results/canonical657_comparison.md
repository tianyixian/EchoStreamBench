# canonical657 comparison notes

Updated: 2026-11-25.

The homepage reports all 17 configurations in the verified aggregate inventory: five Qwen3.5-9B reservoir settings, four OneStreamer configurations, seven historical native systems, and MOSS-VL. There are 11 method families. Each row covers 657 canonical items; ranks are computed from recorded correct counts, in descending order.

## Interpretation and result status

- **Reference protocol:** the four original OneStreamer-4B PHCM/RHM-X rows; their published counts and paired comparison are retained.
- **Historical, provisional:** the verified source inventory retains scientific_acceptance=false for Qwen and the historical native systems. Complete recorded results are available, but their original scientific and input-validation qualifications remain in force, including the historical native systems' D/layer and causal limitations. Publication in this overview does not change that status.
- **Provisional; 1 repaired item:** Flash-VStream combines 656 original-condition outputs and one isolated empty-cluster repair; equivalence to the original implementation is not claimed.
- **34 disclosed repairs:** MOSS-VL has a completed integrity review under disclosed repaired conditions (623 original-condition items plus 34 repairs). The unchanged original condition alone covers 623 items. See [its result report](moss_vl_canonical657.md).

The five Qwen configurations retain 190 failure/replacement records across their combined provenance. Historical native MCQ evaluation uses option logits, whereas MOSS-VL parses generated text. Input frame semantics, backbones, budgets, and backend settings are not identical. StreamForest's source records a case-only model alias and an explicit judge-endpoint override.

Scores are frozen reported outcomes; no scores were recomputed with the newly public OpenQA normalized-exact baseline. OneStreamer and MOSS-VL OpenQA counts use their frozen GLM-5.3 judge outcomes. This overview does not establish equal-condition superiority, statistical significance, contamination resistance, or an architecture-only effect.

## Additional controls

The following two recorded controls are provided separately from the 17 model/configuration ranks:

| Control | Correct / total | Accuracy |
|---|---:|---:|
| Qwen3.5-9B recent16 | 200 / 657 | 30.44% |
| Qwen3.5-9B no_video | 183 / 657 | 27.85% |

StreamTTT appears only in the separate historical 672-cell table: no canonical657 completion source was identified in this inventory. The 672-cell scores are not eligible for the canonical657 ranking.

## Source identity

The released rows were checked against frozen aggregate records. Hashes below identify those records without exposing their internal paths. They are provenance identifiers; the private source files and execution traces are not included here. The public aggregate table is [canonical657_ranking.csv](canonical657_ranking.csv); the original four-column report is [benchmark_report.md](benchmark_report.md).

| Record | Configurations | SHA256 of frozen aggregate record |
|---|---|---|
| S01 | Qwen3.5-9B reservoir 256, Qwen3.5-9B reservoir 128, Qwen3.5-9B reservoir 64, Qwen3.5-9B reservoir 32, Qwen3.5-9B reservoir 16 | 4e80b8fd11131b5a5bb29f16c33cfd9126d411d4772db7fa9e8fce80c78547c5 |
| S02 | OneStreamer-4B V2 + RHM-X, OneStreamer-4B V1 + RHM-X, OneStreamer-4B V1 + PHCM, OneStreamer-4B V2 + PHCM | 73e98817af1ce357b11ee977207d3f46387c645fe87832c3496e8772add5a61a |
| S03 | FluxMem | 5a7961ab06620975f6775025a8382fdd6d58f48a590e90b3816401f18abbfd7a |
| S04 | MOSS-VL | 165d251b9ba35b1c9b67b21193fe93fa9d26e26b4a94a606afc3507da7d2699f |
| S05 | StreamForest | b7e34be8b83f904bb26b1d7c0734280adff5dd58acc2cf55f0d38dc4a534c30c |
| S06 | Flash-VStream | 75de14312492d6bd52675c28327ae566929f772f5f665c741d53a2d303d3ee10 |
| S07 | StreamKV medium | 8782eed38c8171c5b74bf66ebd32aaaf32e1eb8a95b8fd949dec33763acfc831 |
| S08 | StreamingVLM | 9f2469a895134109fd8109181527e4465b5f7e575654c12bc2d2978ad8366227 |
| S09 | ReKV medium, HERMES medium | 020b3d48065a620a704dcd2d25c2561bdb44eb112c4f13d0a6e54dc6d946cb47 |
