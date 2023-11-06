#!/usr/bin/python3
"""
Define class MyInt
"""


class MyInt(int):
    """
    Defining MyInt
    it inherits from int
    """
    def __eq__(self, other):
        """
        used to compare two objects
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        defines the equality comparison
        """
        return int.__eq__(self, other)
