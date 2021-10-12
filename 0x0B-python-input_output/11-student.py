#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize student with first_name, last_name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        obj_dict = {}
        if type(attrs) == list:
            for element in attrs:
                if type(element) != str:
                    break
                if element in self.__dict__.keys():
                    obj_dict[element] = self.__dict__[element]
            else:
                return obj_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if not json:
            return
        self.__dict__ = json
