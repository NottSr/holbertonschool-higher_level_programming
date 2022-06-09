#!/usr/bin/python3
"""
Define method that appends a line in a file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: name of file. Defaults to "".
        text: text to attach. Defaults to "".
    """
    with open(filename, 'a', encoding='utf-8') as rf:
        return rf.write(text)
