#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        text: Text provided

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text_line = ""
    for i in range(len(text)):
        text_line += text[i]
        if text[i] in (".", "?", ":"):
            text_line += "\n"
            print(text_line.strip())
            print()
            text_line = ""
    print(text_line.strip(), end='')
