#!/usr/bin/python3
"""
Define save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Defining save_to_json_file
    function that writes an Object to a text file,
    using a JSON representation:
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
