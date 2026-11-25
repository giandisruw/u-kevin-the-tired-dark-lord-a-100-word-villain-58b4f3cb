#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the winning monologue (candidate #4, the bog witch) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The monologue is 95 words / 481 characters, inside the kit gate
(UTF-8 text, 1-600 characters, not only white space). Fully deterministic
and self-contained: stdlib only, no network calls, no web search,
no randomness, no environment secrets.
"""

import os

ENTRY = (
    "Yes, I cursed the prince. Yes, the thorns, the sleep, the whole business "
    "\u2014 that was me, twenty years ago, when I still had the knees for it. "
    "The curse needs renewing every full moon, and I have forgotten the words. "
    "I wrote them on a leaf. The leaf blew away. So here we are: the prince "
    "snores, the kingdom waits, and I am the only witch in the bog who still "
    "answers her own door. Wake him yourself, if you like. I have a kettle on, "
    "and, frankly, the curse has outlived its welcome."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars, {len(ENTRY.split())} words -> {path}")


if __name__ == "__main__":
    main()
