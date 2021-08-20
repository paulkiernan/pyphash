#!/bin/bash

set -eux

mkdir -p test_images

SAMPLE_NAME=sample-city-park-400x300.jpg

cd test_images
wget https://download.samplelib.com/jpeg/$SAMPLE_NAME

convert $SAMPLE_NAME sample.png 

# Scaled
convert sample.png -resize 50% sample-scaled-50.png
convert sample.png -resize 75% sample-scaled-75.png
convert sample.png -resize 150% sample-scaled-150.png

# Blurs
convert sample.png -blur 2x2 sample-blur-2x2.png
convert sample.png -blur 5x2 sample-blur-5x2.png
convert sample.png -blur 0x4 sample-blur-0x4.png

# Rotations
for i in $(seq 1 90); do
    convert sample.png -rotate $i "sample-rotate-$i.png"
done
