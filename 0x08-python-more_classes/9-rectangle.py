#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle():
    """Defining of the class Rectangle
    Args:
        width: Optional by default 0
        height: Optional by default 0
    Raises:
        TypeError with msg 'width must be an integer'
        TypeError with msg 'height must be an integer'

        ValueError with msg 'width must be >= 0'
        ValueError with msg 'height must be >= 0'
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize Rectangle attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a message when a Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Width attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attribute getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """function that returns the rectangle
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def print(self):
        """prints a rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return
        for i in range(0, self.__height):
            [print(str(getattr(self, 'print_symbol')), end="")
                for j in range(0, self.__width)]
            if i < self.__height - 1:
                print()

    def __str__(self):
        """print a rectangle with the character #"""
        if self.__width != 0 and self.__height != 0:
            for i in range(0, self.__height):
                [print(str(getattr(self, 'print_symbol')), end="")
                    for j in range(0, self.__width)]
                if i < self.__height - 1:
                    print()
        return ""

    def __repr__(self):
        """repr returns a string representation of
            a rectangle
        """
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle determined by the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle object where both the width
        ,height are equal to the size
        """
        return Rectangle(size, size)
