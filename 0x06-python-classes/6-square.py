#!/usr/bin/python3
"""Define a square class"""


class Square:
    """
    A simple class with the size/position attribute and error messages
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    """
    Returns the current square area
    """
    def area(self):
        return self.__size ** 2
    """
    Prints a '#' in a range of size x size
    Prints space based on positions provided
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
