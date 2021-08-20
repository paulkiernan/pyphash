#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Library Imports
import sys

# Global variables
FS_ENCODING = sys.getfilesystemencoding()


def _filename_bytes(filename):
    if isinstance(filename, bytes):
        filename_bytes = filename
    else:
        filename_bytes = filename.encode(FS_ENCODING)
    return filename_bytes
