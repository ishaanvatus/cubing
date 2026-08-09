#!/bin/bash
set -e

INPUT="$1"

if [ -z "$INPUT" ] || [ ! -f "$INPUT" ]; then
    echo "Usage: ./make-stickers.sh sticker.svg"
    exit 1
fi

BASE="${INPUT%.*}"
A4SVG="${BASE}_A4.svg"
PDF="${BASE}_A4.pdf"

python3 - "$INPUT" "$A4SVG" <<'PY'
import sys
from pathlib import Path
from xml.sax.saxutils import escape

src = Path(sys.argv[1]).resolve().as_uri()
out = sys.argv[2]

# A4 = 210 x 297 mm
# Sticker = 12 x 12 mm
# Gap = 4 mm
# 13 x 18 = 234 stickers

# Grid size:
# 13 * 12 + 12 * 4 = 204 mm
# 18 * 12 + 17 * 4 = 284 mm
#
# Centered on A4:
# left = (210 - 204) / 2 = 3 mm
# top  = (297 - 284) / 2 = 6.5 mm

svg = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<svg xmlns="http://www.w3.org/2000/svg"',
    '     xmlns:xlink="http://www.w3.org/1999/xlink"',
    '     width="210mm" height="297mm" viewBox="0 0 210 297">',
]

for row in range(18):
    for col in range(13):
        x = 3 + col * 16
        y = 6.5 + row * 16

        svg.append(
            f'  <image x="{x}" y="{y}" width="12" height="12" '
            f'xlink:href="{escape(src)}" '
            f'preserveAspectRatio="xMidYMid meet"/>'
        )

svg.append('</svg>')

Path(out).write_text("\n".join(svg))
PY

inkscape "$A4SVG" --export-filename="$PDF"

echo
echo "DONE: $PDF"
echo "234 stickers, each 12 x 12 mm, with 4 mm gaps."
echo
echo "PRINT: A4 + 100% / Actual Size"
echo "DO NOT select Fit to Page."
