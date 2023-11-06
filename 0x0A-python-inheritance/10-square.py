#!/usr/bin/python3
"""
This module defines a Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A representation of a square
    """

    def __init__(self, size):
        """
        Initializes a new Square instance
        Args:
            size (int): The size of the square's sides
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)

    def area(self):
        """
        Returns:
            The area of the square
        """
        return Rectangle.area(self)
