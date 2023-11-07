#!/usr/bin/python3
"""
Define write_file
"""


def write_file(filename="", text=""):
    """
    Defining write_file
    function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    """
    with open(filename, "w+", encoding="utf-8") as file:
        file.write(text)
        file.seek(0)
        return len(file.read())
