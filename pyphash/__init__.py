#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" phashlib Python Interface
"""

# Future-proof
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Local Package imports
from .extensions import imagehash
from .extensions import image_digest
from .extensions import cross_correlation
from .extensions import compare_images
from .extensions import texthash
from .extensions import compare_text_hashes


# Package definitions
ALL = [
    'imagehash',
    'image_digest',
    'cross_correlation',
    'compare_images',
    'texthash',
    'compare_text_hashes',
]
