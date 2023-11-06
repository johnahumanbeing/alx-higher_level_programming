#!/usr/bin/python3
"""
Define a lookup(obj) function
"""


def lookup(obj):
    """
    Defining the lookup function
    Args:
        obj: a requirement

    Returns: a list of available attributes and
    methods of an object.
    """
    return dir(obj)
