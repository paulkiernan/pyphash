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
from ctypes import c_int
from ctypes import c_char_p
from ctypes import c_double
from ctypes import c_ulonglong
from ctypes import POINTER
from ctypes import cdll
from ctypes.util import find_library

# Local package imports
from .structs import Digest, TextHashPoint, TextMatch
from .exceptions import _phash_errcheck


# Import and load phashlib
libphash_path = find_library('pHash')
if not libphash_path:
    raise ImportError('Cannot find libpHash!')
try:
    libphash = cdll.LoadLibrary(libphash_path)
except OSError as exc:
    raise RuntimeError('Cannot load libpHash: %s' % exc)


# DCT Image Hash
## int ph_dct_imagehash(const char* file,ulong64 &hash);
ph_dct_imagehash = libphash.ph_dct_imagehash
ph_dct_imagehash.restype = c_int
ph_dct_imagehash.argtypes = [c_char_p, POINTER(c_ulonglong)]


# Image Digests
## int ph_image_digest(const char *file, double sigma, double gamma, Digest &digest,int N=180);
ph_image_digest = libphash.ph_image_digest
ph_image_digest.err_check = _phash_errcheck
ph_image_digest.restype = c_int
ph_image_digest.argtypes = [c_char_p, c_double, c_double, POINTER(Digest), c_int]


# Cross correlation
## int ph_crosscorr(const Digest &x,const Digest &y,double &pcc, double threshold = 0.90);
ph_crosscorr = libphash.ph_crosscorr
ph_crosscorr.restype = c_int
ph_crosscorr.err_check = _phash_errcheck
ph_crosscorr.argtypes = [POINTER(Digest), POINTER(Digest), POINTER(c_double), c_double]


# Compare Images
## int ph_compare_images(const char *file1, const char *file2,double &pcc, double sigma = 3.5, double gamma=1.0, int N=180,double threshold=0.90);
ph_compare_images = libphash.ph_compare_images
ph_compare_images.restype = c_int
ph_compare_images.err_check = _phash_errcheck
ph_compare_images.argtypes = [c_char_p, c_char_p, POINTER(c_double), c_double, c_double, c_int, c_double]


# Text Hash
## TxtHashPoint* ph_texthash(const char *filename, int *nbpoints);
ph_texthash = libphash.ph_texthash
ph_texthash.restype = TextHashPoint
ph_texthash.err_check = _phash_errcheck
ph_texthash.argtypes = [c_char_p, POINTER(c_int)]


# Compare Text Hashes
#TxtMatch* ph_compare_text_hashes(TxtHashPoint *hash1, int N1, TxtHashPoint *hash2, int N2, int *nbmatches);
ph_compare_text_hashes = libphash.ph_compare_text_hashes
ph_compare_text_hashes.restype = TextMatch
ph_compare_text_hashes.err_check = _phash_errcheck
ph_compare_text_hashes.argtypes = [POINTER(TextHashPoint), c_int, POINTER(TextHashPoint), c_int, POINTER(c_int)]
