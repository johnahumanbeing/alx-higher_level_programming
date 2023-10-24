#!/usr/bin/python3
"""A module that defines a class square"""


class Square:
    """
    This class represents a square and provides methods to manipulate and
    calculate properties of the square.
    """

    def __init__(self, size=0):
        """
        Function that itializes a new instance
        of the Square class with the given size.
        """
        self.size = size

    @property
    def size(self):
        """
        Functoin that retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If the size is not a number (float or integer).
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Function that calculates the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Function that checks if two squares are equal based on their areas.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Function that checks if two squares are not equal based on their areas.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compares if one square is greater than another based on their areas.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if one square is greater than or
        equal to another based on their areas.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compares if one square is less than another based on their areas.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares if one square is less than or equal to
        another based on their areas.
        """
        return self.area() <= other.area()
