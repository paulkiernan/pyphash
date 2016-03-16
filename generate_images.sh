#!/bin/bash

set -eux

mkdir -p test_images

cd test_images
wget http://s3.amazonaws.com/i.jpg.to/l/8453 -O tony.jpg

convert tony.jpg tony.png

# Scaled
convert tony.png -resize 50% tony-scaled-50.png
convert tony.png -resize 75% tony-scaled-75.png
convert tony.png -resize 150% tony-scaled-150.png

# Blurs
convert tony.png -blur 2x2 tony-blur-2x2.png
convert tony.png -blur 5x2 tony-blur-5x2.png
convert tony.png -blur 0x4 tony-blur-0x4.png

# Rotations
for i in $(seq 1 360); do
    convert tony.png -rotate $i "tony-rotate-$i.png"
done
