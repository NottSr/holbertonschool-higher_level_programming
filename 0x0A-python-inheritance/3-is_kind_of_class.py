#!/usr/bin/python3
"""
Define method
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: class to take a look in

    Returns: True if the object is an instance
    of, or if the object is an instance of a
    class that inherited from, the specified class
    """
    return (isinstance(obj, a_class))
