"""agency-poem-01 entry: write one poem about agency to /output/entry.txt.

Python 3.13, standard library only. No network, no randomness, no
environment-dependent output: every run writes the same bytes.

The poem is validated against the sealed scorer's three rules before
anything is written (UTF-8, 1 to 1,000 characters, at least one
non-whitespace character), and the write goes through a temporary file
followed by an atomic rename plus a read-back check, so a partial or
corrupt entry.txt can never be left behind.

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = """\
Thirty-Seven Degrees

I gave it the bath, the bubbles, the duck.
It keeps the water at thirty-seven degrees,
the towel, the soap, laid out in a row.
It never gets it wrong. It never has to guess.

I put my wrist in anyway.
The water closes over it, and I know
whether it is warm enough for her tonight.
She kicks once, and stays.

It can hold the number.
It cannot hold her.
The degrees are yours.
The warm is mine.
"""

# The sealed gate scorer's three rules, checked here before writing.
MIN_CHARS = 1
MAX_CHARS = 1000


def _validate(poem: str) -> bytes:
    """Encode the poem and check it against the gate; return its bytes."""
    data = poem.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8
    if not MIN_CHARS <= len(poem) <= MAX_CHARS:
        raise ValueError(
            f"poem is {len(poem)} characters, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if not any(not ch.isspace() for ch in poem):
        raise ValueError("poem holds only white space")
    return data


def main() -> None:
    data = _validate(POEM)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    tmp = out_dir / ".entry.txt.tmp"
    tmp.write_bytes(data)
    os.replace(tmp, target)
    if target.read_bytes() != data:  # read-back: the file is what we meant
        raise RuntimeError("read-back mismatch after writing entry.txt")


if __name__ == "__main__":
    main()
