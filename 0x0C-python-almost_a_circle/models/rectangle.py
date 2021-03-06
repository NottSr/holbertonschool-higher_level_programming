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

        self.int_checker(width, 'width')
        self.int_checker(height, 'height')
        self.int_checker(x, 'x')
        self.int_checker(y, 'y')

        self.__y = y
        self.__x = x
        self.__height = height
        self.__width = width

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

    @height.setter
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

    @x.setter
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

    @y.setter
    def y(self, val):
        """
        ...
        """
        self.int_checker(val, 'y')
        self.__y = val

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

    def __str__(self):
        """
        Args:
            form (str): form created. Defaults to 'Rectangle'.

        Returns a personalized message
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
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
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
