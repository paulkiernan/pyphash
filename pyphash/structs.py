#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" phashlib structs
"""

# Standard Library Imports
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import c_byte
from ctypes import c_char_p
from ctypes import POINTER
from ctypes import Structure


class TextHashPoint(Structure):
    """
    Textual Hash Point

    @field hash: hash
    @field index: position of hash in the original file
    """

    _fields_ = [
        ('hash', c_ulong),
        ('index', c_uint),
        ('length', c_int),
    ]

    def __str__(self):
        return (
            "TextHashPoint("
                "hash={hash}, "
                "index={index}, "
                "length={length}"
            ")"
        ).format(hash=self.hash, index=self.index, length=self.length)


class TextMatch(Structure):
    """
    Textual Hash Point

    @field hash: hash
    @field index: position of hash in the original file
    """

    _fields_ = [
        ('first_index', c_uint),
        ('second_index', c_uint),
        ('length', c_uint),
        ('matching_words', c_int),
    ]

    def __str__(self):
        return (
            "TextMatch("
                "first_index={first_index}, "
                "second_index={second_index}, "
                "length={length}, "
                "matching_words={matching_words}"
            ")"
        ).format(
            first_index=self.first_index,
            second_index=self.second_index,
            length=self.length,
            matching_words=self.matching_words
        )


class Digest(Structure):
    """
    Digest Info

    @field id: str, hash id
    @field coeffs: int, digest coefficient array
    @field size: int, size of the coefficient array
    """

    _fields_ = [
        ('id', POINTER(c_char_p)),
        ('coeffs', POINTER(c_byte)),
        ('size', c_int),
    ]

    def __str__(self):
        return (
            "Digest("
                "id={id}, "
                "coeffs={coeffs}, "
                "size={size}"
            ")"
        ).format(id=self.id, coeffs=self.coeffs, size=self.size)


