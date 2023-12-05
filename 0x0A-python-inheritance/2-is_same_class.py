#!/usr/bin/python3
"""a function to get the type of an object"""


def is_same_class(obj, a_class):
    """returns true if obj is of type a_class
    otherwise return false
    ARGS:
        obj: object
        a_class: class
    """
    return type(obj) is a_class
