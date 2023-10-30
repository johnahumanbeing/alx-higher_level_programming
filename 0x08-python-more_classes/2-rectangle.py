#!/usr/bin/python3
"""
Defining a class rectangle with two methods
area()
perimeter()
"""


class Rectangle():
    """
    This class represents a rectangle with a given width and height.
    The width and height must be positive integers.
    """

    def __init__(self, width=0, height=0):
        """
        Raises:
        ValueError: If width or height is negative.
        TypeError: If width or height is not an integer.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
        ValueError: If width is negative.
        TypeError: If width is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be a positive integer.")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raises:
        ValueError: If height is negative.
        TypeError: If height is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be a positive integer.")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
