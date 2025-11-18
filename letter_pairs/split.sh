#!/bin/bash

FILE="Speffz Images A-X no repeats.apkg"
PART_PREFIX="part_"

split -b 32M "$FILE" "$PART_PREFIX"

echo "split into parts with name '$PART_PREFIX'."
