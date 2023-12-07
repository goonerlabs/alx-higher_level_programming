#!/usr/bin/python3
"""utility function to deserialize from JSON file"""
import json


def load_from_json_file(filename):
    """loads a python object from a JSON file
    Args:
        filename (str): the source file
    Returns:
        the object that was read
    """

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
