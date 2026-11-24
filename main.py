"""Write one short roast line for make.fun, byte for byte, without a trailing newline."""

import os
import sys
from pathlib import Path

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def output_dir() -> Path:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
