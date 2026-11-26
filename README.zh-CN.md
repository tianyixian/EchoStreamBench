# EchoStreamBench 中文说明

**面向长视频问答、可在本地复现的评测题集。**

[English](README.md) · [Hugging Face 数据集](https://huggingface.co/datasets/tianyixian/echostreambench-canonical657) · [在线浏览题目](https://huggingface.co/datasets/tianyixian/echostreambench-canonical657/viewer/default/train) · [完整排名](#canonical657-完整排名) · [下载 ZIP](https://github.com/tianyixian/EchoStreamBench/releases/latest) · [提交结果](SUBMIT.md)

EchoStreamBench canonical657 包含 **657 道题、591 个源视频、8 个来源 benchmark**：647 道选择题和 10 道开放问答。来源为 LongVideoBench、LVBench、MLVU、OVO-Bench backward、RTV-Bench、StreamingBench、SVBench 和 Video-MME。

本仓库提供题目、公开答案、评测协议、本地评分代码，以及 **11 种方法、17 个配置**的汇总结果。Hugging Face 提供同一批数据和 Dataset Viewer；原视频需按[媒体获取指南](MEDIA_ACCESS_GUIDE.md)从上游取得。

## canonical657 完整排名

更新：2026-11-25 · **11种方法、17个已评测配置** · 每行均为657题。

下表按同一 canonical657 题集上的已记录准确率排序。各系统的骨干、内存预算、采样和选择题读出方式不同，因此这是配置成绩总览，名次不直接代表架构本身的优劣。

| 排名 | 系统 / 配置 | 正确数 / 总数 | 准确率 | 结果说明 |
|---:|---|---:|---:|---|
| 1 | Qwen3.5-9B reservoir 256 | 413 / 657 | 62.86% | 历史结果，暂定 |
| 2 | **OneStreamer-4B V2 + RHM-X** | 411 / 657 | 62.56% | 原四列协议 |
| 3 | Qwen3.5-9B reservoir 128 | 395 / 657 | 60.12% | 历史结果，暂定 |
| 4 | Qwen3.5-9B reservoir 64 | 392 / 657 | 59.67% | 历史结果，暂定 |
| 5 | Qwen3.5-9B reservoir 32 | 385 / 657 | 58.60% | 历史结果，暂定 |
| 6 | FluxMem | 377 / 657 | 57.38% | 历史结果，暂定 |
| 7 | **OneStreamer-4B V1 + RHM-X** | 370 / 657 | 56.32% | 原四列协议 |
| 8 | MOSS-VL | 347 / 657 | 52.82% | 34题披露修复 |
| 9 | Qwen3.5-9B reservoir 16 | 346 / 657 | 52.66% | 历史结果，暂定 |
| 10 | StreamForest | 335 / 657 | 50.99% | 历史结果，暂定 |
| 11 | Flash-VStream | 324 / 657 | 49.32% | 暂定；1题修复 |
| 12 | OneStreamer-4B V1 + PHCM | 291 / 657 | 44.29% | 原四列协议 |
| 13 | OneStreamer-4B V2 + PHCM | 290 / 657 | 44.14% | 原四列协议 |
| 14 | StreamKV medium | 273 / 657 | 41.55% | 历史结果，暂定 |
| 15 | StreamingVLM | 260 / 657 | 39.57% | 历史结果，暂定 |
| 16 | ReKV medium | 252 / 657 | 38.36% | 历史结果，暂定 |
| 17 | HERMES medium | 240 / 657 | 36.53% | 历史结果，暂定 |

MOSS-VL 在17个配置中排第8。 总分347/657，其中选择题344/647、OpenQA 3/10；623题使用原条件，34题使用已披露的修复条件。

标为“暂定”的历史结果保留原记录的科学验收限制。Qwen五个配置的来源合计保留190条失败/替换记录；Flash-VStream为656条原运行加1条修复运行。详见[比较说明](results/canonical657_comparison.md)和[MOSS-VL报告](results/moss_vl_canonical657.md)。

[下载17行完整CSV](results/canonical657_ranking.csv) · [全部结果JSON](leaderboard.json) · [原四列与历史表](LEADERBOARD.md)

## 快速开始

读取 JSON 和评分只需要 Python 3.10+ 标准库，无需安装第三方依赖。

```bash
git clone https://github.com/tianyixian/EchoStreamBench.git
cd EchoStreamBench
python scripts/validate_public_release.py
python scripts/verify_checksums.py
```

也可以下载并解压 [Release ZIP](https://github.com/tianyixian/EchoStreamBench/releases/latest)，在解压后的目录打开终端。

读取全部题目：

```python
import json
from pathlib import Path

items = json.loads(Path("manifest.json").read_text(encoding="utf-8"))["items"]
print(len(items))                  # 657
print(items[0]["public_id"])        # ESB-0001
print(items[0]["question"])
```

1. 按 [MEDIA_ACCESS_GUIDE.md](MEDIA_ACCESS_GUIDE.md) 从原数据集获取视频，通过 `source_benchmark`、`video_id` 和 `media_locator` 对齐题目。
2. 用自己的模型实现运行推理，遵守每题 `query_cutoff_seconds`。模型加载、视频解码和推理需要使用对应模型的代码。
3. 为全部 657 题保存 `predictions.jsonl`，每行包含 `public_id` 和 `prediction`；选择题填选项字母，开放题填答案文本：

```json
{"public_id":"ESB-0001","prediction":"E"}
```

4. 运行评分：

```bash
python answers/score.py --pred predictions.jsonl --output scores.json
```

评分器对选择题做精确匹配，对 OpenQA 做**规范化文本精确匹配**。历史榜单的开放题使用冻结的 GLM-5.3 judge，两种评分方式不能当成同一分数。详见[评测协议](evaluation_protocol.md)和[答案公开说明](ANSWERS_RELEASE.md)。

## 仓库内容

| 文件 | 用途 |
|---|---|
| [manifest.json](manifest.json) | 657 题题干、选项、来源、截止点和哈希 |
| [answers/answers.jsonl](answers/answers.jsonl) | 以 `public_id` 对齐的公开参考答案 |
| [answers/score.py](answers/score.py) | 无第三方依赖的本地评分器 |
| [data/](data/) | 同一题集的 JSONL 和 Parquet 文件 |
| [LEADERBOARD.md](LEADERBOARD.md) | 完整排名、OneStreamer 参考表及单列的历史 672-cell 结果 |
| [leaderboard.json](leaderboard.json) | 机器可读结果 |
| [UPSTREAM_SNAPSHOT.json](UPSTREAM_SNAPSHOT.json) | 对应 HF 版本及共享数据哈希 |
| [checksums/SHA256SUMS.txt](checksums/SHA256SUMS.txt) | 当前 GitHub 发布包的完整性校验 |

公开答案使该版本适合复现，不再适合作为隐藏测试集。仓库不包含原视频、模型权重或各模型推理运行环境；历史 672-cell 使用不同题集，与 canonical657 分开阅读。

## 结果提交与反馈

欢迎按[提交说明](SUBMIT.md)分享评测结果，或通过 [GitHub Issues](https://github.com/tianyixian/EchoStreamBench/issues/new/choose)报告问题和数据勘误。请注明数据版本、模型与推理设置、媒体版本和 OpenQA 评分规则。

## 引用与许可

本数据发布包的 BibTeX 在[英文首页](README.md#citation)，机器可读引用见 [CITATION.cff](CITATION.cff)。使用时也请引用对应[源 benchmark](DATASET_CITATIONS.md)。

`answers/` 和 `scripts/` 中的原创 Python 工具采用 [MIT 许可证](LICENSE)。第三方题干、选项、答案和媒体引用仍遵循原来源许可，MIT 代码许可不覆盖这些内容。见 [NOTICE.md](NOTICE.md)、[使用条款](TERMS_OF_USE.md)和[媒体许可核查](MEDIA_LICENSE_AUDIT_20261121.md)。
