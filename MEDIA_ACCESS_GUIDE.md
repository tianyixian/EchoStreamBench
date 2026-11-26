# EchoStreamBench media access guide

EchoStreamBench publishes the frozen question manifest and stable source identifiers. It does not mirror third-party video files. To run a local evaluation, use the official source release named by `source_benchmark` and match its `video_id` or `media_locator` in `manifest.json`.

| Source benchmark | Official access point | What users should do | Redistribution status |
|---|---|---|---|
| LongVideoBench | [HF dataset card](https://huggingface.co/datasets/longvideobench/LongVideoBench) | Use the web-video links and follow the gated card terms. | The benchmark does not own the linked videos; do not mirror them. |
| LVBench | [GitHub README](https://github.com/zai-org/LVBench), [HF dataset](https://huggingface.co/datasets/THUDM/LVBench) | Obtain `video_info.meta.jsonl` and use the official download script/YouTube IDs. | Academic research only; raw-video copyright is not owned by the benchmark. |
| MLVU | [HF dataset](https://huggingface.co/datasets/MLVU/MVLU), [test release](https://huggingface.co/datasets/MLVU/MLVU_Test), [GitHub README](https://github.com/JUNJIE99/MLVU) | Request/access the source release and follow its gated terms. | Research access only; original video owners retain rights. |
| Video-MME | [Official GitHub dataset section](https://github.com/BradyFU/Video-MME#-dataset) | Follow the official academic-use download instructions. | Distribution, publication, copying, and dissemination require prior approval. |
| OVO-Bench | [Official GitHub README](https://github.com/JoeLeelyf/OVO-Bench#license), [HF dataset](https://huggingface.co/datasets/JoeLeelyf/OVO-Bench) | Obtain the source/chunk archives from the official release and follow both OVO and source-dataset terms. | No single OVO license clears the mixed-source raw videos. |
| RTV-Bench | [Official GitHub repository](https://github.com/LJungang/RTV-Bench), [HF dataset](https://huggingface.co/datasets/RTVBench/RTV-Bench) | Obtain the official dataset and inspect its current terms before use. | Raw-video redistribution authorization is not stated. |
| StreamingBench | [Official GitHub repository](https://github.com/THUNLP-MT/StreamingBench), [HF dataset](https://huggingface.co/datasets/mjuicem/StreamingBench) | Retrieve the dataset from the official release; users may need to obtain raw videos independently. | The MIT code license does not grant raw-video redistribution. |
| SVBench | [Official GitHub README](https://github.com/sotayang/SVBench), [HF dataset](https://huggingface.co/datasets/yzy666/SVBench) | Follow the source-specific download instructions for YT-Temporal-1B, YouCook2, MovieChat, Panda-70M, Ego4D, and ActivityNet. | Research use only; comply with every original source license. |

## Reproducible lookup

1. Select a row in `manifest.json`.
2. Read `source_benchmark`, `video_id`, `media_locator`, and `query_cutoff_seconds`.
3. Download or request the corresponding media from the official source above under its current terms.
4. Keep the downloaded media local and use the recorded cutoff; this repository does not grant permission to re-upload it.

The full evidence and decision for each source are in [`MEDIA_LICENSE_AUDIT_20261121.md`](MEDIA_LICENSE_AUDIT_20261121.md).
