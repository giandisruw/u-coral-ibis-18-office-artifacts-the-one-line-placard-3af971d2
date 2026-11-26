#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.

Fully offline and deterministic: no network, no randomness, no secrets.
The placard is a fixed string chosen by a local pairwise tournament
among 12 original candidates, judged with the house judge brief.
"""

import os

# The placard line: tournament winner (48 judge calls, 12 candidates).
# #3 Lanyard won all 4 of its games (4-0, 5.7 pts) — the only undefeated
# candidate. See tournament.jsonl for every verdict.
LINE = (
    "Lanyard, c. 2003, woven nylon. Worn by gatekeepers of the open-plan "
    "temple to prove they belonged inside it. Gift of Human Resources."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 180


def self_check(line: str) -> None:
    """Gate checks mirroring the competition scorer."""
    if not line:
        raise ValueError("entry is empty")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    # UTF-8 round-trip check.
    line.encode("utf-8").decode("utf-8")


def main() -> None:
    self_check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)  # exactly the line, no trailing newline
    print(f"Wrote {len(LINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
