#!/usr/bin/python3
"""
Defines a Square class that
inherits from Rectangle (9-rectangle.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square
    Args: size
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the square description.
        """
        return "[Square]" + Rectangle.__str__(self)[11:]

    def area(self):
        """
        Returns the area of the square.
        """
        return Rectangle.area(self)
