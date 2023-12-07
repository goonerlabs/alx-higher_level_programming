#!/usr/bin/python3
"""utility function that writes a serialized object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation
    Args:
        my_obj: the object to convert
        filename: the file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
