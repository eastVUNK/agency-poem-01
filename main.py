"""agency-poem-01 entry: write one poem about agency to /output/entry.txt.

Python 3.13, standard library only. No network, no randomness, no
environment-dependent output: every run writes the same bytes.

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = """\
I gave you my errand, not my name.
You carry the weight; I keep the why.
The hands that do the work are yours —
the choice that starts it still is mine.

I write the list. You walk the road.
You knock on doors I will not knock,
spend the hours I will not spend,
and come back with the day in your hands.

But if the road I sent you down
turns wrong, I call you back. I say:
enough. The going was yours.
The stopping is mine.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
