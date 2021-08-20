#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" basic image compare """

import sys

# Custom libphash bindings
import pyphash as phash

# Helpers
def hamming_distance(string1, string2):
    return sum(map(str.__ne__, string1, string2))

def get_image_hashes(imagename):
    base_image_path = imagename
    base_phash_digest = phash.image_digest(base_image_path)
    base_phash_imagehash = phash.imagehash(base_image_path)
    return (base_phash_digest, base_phash_imagehash)

def test_image_correlations(image1, image2):
    hashes1 = get_image_hashes(image1)
    hashes2 = get_image_hashes(image2)

    print("{} pHash digest: {} and DCT: {}".format(image1, hashes1[0], hashes1[1]))
    print("{} pHash digest: {} and DCT: {}".format(image2, hashes2[0], hashes2[1]))

    print("Cross-correlation: %5.2f%%" % (
        100 * phash.cross_correlation(hashes1[0], hashes2[0])
    ))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please specify two images on the command-line")
        sys.exit(1)
    image1 = sys.argv[1]
    image2 = sys.argv[2]
    test_image_correlations(image1, image2)