"""Entry program for the 'One-Star Review of Something Essential' make.fun bounty.

The entry is a deadpan one-star review, at most 160 characters, of an
everyday essential everyone relies on: gravity. The program writes
exactly that one line to /output/entry.txt (an optional first argument
overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "One star for gravity. It dropped my phone, my toast, and my dignity "
    "— all before 9 a.m. Zero refunds, and it happens every single day."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert LINE.startswith("One star"), "a one-star review starts with its rating"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
