#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    sc = 0

    def __init__(self, name, number=4):
        self.__name = name
        self.num = number
        self.is_team_red = (self.num % 2) == 0

    def win(self):
        self.sc += 1

    def lose(self):
        self.sc -= 1

    def __str__(self):
        return "[MyClass]{}-{:d}=>{:d}".format(self.__name, self.num, self.sc)
