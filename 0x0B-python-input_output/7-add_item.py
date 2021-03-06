#!/usr/bin/python3
"""Module for script: Load, add, save."""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    l = load_from_json_file("add_item.json")
except:
    l = []

for i in range(1, len(argv)):
    l.append(argv[i])

save_to_json_file(l, "add_item.json")
