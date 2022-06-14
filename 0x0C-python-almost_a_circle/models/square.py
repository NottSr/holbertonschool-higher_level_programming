#!/usr/bin/python3
"""
Define class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines square values
    """
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        return super().__str__('Square')

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            my_dict = [
                "id",
                "size",
                "x",
                "y"
            ]
            for i in range(len(args)):
                setattr(self, my_dict[i], args[i])

    def to_dictionary(self):
        return vars(self)
