#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" phashlib Core C++ interface
"""

# Third-party Libraries
import matplotlib.pyplot as plt

# Custom libphash bindings
import pyphash as phash
print(phash)
print(dir(phash))


TEST_IMAGES = {
    'base': 'test_images/sample.png',
    'blurs': {
        '2x2': 'test_images/sample-blur-2x2.png',
        '5x2': 'test_images/sample-blur-5x2.png',
        '0x4': 'test_images/sample-blur-0x4.png',
    },
    'rotations': {
        '10°': 'test_images/sample-rotate-10.png',
        '30°': 'test_images/sample-rotate-30.png',
        '70°': 'test_images/sample-rotate-70.png',
        '90°': 'test_images/sample-rotate-90.png',
    },
    'scaled': {
        '50%': 'test_images/sample-scaled-50.png',
        '75%': 'test_images/sample-scaled-75.png',
        '150%': 'test_images/sample-scaled-150.png',
    }
}

# Helpers
def hamming_distance(string1, string2):
    return sum(map(str.__ne__, string1, string2))


def test_image_correlations(image_distortion_type):
    base_image_path = TEST_IMAGES.get('base')
    base_phash_digest = phash.image_digest(base_image_path)
    base_phash_imagehash = phash.imagehash(base_image_path)

    print("pHash Digest: {0}".format(base_phash_digest))
    print("pHash DCT Hash: {0}".format(base_phash_imagehash))

    for distortion_info, image_path in TEST_IMAGES.get(image_distortion_type).items():
        _image_phash_digest = phash.image_digest(image_path)
        _image_phash_imagehash = phash.imagehash(image_path)
        print("pHash Digest: {0}".format(_image_phash_digest))
        print("pHash DCT Hash: {0}".format(_image_phash_imagehash))
        print("pHash DCT Hash Hamming Distance: {0}".format(
            hamming_distance(
                str(base_phash_imagehash),
                str(_image_phash_imagehash)
            )
        ))
        print("Cross-correlation on Base vs. %s %s: %5.2f%%" % (
            distortion_info,
            image_distortion_type,
            100 * phash.cross_correlation(base_phash_digest, _image_phash_digest)
        ))


def test_rotations():
    base_image_path = TEST_IMAGES.get('base')
    base_phash_digest = phash.image_digest(base_image_path)

    correlations = []
    for x in range(1, 90):
        _image_path = "test_images/sample-rotate-{0}.png".format(x)
        _image_phash_digest = phash.image_digest(_image_path)
        correlations.append((
            x,
            phash.cross_correlation(base_phash_digest, _image_phash_digest)
        ))

    return list(zip(*correlations))

if __name__ == "__main__":
    test_image_correlations('scaled')
    test_image_correlations('blurs')
    test_image_correlations('rotations')
    xx, yy = test_rotations()
    plt.plot(xx, yy)
    plt.plot(xx[:10], yy[:10])
    plt.plot(xx[-10:], yy[-10:])
