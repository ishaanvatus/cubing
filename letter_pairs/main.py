#!/usr/bin/env python3
"""
Build an Anki deck from a folder of 3BLD memo-pair images/videos.

Expected input layout (as produced by your split.sh / shown in your tree):
    SOURCE_DIR/
        a/
            AB_abs.jpg
            AC_air_conditioner.jpg
            ...
        b/
            BA_BAnana.jpg
            ...
        ...

Front of card  -> the two-letter pair, uppercase (e.g. "AB")
Back of card   -> the word/phrase derived from the filename, plus the
                  image or video itself.

Word derivation:
    1. Strip the leading "XY_" prefix (the two-letter code + underscore).
    2. Repeatedly strip known media extensions from the end
       (handles double-extension typos like "GAtorade.png.jpg" -> "GAtorade").
    3. Replace any remaining underscores/dashes with spaces.
       (e.g. "Nod-Don" -> "Nod Don", "AI_spaghetti" -> "AI spaghetti")
    4. Collapse extra whitespace.

Sizing:
    - Both images and videos are capped at 70% of the viewport width/height
      (only shrunk if larger than that, aspect ratio preserved) via
      max-width/max-height + auto width/height. This is CSS-only scaling;
      the original source files on disk are never modified.

Install dependency first:
    pip install genanki --break-system-packages

Usage:
    python3 build_bld_deck.py
    (edit SOURCE_DIR / OUTPUT_FILE below, or pass them as CLI args)
"""

import os
import re
import sys
import genanki

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SOURCE_DIR = sys.argv[1] if len(sys.argv) > 1 else "."
OUTPUT_FILE = sys.argv[2] if len(sys.argv) > 2 else "Speffz_A_to_Z.apkg"

DECK_NAME = "3BLD Memo Pairs"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif"}
VIDEO_EXTS = {".webm", ".mp4", ".mov"}
MEDIA_EXTS = IMAGE_EXTS | VIDEO_EXTS

# Any of these trailing extensions get stripped repeatedly when building
# the display word, to clean up double-extension filenames.
STRIPPABLE_EXTS = MEDIA_EXTS | {".png", ".jpg", ".jpeg", ".gif", ".webm", ".mp4", ".mov"}

# Fixed IDs so re-running the script updates the same deck/model instead of
# creating duplicates in Anki. Don't change these once you've imported once.
MODEL_ID = 1607392319
DECK_ID = 2059400110

# ---------------------------------------------------------------------------
# Anki model (card template + styling)
# ---------------------------------------------------------------------------

CSS = """
.card {
    font-family: Helvetica, Arial, sans-serif;
    text-align: center;
    background-color: white;
    color: black;
}

.pair {
    font-size: 64px;
    font-weight: bold;
    letter-spacing: 4px;
    margin: 40px 0;
}

.word {
    font-size: 28px;
    margin-bottom: 16px;
}

.media {
    margin-top: 12px;
}

/* Images: scaled to fit via CSS only (source files are never modified). */
.card img {
    max-width: 70vw;
    max-height: 70vh;
    width: auto;
    height: auto;
}

/* Videos: capped at 70% of the viewport, only shrunk if larger, aspect ratio kept. */
.card video {
    max-width: 70vw;
    max-height: 70vh;
    width: auto;
    height: auto;
}
"""

model = genanki.Model(
    MODEL_ID,
    "3BLD Memo Pair Model",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Pair -> Word/Image",
            "qfmt": "{{Front}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        },
    ],
    css=CSS,
)

deck = genanki.Deck(DECK_ID, DECK_NAME)
media_files = []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def derive_word(rest: str) -> str:
    """Turn 'GAtorade.png.jpg' -> 'GAtorade', 'Nod-Don' -> 'Nod Don', etc."""
    name = rest
    while True:
        base, ext = os.path.splitext(name)
        if ext.lower() in STRIPPABLE_EXTS:
            name = base
        else:
            break
    name = re.sub(r"[_\-]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def media_tag(filename: str, ext: str) -> str:
    if ext.lower() in VIDEO_EXTS:
        return f'<video controls><source src="{filename}"></video>'
    return f'<img src="{filename}">'


# ---------------------------------------------------------------------------
# Build the deck
# ---------------------------------------------------------------------------

count = 0
for root, _dirs, files in os.walk(SOURCE_DIR):
    for fname in sorted(files):
        base, ext = os.path.splitext(fname)
        if ext.lower() not in MEDIA_EXTS:
            continue  # skip merge.sh, split.sh, etc.
        if "_" not in base:
            print(f"Skipping (no underscore separator): {fname}")
            continue

        code_part, rest = base.split("_", 1)
        pair = code_part.strip().upper()
        word = derive_word(rest)

        full_path = os.path.join(root, fname)
        front_html = f'<div class="pair">{pair}</div>'
        back_html = (
            f'<div class="word">{word}</div>'
            f'<div class="media">{media_tag(fname, ext)}</div>'
        )

        note = genanki.Note(model=model, fields=[front_html, back_html])
        deck.add_note(note)
        media_files.append(full_path)
        count += 1

print(f"Built {count} cards.")

package = genanki.Package(deck)
package.media_files = media_files
package.write_to_file(OUTPUT_FILE)

print(f"Wrote {OUTPUT_FILE}")
