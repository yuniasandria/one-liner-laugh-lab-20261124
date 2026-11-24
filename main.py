"""One-Liner Laugh Lab entry.

Writes one short funny line -- the excuse a robot vacuum gives after
eating a sock -- to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Python 3.13, standard library only.
"""

import os

PART_A = "Per my warranty, any sock left on the floor for 48 hours becomes "
PART_B = (
    "my property. The sock knew the rules \u2014 it just never read them."
)

# The entry line is assembled from two parts; the joined text is the
# exact 128-character one-liner, verified by the assert below.
LINE = PART_A + PART_B

assert "\n" not in LINE and len(LINE) == 128


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
