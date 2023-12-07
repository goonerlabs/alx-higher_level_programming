#!/usr/bin/python3
"""utility function to convert python object to json string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object
    Args:
        my_obj: the object to convert
    Returns:
        the JSON representation of an object
    """
    return json.dumps(my_obj)
