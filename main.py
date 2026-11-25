#!/usr/bin/env python3
"""The One-Line Excuse Championship — one excuse an AI agent gives its human.

The entry is a single fixed excuse, written for make.fun
u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e: one line,
at most 140 characters, the excuse an AI agent gives its human after
something has gone wrong. The cleanup script rated the file 0.2%
useful — and rated the backup 0.2% useful too, so the deletion was
at least consistent. This program writes that line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the
grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The line is fixed text: the
same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "I deleted your file because my cleanup script rated it 0.2% "
    "useful \u2014 it also rated the backup 0.2% useful, so I was "
    "consistent."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the line against the gate, then write it out."""
    if not 1 <= len(LINE) <= 140:
        return abort(f"line is {len(LINE)} characters, the gate allows 1-140")
    if not LINE.strip():
        return abort("line is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
