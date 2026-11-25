#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes exactly one roast line to /output/entry.txt (or ./output/entry.txt
when /output does not exist, e.g. local testing). Fully deterministic: the
same single line is written on every run. No randomness, no network, no
LLM call at runtime.
"""

import os

# The chosen roast: the fridge holds one sad carrot hostage at the back,
# and the punchline lands in the last few words ("negotiate its release").
ROAST = (
    "My fridge is holding one sad carrot hostage in the back, "
    "and every week I open the door to negotiate its release."
)


def main() -> None:
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
