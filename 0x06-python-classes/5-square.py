#!/usr/bin/python3
'''Module that defines a class Square'''


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square using the '#' character.
    """

    def __init__(self, size=0):
        """
        Function that initializes a new instance of the Square class.
        """
        self.size = size

    @property
    def size(self):
        """
        Function that gets the size of the square
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Function that sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Function that calculates the area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Function that prints the square using the character "#'.
        If the size is 0, it prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
