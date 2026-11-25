"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to /output/entry.txt.
Deterministic: the line is a literal, so every run produces
byte-identical output. No network access.
"""

import os

LINE = "My fridge app notified me the milk expired \u2014 two days after I drank it. Less a smart appliance, more a very expensive obituary writer."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
