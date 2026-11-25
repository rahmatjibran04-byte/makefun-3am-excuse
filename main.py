#!/usr/bin/env python3
"""The 3 AM Excuse - make.fun bounty entry.

Writes one line (under 200 characters) in the voice of a hardware wallet
that refuses to sign a transaction at 3 AM: personality, reason and joke
in a single breath.

Run: python3 main.py  (writes /output/entry.txt)
"""

import os

ENTRY = (
    "It's 3 AM \u2014 my private keys are already asleep, and last time "
    "I woke them you bought a frog coin and blamed me. "
    "Not tonight, insomniac."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
