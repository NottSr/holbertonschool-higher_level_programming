#!/usr/bin/python3
"""
Define method that returns obj dict
"""


def class_to_json(obj):
    """
    Args:
        obj: Instance of a Class

    Returns:
        Dictionary description
    """
    return obj.__dict__
