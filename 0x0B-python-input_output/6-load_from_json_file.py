#!/usr/bin/python3
"""
Define module
"""


import json


def load_from_json_file(filename):
    """
    Module that creates an Object from a “JSON file”
    """
    with open(filename, mode='r', encoding='utf-8') as rf:
        return json.load(rf)
