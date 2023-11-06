#!/usr/bin/python3
"""
Define a function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Defining is_same_class
    function that returns True if the object is an
    exactly an instance of the specified class else
    False
    """
    return type(obj) is a_class
