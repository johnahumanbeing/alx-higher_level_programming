#!/usr/bin/python3
"""Define to_json_string"""
import json


def to_json_string(my_obj):
    """Defining to_json_string
    returns the JSON representation of an object (string):
    """
    return json.dumps(my_obj)
