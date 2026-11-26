#!/usr/bin/env python3
"""Score local predictions against the public EchoStreamBench answer key.

Usage: python answers/score.py --pred predictions.jsonl
The prediction file must contain one JSON object per item with public_id and
prediction. MCQ is exact match after extracting the first A--Z label. OpenQA
uses normalized exact match as a transparent local baseline; it is not the
historical GLM-5.3 judge used for the released leaderboard.
"""
import argparse
import json
import re
import string
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ANSWERS = Path(__file__).with_name("answers.jsonl")
LABEL_RE = re.compile(r"(?<![A-Za-z])([A-Ea-e])(?![A-Za-z])")


def normalize(text):
    text = unicodedata.normalize("NFKC", str(text)).casefold()
    text = "".join(ch if ch not in string.punctuation else " " for ch in text)
    return " ".join(text.split())


def read_jsonl(path):
    rows = []
    for line_no, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSON at {path}:{line_no}: {exc}")
    return rows


def extract_letter(value):
    match = LABEL_RE.search(str(value))
    return match.group(1).upper() if match else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", required=True, help="JSONL with public_id and prediction")
    parser.add_argument("--answers", default=str(DEFAULT_ANSWERS))
    parser.add_argument("--output", help="Optional JSON report path")
    args = parser.parse_args()

    answer_rows = read_jsonl(args.answers)
    answers = {row["public_id"]: row for row in answer_rows}
    if len(answers) != len(answer_rows):
        raise SystemExit("Answer key contains duplicate public_id values")
    pred_rows = read_jsonl(args.pred)
    predictions = {}
    for row in pred_rows:
        pid = row.get("public_id")
        if not pid or pid in predictions:
            raise SystemExit(f"Missing or duplicate prediction public_id: {pid!r}")
        if pid not in answers:
            raise SystemExit(f"Unknown public_id: {pid}")
        predictions[pid] = row.get("prediction", row.get("answer", ""))
    missing = sorted(set(answers) - set(predictions))
    if missing:
        raise SystemExit(f"Missing predictions: {len(missing)} (first: {missing[:5]})")

    errors = []
    mcq_correct = open_correct = 0
    mcq_total = open_total = 0
    for pid, answer_row in answers.items():
        pred = predictions[pid]
        mode = answer_row["eval_mode"]
        if mode == "mcq_letter":
            mcq_total += 1
            parsed = extract_letter(pred)
            correct = parsed == answer_row["answer"]
        else:
            open_total += 1
            parsed = normalize(pred)
            correct = parsed == normalize(answer_row["answer"])
        if correct:
            if mode == "mcq_letter": mcq_correct += 1
            else: open_correct += 1
        else:
            errors.append({"public_id": pid, "eval_mode": mode, "prediction": str(pred), "parsed": parsed})

    report = {
        "benchmark": "EchoStreamBench canonical657",
        "total": len(answers),
        "correct": mcq_correct + open_correct,
        "accuracy": (mcq_correct + open_correct) / len(answers),
        "mcq": {"correct": mcq_correct, "total": mcq_total, "accuracy": mcq_correct / mcq_total},
        "openqa_normalized_exact": {"correct": open_correct, "total": open_total, "accuracy": open_correct / open_total},
        "errors": errors,
        "note": "OpenQA normalized exact match is a local baseline and is not the frozen GLM-5.3 judge protocol used by the historical leaderboard."
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    print(text, end="")
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
