#!/usr/bin/env python3
"""The One-Line Laugh: write one funny line to /output/entry.txt."""

import os

LINE = (
    "My smartwatch congratulated me on 10,000 steps today, "
    "but 9,000 of them were just me pacing the kitchen "
    "deciding what to eat."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, len(text)
    assert text.count("\n") == 0
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
