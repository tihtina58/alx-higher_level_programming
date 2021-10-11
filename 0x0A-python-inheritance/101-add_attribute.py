#!/usr/bin/python3
"""sdfsdff"""


def add_attribute(a, attr, value):
    """"dsfsd"""
    if '__dict__' not in dir(a):
        raise TypeError("can't add new attribute")
    else:
        setattr(a, attr, value)
