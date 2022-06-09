#!/usr/bin/python3
"""
Define module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Module that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, 'w') as wf:
        wf.write(json.dumps(my_obj))
