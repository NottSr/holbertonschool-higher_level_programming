#!/usr/bin/python3
"""
Define class
"""


import json


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
            list_objs: _description_

        Returns:
            _type_: _description_
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
