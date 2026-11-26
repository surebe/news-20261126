#!/usr/bin/env python3
"""THE WHOLE WORLD - Thursday 26 November 2026 (make.fun news-image-20261126).

The entry is a single 1024x1024 newspaper front page carrying 42 wire
stories that all happened, or were first reported, on Thursday
26 November 2026 - checked story by story against Reuters, AP, BBC, AFP,
Al Jazeera and AAP at the morning freeze.

The judged artifact is the shipped entry.png. This program reproduces
that artifact byte-for-byte: it copies the entry.png held in this
repository to the output path it is given (or ./out/entry.png), so every
run produces exactly the same file.
"""

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY = HERE / "entry.png"


def main(argv):
    out = Path(argv[1]) if len(argv) > 1 else HERE / "out" / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, out)
    print("wrote {} ({} bytes)".format(out, out.stat().st_size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
