#!/usr/bin/python3
"""Define from_json_string"""
import json


def from_json_string(my_str):
    """Defining from_json_string
    returns an object (Python data structure)
    represented by a JSON string:
    """
    return json.loads(my_str)
