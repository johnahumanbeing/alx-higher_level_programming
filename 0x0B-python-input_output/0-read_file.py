#!/usr/bin/python3
"""
Define read_file
"""


def read_file(filename=""):
    """
    Defining read_file
    function that reads a text file (UTF8)
    and prints it to stdout:
    """
    with open(filename) as file:
        for line in file:
            print(line, end="")
