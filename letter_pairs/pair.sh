#!/usr/bin/env bash
# Usage: ./pair.sh EM
# Looks up the mnemonic image/video for a letter pair and opens it.
# Run from the root dir containing a/ b/ c/ ... x/ (same place as main.py).

set -euo pipefail

pair="${1:-}"
if [[ -z "$pair" ]]; then
    echo "Usage: $0 <PAIR>   e.g. $0 EM" >&2
    exit 1
fi

pair="${pair^^}"        # e.g. em -> EM
letter="${pair:0:1}"
folder="${letter,,}"    # e.g. E -> e

if [[ ! -d "$folder" ]]; then
    echo "No folder '$folder' here. Run this from the root dir (with a/ b/ c/...)." >&2
    exit 1
fi

# Match "<PAIR>_*.*" case-insensitively, first hit only.
match=$(find "$folder" -maxdepth 1 -type f -iname "${pair}_*" | sort | head -n 1)

if [[ -z "$match" ]]; then
    echo "No file found for pair '$pair' in $folder/" >&2
    exit 1
fi

ext="${match##*.}"
ext="${ext,,}"

case "$ext" in
    webm|mp4|mov)
        # Not an image -- hand video files to mpv instead of sxiv.
        exec swallow mpv "$match"
        ;;
    *)
        exec swallow nsxiv "$match"
        ;;
esac
