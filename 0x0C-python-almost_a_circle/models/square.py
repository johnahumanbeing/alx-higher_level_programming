#!/usr/bin/python3
"""Define class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining class Square

    it is inherited from Rectangle
    Attributes:
        id (int): the identifier of the square
        size (int): the size of the square
        x (int): x-cooredinate for the square
        y (int): y-cooredinate of the square
    """

    def __ibit__(self, size, x=0, y=0, id=None):
        """Initializes instance of the class square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string rep of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
