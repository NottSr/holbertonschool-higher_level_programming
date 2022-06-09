#!/usr/bin/python3
"""
Define method that writes in a file
"""


def write_file(filename="", text=""):
    """
    Args:
        filename: name of file. Defaults to "".
        text: text to attach. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as rf:
        return rf.write(text)
