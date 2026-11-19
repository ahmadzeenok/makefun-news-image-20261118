#!/usr/bin/env python3
"""Write the 18 November 2026 world-news image to the output directory.

This program is the entry for the make.fun competition
`news-image-20261118`: "Sum up 18 November's world news in one image".

The bundled entry.png is a newspaper front page for Wednesday
18 November 2026, covering the day's five biggest stories:

  1. Lead story -- Xi Jinping and Vladimir Putin meet in
     Shenzhen ahead of Thursday's trilateral talks with
     President Trump.
  2. The U.S. strikes an Iranian missile site on Qeshm
     Island; Iran answers with attacks on bases in Bahrain
     and Kuwait.
  3. Ukraine hits the Kerch Bridge again; a road span
     collapses in the second-day strike.
  4. Democrat Mary Peltola wins Alaska's U.S. Senate race,
     giving Democrats a 56-44 majority.
  5. Voyager 1 reaches one light-day from Earth, a first
     for any human-made object.

The program copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output). Python 3.13, standard library only, no network.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
