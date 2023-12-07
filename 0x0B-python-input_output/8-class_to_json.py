#!/usr/bin/python3
"""a function that returns the class __dict__ representation of an object
"""


def class_to_json(obj):
    """returns the class __dict__ representation of an object
    Args:
        obj: the object to convert
    Returns:
        the class __dict__ representation of an object
    """
    return obj.__dict__
