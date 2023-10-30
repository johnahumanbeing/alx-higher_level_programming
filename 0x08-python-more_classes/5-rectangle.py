#!/usr/bin/python3
"""Class defining a rectangle"""


class Rectangle:
    """Definition of a class rectangle"""

    def __init__(self, width=0, height=0):
        """intitializing rectangle width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Attribute for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Attribute for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.height == 0:
            perimeter = 0
        elif self.width == 0:
            perimeter = 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def __str__(self):
        """prints a rectangle with the  character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance of a Rectangle """
        print("Bye rectangle...")
