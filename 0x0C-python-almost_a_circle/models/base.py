#!/usr/bin/python3
"""
Define class
"""


import json
from os import path
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries: list of dictionaries

        Returns: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Args:
            list_objs: list of instances who inherits of Base

        Returns JSON string representation of list_objs to a file
        """
        file_name = cls.__name__ + '.json'
        elm_dict = []
        if list_objs is None:
            with open(file_name, 'w', encoding='utf-8') as f:
                return f.write(cls.to_json_string(None))

        for elm in list_objs:
            elm_dict.append(elm.to_dictionary())

        with open(file_name, 'w', encoding='utf-8') as f:
            return f.write(cls.to_json_string(elm_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string is a string representing a list of dictionaries

        Returns the list represented by json_string
        """
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns updated instance
        """
        if cls.__name__ == 'Rectangle':
            Inst = cls(89, 89)
        if cls.__name__ == 'Square':
            Inst = cls(89)
        Inst.update(**dictionary)
        return Inst

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        file_name = cls.__name__ + '.json'
        insts = []

        if path.exists(file_name) is False:
            return []

        with open(file_name, 'r', encoding='utf-8') as f:
            list_objs = cls.from_json_string(f.read())
            for elm in list_objs:
                insts.append(cls.create(**elm))
            return insts

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Args:
            list_objs: list of instances who inherits of Base

        Returns CSV string representation of list_objs to a file
        """
        file_name = cls.__name__ + '.csv'
        elm_dict = []
        if list_objs is None:
            with open(file_name, 'w', encoding='utf-8') as f:
                return f.write(cls.to_json_string(None))

        for elm in list_objs:
            elm_dict.append(elm.to_dictionary())

        with open(file_name, 'w', encoding='utf-8') as f:
            return f.write(cls.to_json_string(elm_dict))

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances csv
        """
        file_name = cls.__name__ + '.csv'
        insts = []

        if path.exists(file_name) is False:
            return []

        with open(file_name, 'r', encoding='utf-8') as f:
            list_objs = cls.from_json_string(f.read())
            for elm in list_objs:
                insts.append(cls.create(**elm))
            return insts
