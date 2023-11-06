#!/usr/bin/python3
"""
Define a Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defining rectangle
    """

    def __init__(self, width, height):
        """
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        super().__init__()

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
