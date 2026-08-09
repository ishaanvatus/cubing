#!/bin/bash

magick $1 -monochrome -define png:color-type=2 $(basename $1 .png).bmp

#potrace --alphamax 1.5 -t 64 --svg $(basename $1 .png).bmp -o $(basename $1 .png).svg
potrace --svg $(basename $1 .png).bmp -o $(basename $1 .png).svg

