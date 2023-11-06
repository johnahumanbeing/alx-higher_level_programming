#!/usr/bin/python3
"""
Define a class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defining Rectangle
    it inherits from the class BaseGeomerty
    """
    def __init__(self, width, height):
        """
        initializing with the Rectangle attributes
        Args:
            width (int): the rectangles width
            height (int): the rectangles height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
