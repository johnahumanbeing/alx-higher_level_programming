#!/usr/bin/python3
'''This is a class square that defines a square by size validation'''


class Square:
    '''
    Attributes:
    __size (int): The size of square (private).
    '''

    def __init__(self, size=0):
        '''
        Function to initialize a new instance of a square class.

        args:
        size (int): The size of square (default 0).

        Raises:
        TypeError: if size is not an int.
        ValueError: if size is less than zero.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
