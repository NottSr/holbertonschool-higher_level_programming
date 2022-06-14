#!/usr/bin/python3
"""
Define class
"""


class Base:
    """
    Class that will be the “base” of all
    other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Manage id attribute in all your future
        classes and to avoid duplicating the
        same code
        Args:
            id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
