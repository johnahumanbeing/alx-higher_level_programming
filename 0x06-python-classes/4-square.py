#!/usr/bin/python3
'''This module defines the Square class.'''


class Square:
    '''
    A class that defines a square.

    Attributes:
    __size (int): The size of the square (private).
    '''

    def __init__(self, size=0):
        '''
        Function that initializes a new instance of the Square class.

        Args:
        size (int): The size of the square (default 0).

        Raises:
        TypeError: if the size is not an int
        ValueError: if the size is less than zero.
        '''
        self.size = size

    @property
    def size(self):
        '''
        Function that gets the size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Set the size of the square.

        Args:
        value (int): The new size of the square.

        Raises:
        TypeError: If the value is not an int.
        ValueError: If the value is less than zero.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Function that returns the area of the square
        '''
        return self.__size ** 2
