#!/usr/bin/python3
"""
Define method
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: class to take a look in

    Returns: True if the object is exactly an
    instance of the specified class
    """
    return (issubclass(a_class, obj.__class__))
