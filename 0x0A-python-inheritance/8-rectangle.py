#!/usr/bin/python3
"""
Define subclass Rectangle using BaseGeometry
as parent class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass Rectangle with class BaseGeometry
    """
    def __init__(self, width, height):
        """
        Method that validates args and set them as
        private attributes
        Args:
            width: Rectangle width
            height: Rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
