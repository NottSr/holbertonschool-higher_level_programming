#!/usr/bin/python3
"""Define a square class"""


class Square:
    """A simple class with the size attribute and error messages"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
