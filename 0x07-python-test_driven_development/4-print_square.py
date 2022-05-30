#!/usr/bin/python3
"""
Module that prints a square based on a size
"""


def print_square(size):
    """
    Args:
        size: Size of the square

    Raises:
        TypeError: Size must be an integer
        ValueError: Size must be >= 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
