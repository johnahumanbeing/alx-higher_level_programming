#!/usr/bin/python3
class Square:
    '''
    A class that defines a aquare
    '''

    def __init__(self, size=0):
        '''
        Function that initializes a new instance of a Square class.

        args:
        size (int): The size of the square (default 0).

        Raises:
        TypeError: if the size is not an int.
        ValueError: if the size is less than zero.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        calculates area of the square.

        Returns:
        int: the area of the square.
        '''
        return self.__size ** 2
