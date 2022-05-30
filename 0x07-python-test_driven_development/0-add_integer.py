#!/usr/bin/python3
"""
Module that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Args:
        a: Number a
        b: Number b. Defaults to 98.

    Raises:
        TypeError: When a is not a number
        TypeError: When b is not a number

    Returns:
        int: sum a + b
    """

    if not type(a) in (int, float):
        raise TypeError("a must be an integer")
    if not type(b) in (int, float):
        raise TypeError("b must be an integer")

    return int(a + b)
