#!/usr/bin/python3
"""Module for load_from_json_file function"""
import json


def load_from_json_file(filename):
    """function that creates an
    Object from a JSON file."""
    with open(filename, encoding='utf-8') as myfile:
        return json.load(myfile)
