"""One Line, One Laugh — make.fun entry.

Writes a single sharp funny line to /output/entry.txt.
Deterministic: no network, no randomness, no input.
"""
import os

LINE = (
    "I told my houseplant it was the only thing in my life I hadn't "
    "disappointed, and it immediately started dying."
)


def main() -> None:
    # Gate: the entry must be 1-140 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 140, "line must fit the 140-character cap"
    assert LINE.strip(), "line must not be only whitespace"
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
