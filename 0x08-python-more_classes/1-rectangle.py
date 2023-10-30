#!/usr/bin/python3
"""Defining a  class rectangle"""


class Rectangle():
    """Defining the class rectangle

    Args:
        width:
        height:

    Raises:
        TypeError when msg is 'width must be an integer'
        ValueError when msg is 'width must be >= 0'

        TypeError when msg is 'height must be an integer'
        ValueError when msg 'height must be >= 0'
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
