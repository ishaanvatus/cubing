#!/bin/bash

FILE="Speffz Images A-X no repeats.apkg"
PART_PREFIX="part_"

#split -b 32M "$FILE" "$PART_PREFIX"
#
#echo "File split into parts with prefix '$PART_PREFIX'."

recombine() {
    cat ${PART_PREFIX}* > "$FILE"
    echo "File recombined as '$FILE'."
}

recombine
