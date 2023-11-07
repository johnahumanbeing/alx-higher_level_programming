#!/usr/bin/python3
"""Define load_from_json_file"""
import json


def load_from_json_file(filename):
    """Defining load_from_json_file
    function that creates an Object from a “JSON file”:
"""
    with open(filename, "r") as file:
        json_str = file.read()
        obj = json.loads(json_str)
        return obj
