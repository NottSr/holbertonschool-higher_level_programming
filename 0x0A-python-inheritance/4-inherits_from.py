#!/usr/bin/python3
"""
Define method that checks the object
"""


def inherits_from(oj, a_class):
    """
    Returns: True if the object is an
    instance of a class that inherited
    (directly or indirectly) from the
    specified class
    """
    if isinstance(oj, a_class) and issubclass(a_class, oj.__class__) is False:
        return True
    return False
