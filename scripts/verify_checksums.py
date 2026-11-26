#!/usr/bin/env python3
"""Verify the release files listed in checksums/SHA256SUMS.txt."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
count = 0
for line in (ROOT / "checksums/SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, name = line.split("  ", 1)
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise SystemExit(f"Missing or invalid release path: {name}")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f"Checksum mismatch: {name}")
    count += 1
print(f"CHECKSUM_VERIFICATION_PASS {count} files")
