#!/usr/bin/python3
"""
Define class method
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name='', last_name='', age=0):
        """
        Method that assigns public attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            Dictionary representation of a Student instance
        """
        return self.__dict__
