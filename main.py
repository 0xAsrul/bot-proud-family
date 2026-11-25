#!/usr/bin/env python3
"""Write one short family scene to /output/entry.txt."""
import os

SCENE = (
    "Dad finally fixed the wobbly kitchen table — then sat down, and it wobbled again.\n"
    "Our six-year-old patted his arm and said, \"It's okay, Dad. You're the wobble now.\" "
    "We laughed until the table gave up and stayed still."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
