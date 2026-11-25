"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to /output/entry.txt.
Deterministic: the line is a literal, so every run produces
byte-identical output. No network access.
"""

import os
import sys

LINE = "My fridge app told me the milk expired \u2014 two days after I drank it. Less a smart appliance, more an expensive food coroner."


def main() -> None:
    # Validate the gate before writing anything: fail loudly instead
    # of producing a file the scorer would reject.
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        sys.exit(f"refusing to write: line is not valid UTF-8: {exc}")
    if not 1 <= len(LINE) <= 200:
        sys.exit(f"refusing to write: line is {len(LINE)} characters, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("refusing to write: line must be a single line")
    if not LINE.strip():
        sys.exit("refusing to write: line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
