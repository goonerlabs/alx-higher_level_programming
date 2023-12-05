#!/usr/bin/python3
"""checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """returns true if obj is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
    ARGS:
        obj: object
        a_class: class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
