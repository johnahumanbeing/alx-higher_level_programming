#!/usr/bin/python3
""" module that defines a class square"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Function that initializes a new Square instance.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Function that retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Function that sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Function that retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Function that sets the position of the square.
        """
        if not isinstance(value, tuple) or \
            len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Function that calculates the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
