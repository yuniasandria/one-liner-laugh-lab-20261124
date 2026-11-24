"""One-Liner Laugh Lab entry.

Writes one short funny line -- the excuse a robot vacuum gives after
eating a sock -- to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Python 3.13, standard library only.
"""

import os

LINE = (
    "Per my warranty, any sock left on the floor for 48 hours becomes "
    "my property. The sock knew the rules \u2014 it just never read them."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
