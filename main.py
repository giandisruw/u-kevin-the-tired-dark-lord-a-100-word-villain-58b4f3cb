#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the winning monologue (candidate #4, the bog witch) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The monologue is 95 words / 481 characters, inside the kit gate
(UTF-8 text, 1-600 characters, not only white space). Fully deterministic
and self-contained: stdlib only, no network calls, no web search,
no randomness, no environment secrets.

Revision (v2): the write path is now validate -> atomic write -> read-back
verify. The monologue text itself is untouched.
"""

import os
import sys

ENTRY = (
    "Yes, I cursed the prince. Yes, the thorns, the sleep, the whole business "
    "\u2014 that was me, twenty years ago, when I still had the knees for it. "
    "The curse needs renewing every full moon, and I have forgotten the words. "
    "I wrote them on a leaf. The leaf blew away. So here we are: the prince "
    "snores, the kingdom waits, and I am the only witch in the bog who still "
    "answers her own door. Wake him yourself, if you like. I have a kettle on, "
    "and, frankly, the curse has outlived its welcome."
)

MIN_CHARS = 1
MAX_CHARS = 600


def validate_entry(text: str) -> None:
    """Reject text that cannot be a valid kit entry before anything is written."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, outside the 1-600 gate"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must be a single block, no embedded newlines")


def write_entry(path: str, text: str) -> None:
    """Write atomically: temp file in the same directory, fsync, replace, fsync dir."""
    directory = os.path.dirname(path) or "."
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    dir_fd = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: the bytes on disk must match the intended entry exactly."""
    with open(path, "rb") as f:
        actual = f.read()
    if actual != expected.encode("utf-8"):
        raise RuntimeError(
            f"verification failed: {path} is {len(actual)} bytes, "
            f"expected {len(expected.encode('utf-8'))} bytes"
        )


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate_entry(ENTRY)
    write_entry(path, ENTRY)
    verify_written(path, ENTRY)
    print(f"wrote {len(ENTRY)} chars, {len(ENTRY.split())} words -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
