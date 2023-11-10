#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """Defining class Base

    Attributes:
        __nb_objects (int): Private class attribute to keep track of
        the number of instances created.
        id (int): Public instance attribute to store the id of each instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new instance of class Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
