#!/bin/bash

FILE="Speffz Images A-X no repeats.apkg"
PART_PREFIX="part_"

merge() {
    cat ${PART_PREFIX}* > "$FILE"
    echo "merged parts as '$FILE'."
}

merge
