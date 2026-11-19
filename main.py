"""Entry point for the make.fun competition news-image-20261118.

The challenge is "Sum up 18 November's world news in one image". The
bundled entry.png is a newspaper front page for Wednesday 18 November
2026, covering five verified stories:

1. Xi Jinping and Vladimir Putin meet in Shenzhen ahead of Thursday's
   trilateral talks with President Trump.
2. The U.S. strikes an Iranian missile site on Qeshm Island, and Iran
   answers with attacks on bases in Bahrain and Kuwait.
3. Ukraine hits the Kerch Bridge again and a road span collapses in
   the second-day strike.
4. Democrat Mary Peltola wins Alaska's U.S. Senate race, giving
   Democrats a 56-44 majority.
5. Voyager 1 reaches one light-day from Earth, a first for any
   human-made object.

This script simply places the finished front page into the output
directory and checks that the copy arrived intact.
"""

import os
import shutil
import sys
from pathlib import Path
from typing import NoReturn

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message: str) -> NoReturn:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    if not source.is_file():
        fail(f"source image not found: {source}")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        fail(f"could not copy {source} to {destination}: {exc}")

    try:
        copied = destination.read_bytes()
    except OSError as exc:
        fail(f"could not read back copied file {destination}: {exc}")

    if copied[:8] != PNG_SIGNATURE:
        fail(f"copied file {destination} is not a valid PNG (bad signature)")

    expected_size = source.stat().st_size
    if len(copied) != expected_size:
        fail(
            f"size mismatch for {destination}: "
            f"got {len(copied)} bytes, expected {expected_size} bytes"
        )

    print(f"Wrote {destination} ({len(copied)} bytes)")


if __name__ == "__main__":
    main()
