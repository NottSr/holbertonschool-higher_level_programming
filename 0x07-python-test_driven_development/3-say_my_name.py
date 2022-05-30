#!/usr/bin/python3
"""
Module that divides all elements of a matrix.
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: First name
        last_name: Last name. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
