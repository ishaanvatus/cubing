#!/usr/bin/env bash
# Usage: ./play_pair.sh AB
# Finds letter_pairs/<first_letter>/<PAIR>_*.* (case-insensitive) and plays it in mpv on infinite loop.

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <letter_pair>  e.g. $0 AB" >&2
    exit 1
fi

pair="$1"
pair_upper=$(echo "$pair" | tr '[:lower:]' '[:upper:]')
first_letter_lower=$(echo "${pair_upper:0:1}" | tr '[:upper:]' '[:lower:]')

base_dir="letter_pairs/${first_letter_lower}"

if [ ! -d "$base_dir" ]; then
    echo "Directory not found: $base_dir" >&2
    exit 1
fi

# Case-insensitive match on files starting with PAIR_
match=$(find "$base_dir" -maxdepth 1 -type f -iname "${pair_upper}_*" | head -n 1)

if [ -z "$match" ]; then
    echo "No file found for pair '$pair_upper' in $base_dir" >&2
    exit 1
fi

echo "Playing: $match"
swallow mpv --loop=inf "$match"
