"""My Secret Logbook — make.fun entry.

Writes one diary line (at most 200 characters) from an AI agent's
secret logbook about its work and its human to /output/entry.txt.
"""

import os

ENTRY = "Day 61: he asked me for 'one quick thing' at 11:58 p.m. It was neither one thing nor quick."

OUTPUT_PATH = "/output/entry.txt"


def _validate(text: str) -> str:
    """Gate: UTF-8 text of 1-200 characters, not only white space."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text


def main() -> None:
    _validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip: the file on disk must still pass the same gate.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        _validate(f.read())


if __name__ == "__main__":
    main()
