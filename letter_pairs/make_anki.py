#!/usr/bin/env python3
import re
from pathlib import Path
import genanki

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "speffz_letter_pairs.apkg"

MODEL_ID = 1607392319
DECK_ID = 2059400110

MODEL = genanki.Model(
    MODEL_ID,
    "Speffz Letter Pair",
    fields=[{"name": "Code"}, {"name": "Back"}],
    templates=[
        {
            "name": "Code to Image",
            "qfmt": '<div style="font-size: 48px; text-align: center;">{{Code}}</div>',
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        }
    ],
    css=".card { font-family: arial; font-size: 20px; text-align: center; color: black; background: white; }",
)

DECK = genanki.Deck(DECK_ID, "Speffz Letter Pairs")

CODE_RE = re.compile(r"^([A-Z][A-Z])_(.+)\.[A-Za-z]+$")
BARE_RE = re.compile(r"^([A-Z][A-Z])\.[A-Za-z]+$")


def main():
    media = []
    for letter_dir in sorted(ROOT.iterdir()):
        if not letter_dir.is_dir():
            continue
        for path in sorted(letter_dir.iterdir()):
            m = CODE_RE.match(path.name) or BARE_RE.match(path.name)
            if not m:
                continue
            code = m.group(1)
            mnemonic = m.group(2).replace("_", " ") if m.lastindex == 2 else code
            DECK.add_note(
                genanki.Note(
                    model=MODEL,
                    fields=[code, f'<img src="{path.name}"><br>{mnemonic}'],
                )
            )
            media.append(str(path))

    genanki.Package(DECK, media_files=media).write_to_file(str(OUTPUT))
    print(f"Wrote {OUTPUT} with {len(media)} cards.")


if __name__ == "__main__":
    main()
