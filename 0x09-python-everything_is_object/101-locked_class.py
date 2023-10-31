#!/usr/bin/python3
"""
Define a LockedClass
"""


class LockedClass:
    """
    Defining of LockedClass
        a class that prevent the user from creating
        new instance attributes, except if the new
        instance attribute is called first_name.
    """
    __slots__ = ["first_name"]
