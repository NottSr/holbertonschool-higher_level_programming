#!/usr/bin/python3
"""
Define class
"""


from models.base import Base


class Rectangle(Base):
    """
    Class that defines rectangle values
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width: Rectangle width
            height: Rectangle height
            x. Defaults to 0.
            y. Defaults to 0.
            id. Defaults to None.
        """

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """
        Return the area
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Method that prints the form
        """
        if self.__y > 0:
            for i in range(self.__y):
                print()

        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end='')

            for j in range(self.__width):
                print('#', end='')

            print()

    def update(self, *args, **kwargs):
        """
        Method that update values
        """
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            my_dict = [
                "id",
                "width",
                "height",
                "x",
                "y"
            ]
            for i in range(len(args)):
                setattr(self, my_dict[i], args[i])

    def __str__(self, form='Rectangle'):
        """
        Args:
            form (str): form created. Defaults to 'Rectangle'.

        Returns a personalized message
        """
        if form == 'Square':
            return '[{}] ({:d}) {:d}/{:d} - {:d}'.format(
                form, self.id, self.__x, self.__y, self.__width
                )

        return '[{}] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            form, self.id, self.__x, self.__y, self.__width, self.__height
        )

    @staticmethod
    def int_checker(val, meth):
        """
        Args:
            val: value
            meth: Str representation of method to update

        Raises:
            TypeError: must be an integer
            ValueError: the width or height must be > 0
            ValueError: the x or y must be >= 0
        """
        if type(val) is not int:
            raise TypeError(f'{meth} must be an integer')

        if val <= 0 and meth in ('width', 'height'):
            raise ValueError(f'{meth} must be > 0')

        if val < 0 and meth in ('x', 'y'):
            raise ValueError(f'{meth} must be >= 0')

    def to_dictionary(self):
        """
        Return class dictionary
        """
        return vars(self)

    @property
    def width(self):
        """
        ...
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        ...
        """
        self.int_checker(val, 'width')
        self.__width = val

    @property
    def height(self):
        """
        ...
        """
        return self.__height

    @width.setter
    def height(self, val):
        """
        ...
        """
        self.int_checker(val, 'height')
        self.__height = val

    @property
    def x(self):
        """
        ...
        """
        return self.__x

    @width.setter
    def x(self, val):
        """
        ...
        """
        self.int_checker(val, 'x')
        self.__x = val

    @property
    def y(self):
        """
        ...
        """
        return self.__y

    @width.setter
    def y(self, val):
        """
        ...
        """
        self.int_checker(val, 'y')
        self.__y = val
