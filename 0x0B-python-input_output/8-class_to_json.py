#!/usr/bin/python3
"""
Define class_to_json
"""


def class_to_json(obj):
    """
    defining class_to_json
    function that returns the dictionary description with 
    simple data structure (list, dictionary, string, integer and boolean) for 
    JSON serialization of an object:
    """
    return obj.__dict__
