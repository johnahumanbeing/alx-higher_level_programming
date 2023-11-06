#!/usr/bin/python3
"""
Define a function is_kind_of_clss
"""


def is_kind_of_class(obj, a_class):
    """
    Defining is_kind_of_class;

    Returns True if the obj is an instance of, or if
    the obj is an instance of the specified class;
    else False.
    """
    return isinstance(obj, a_class)
