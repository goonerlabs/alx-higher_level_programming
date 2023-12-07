"""utility function to deserialize a json string"""
import json


def from_json_string(my_str):
    """returns the json representation of an object
    Args:
        my_obj: the object to convert
    Returns:
        the JSON representation of an object
    """
    return json.loads(my_str)
