#!/usr/bin/python3
"""
Define module
"""


import json


def to_json_string(my_obj):
    """
    Returns:
        json representation of the object
    """
    return json.dumps(my_obj)
