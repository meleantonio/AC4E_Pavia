#!/usr/bin/env python3
"""Run Card-Krueger verification when the DiD analysis script is edited (Codex PostToolUse hook)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

TARGET = "examples/card-krueger-toy/src/did_analysis.py"
REPO_ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool_input = payload.get("tool_input") or {}
    edited_path = str(tool_input.get("path") or tool_input.get("file_path") or "")
    if TARGET not in edited_path:
        return 0

    print(f"[Hook] {TARGET} edited — running verification suite.", file=sys.stderr)
    result = subprocess.run(
        ["python3", "-m", "pytest", "examples/card-krueger-toy/tests", "-q"],
        cwd=REPO_ROOT,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
