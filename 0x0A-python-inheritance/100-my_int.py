#!/usr/bin/python3
"""
Define class
"""


class MyInt(int):
    """
    Class that inverts the == and != operators
    """
    def __eq__(self, __x: object) -> bool:
        return super().__ne__(__x)

    def __ne__(self, __x: object) -> bool:
        return super().__eq__(__x)
