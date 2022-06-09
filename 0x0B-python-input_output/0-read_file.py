#!/usr/bin/python3
"""
Define method that reads a file
"""


def read_file(filename=""):
    """
    Args:
        filename: name of file. Defaults to "".
    """
    with open(filename, encoding='utf-8') as rf:
        for line in rf:
            print(line, end='')
