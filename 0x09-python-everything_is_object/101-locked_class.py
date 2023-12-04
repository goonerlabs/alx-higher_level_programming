#!/usr/bin/python3
""" creates a locked class """


class LockedClass:
    """ prevents the user from instantiating
    attributes other than first_name """
    __slots__ = ('first_name',)
