#!/usr/bin/python3
"""
Define append_write
"""


def append_write(filename="", text=""):
    """
    Defining append_write
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
    """
    with open(filename, "a+", encoding="utf-8") as file:
        file.write(text)
        file.seek(0, 2)
        return file.tell()
