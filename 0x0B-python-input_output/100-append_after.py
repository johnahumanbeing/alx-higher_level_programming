#!/usr/bin/python3
"""Define append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Defining append_after function
    inserts a line of text to a file, after each line containing
    a specific string
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
