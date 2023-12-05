#!/usr/bin/python3
"""checks if object is an instance of, or if the object is an
instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """returns true if obj is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
    ARGS:
        obj: object
        a_class: class
    """
    return isinstance(obj, a_class)
