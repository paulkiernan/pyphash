#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" phashlib Python Interface

This file contains all the python-friendly code in the modules. Most of these
methods are simply wrappers to the defined C functions.
"""

# Future-proof
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Standard Library Imports
from ctypes import c_int
from ctypes import c_double
from ctypes import c_ulonglong
from ctypes import byref
from ctypes import pointer

# Local package imports
from .core import ph_dct_imagehash
from .core import ph_image_digest
from .core import ph_crosscorr
from .core import ph_compare_images
from .core import ph_texthash
from .core import ph_compare_text_hashes
from .helpers import _filename_bytes
from .structs import Digest


def imagehash(filename):
    """
    Compute discrete cosine transform robust image hash

    @param filename: str, path to image on which we want to compute the hash
    @returns: int, DCT hash
    """

    _hash = c_ulonglong()
    ph_dct_imagehash(
        _filename_bytes(filename),
        byref(_hash)
    )
    return _hash.value


def image_digest(filename, sigma=1.0, gamma=1.0, lines=180):
    """
    Image Digest, compute the image digest given the file name

    @param filename: str, value for file name of the input image
    @param sigma: float, value for the deviation for the gaussian filter
    @param gamma: float, value for the gamma correction on the input image
    @param lines: int, value for number of angles to consider
    @returns: Digest, digest struct
    """

    d = Digest()

    ph_image_digest(
        _filename_bytes(filename),
        sigma,
        gamma,
        d,
        lines
    )

    return d


def cross_correlation(digest_1, digest_2, threshold=0.90):
    """
    Cross Correlation for 2 series
    Compute the cross correlation of the two series vectors. The peak of cross
    correlation between the two vectors is returned in the pcc parameter passed
    by reference to the ph_crosscorr function.

    @param digest_1: Digest, digest struct of the first image
    @param digest_2: Digest, digest struct of the second image
    @param threshold: float, value for the threshold value for which 2 images
                      are considered the same or different
    @returns: float, the value for the peak of cross correlation
    """

    pcc = c_double()
    ph_crosscorr(
        pointer(digest_1),
        pointer(digest_2),
        byref(pcc),
        threshold
    )
    return pcc.value


def compare_images(file1, file2, sigma=3.5, gamma=1.0, lines=180, threshold=0.90):
    """
    Compare 2 images given their file names

    @param file1: str, path to first image file
    @param file2: str, path to second image file
    @param sigma: float, value for the deviation for the gaussian filter
    @param gamma: float, value for the gamma correction on the input image
    @param lines: int, value for number of angles to consider
    @param threshold: float, value for the threshold value for which 2 images
                      are considered the same or different
    @returns: float, the value for the peak of cross correlation
    """

    pcc = c_double()
    ph_compare_images(
        _filename_bytes(file1),
        _filename_bytes(file2),
        byref(pcc),
        sigma,
        gamma,
        lines,
        threshold
    )
    return pcc.value


def texthash(filename):
    """
    Textual hash for a file

    @param filename: str, path to the file to hash
    @param nbpoints: int, length of array of return value (out)
    @returns: TextHashPoint, array of hash points with respective index into file
    """

    _nbpoints = c_int()
    text_hash_point = ph_texthash(
        _filename_bytes(filename),
        _nbpoints
    )
    text_hash_point.length = _nbpoints.value
    return text_hash_point


def compare_text_hashes(hash1, hash2):
    """
    Compare 2 Text Hashes

    @param hash1: TextHashPoint, hash of the first text
    @param hash2: TextHashPoint, hash of the second text
    @returns: TextMatch, list of all matches
    """

    _nbpoints = c_int()
    text_match = ph_compare_text_hashes(
        hash1,
        hash1.length,
        hash2,
        hash2.length,
        _nbpoints
    )
    text_match.matching_words = _nbpoints.value

    return text_match
