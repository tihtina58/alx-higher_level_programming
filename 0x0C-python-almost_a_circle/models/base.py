#!/usr/bin/python3
"""Module for Base class."""
import json


class Base:
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing object with id."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or (type(list_dictionaries) == list and
                                         len(list_dictionaries) == 0):
            return '"[]"'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            other_list = [r.to_dictionary() for r in list_objs]
        else:
            other_list = []
        json_str = cls.to_json_string(other_list)
        with open(filename, 'w') as my_file:
            my_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        dic = None
        with open(cls.__name__ + ".json") as my_file:
            dic = my_file.read()
        if dic is None:
            return []
        list1 = cls.from_json_string(dic)
        list1 = [cls.create(**dic) for dic in list1]
        return list1

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV."""
        filename = cls.__name__ + ".csv"
        if list_objs is not None:
            other_list = [r.to_dictionary() for r in list_objs]
        else:
            other_list = []
        json_str = cls.to_json_string(other_list)
        with open(filename, 'w') as my_file:
            my_file.write(json_str)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV."""
        dic = None
        with open(cls.__name__ + ".csv") as my_file:
            dic = my_file.read()
        if dic is None:
            return []
        list1 = cls.from_json_string(dic)
        list1 = [cls.create(**dic) for dic in list1]
        return list1
