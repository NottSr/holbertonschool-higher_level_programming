#!/usr/bin/python3
"""
Define method that checks the object
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: class to take a look in

    Returns: True if the object is an
    instance of a class that inherited
    (directly or indirectly) from the
    specified class
    """
    if isinstance(obj, a_class) & issubclass(a_class, obj.__class__) is False:
        return True
    return False
