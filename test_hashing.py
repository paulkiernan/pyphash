#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" phashlib Core C++ interface
"""

# Future-proof
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Standard Library Imports
from hashlib import md5
from itertools import imap

# Third-party Libraries
import matplotlib.pyplot as plt
from IPython.display import Image, display

# Custom libphash bindings
import python_phash as phash
print(phash)
print(dir(phash))


TEST_IMAGES = {
    'base': 'test_images/tony.png',
    'blurs': {
        '2x2': 'test_images/tony-blur-2x2.png',
        '5x2': 'test_images/tony-blur-5x2.png',
        '0x4': 'test_images/tony-blur-0x4.png',
    },
    'rotations': {
        '10°': 'test_images/tony-rotate-10.png',
        '30°': 'test_images/tony-rotate-30.png',
        '90°': 'test_images/tony-rotate-90.png',
        '180°': 'test_images/tony-rotate-180.png',
    },
    'scaled': {
        '50%': 'test_images/tony-scaled-50.png',
        '75%': 'test_images/tony-scaled-75.png',
        '150%': 'test_images/tony-scaled-150.png',
    }
}

# Helpers
def hamming_distance(string1, string2):
    return sum(imap(str.__ne__, string1, string2))


def test_image_correlations(image_distortion_type, is_ipython_notebook=False):

    base_image_path = TEST_IMAGES.get('base')
    base_image = Image(filename=base_image_path)
    base_phash_digest = phash.image_digest(base_image_path)
    base_phash_imagehash = phash.imagehash(base_image_path)
    base_md5_digest = md5(open(base_image_path).read()).hexdigest()

    if is_ipython_notebook:
        display(base_image)
    print("md5 Digest: {0}".format(base_md5_digest))
    print("pHash Digest: {0}".format(base_phash_digest))
    print("pHash DCT Hash: {0}".format(base_phash_imagehash))

    for distortion_info, image_path in TEST_IMAGES.get(image_distortion_type).iteritems():
        _image = Image(filename=image_path)
        if is_ipython_notebook:
            display(_image)
        _image_phash_digest = phash.image_digest(image_path)
        _image_phash_imagehash = phash.imagehash(image_path)
        _image_md5_digest = md5(open(image_path).read()).hexdigest()
        print("md5 Digest: {0}".format(_image_md5_digest))
        print("md5 Hamming Distance: {0}".format(hamming_distance(base_md5_digest, _image_md5_digest)))
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
    for x in xrange(1, 361):
        _image_path = "test_images/tony-rotate-{0}.png".format(x)
        _image_phash_digest = phash.image_digest(_image_path)
        correlations.append((
            x,
            phash.cross_correlation(base_phash_digest, _image_phash_digest)
        ))

    return zip(*correlations)

test_image_correlations('scaled', is_ipython_notebook=False)
test_image_correlations('blurs', is_ipython_notebook=False)
test_image_correlations('rotations', is_ipython_notebook=False)
xx, yy = test_rotations()
plt.plot(xx, yy)
plt.plot(xx[:10], yy[:10])
plt.plot(xx[-10:], yy[-10:])
