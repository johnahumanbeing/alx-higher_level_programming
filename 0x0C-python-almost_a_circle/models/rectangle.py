#!/usr/bin/python3
"""Define class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defining class Rectangle

    Attributes:
        width: rectanles width (requirement)
        height: rectangles height (requirement)
        x (int): x-coordinate of rectangle (default 0)
        y (int): y-coordinate of rectangle (default 0)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new instance of class rectangle

        Args:
            width (int): rectangles width
            height (int): rectangles height
            x (int): x-coordinate of rectangle (default 0)
            y (int): y-coordinate of rectangle (default 0)
            id (int): optional to assign
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width atrribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height atribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.
        """
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Returns: int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Args: value (int): The new value for the y-coordinate of the rectangle.
        """
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle with the character (#)
        """
        for j in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string rep of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
