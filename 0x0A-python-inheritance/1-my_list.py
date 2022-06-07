#!/usr/bin/python3
"""
Define subclass
"""


class MyList(list):
    """
    Method that prints the list, but sorted
    """
    def print_sorted(self):
        """
        Returns: list printed
        """
        return (print(sorted(self)))
