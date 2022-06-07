#!/usr/bin/python3
"""
Define subclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Subclass square with parent Rectangle
    """
    def __init__(self, size):
        """
        Method that validates args and set them as
        private attributes
        Args:
            size: Square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
