#!/usr/bin/env python3
"""The most boring object, reviewed in one line.

Writes the one-line review to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Standard library only. No trailing newline.
"""

import os

TEXT = (
    "There are eleven teaspoons in this drawer. Nine are missing. "
    "This one has stirred 3,000 cups of tea and never left the house. "
    "It has perfect attendance. Its name is Colin."
)


def main() -> None:
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    # Read-back validation: exact content, 171 chars, 1 line, 0 newlines.
    with open(path, "r", encoding="utf-8", newline="") as f:
        data = f.read()
    assert data == TEXT, "read-back mismatch"
    assert len(data) == 171, f"expected 171 chars, got {len(data)}"
    assert data.count("\n") == 0, "unexpected newline"
    assert len(data.splitlines()) == 1, "expected exactly 1 line"
    assert data.rstrip().endswith("Colin.") and "3,000" in data, "spoon name or count missing"


if __name__ == "__main__":
    main()
