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

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of the class square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a representation of the square"""
        return "[Square] (" + str(self.id) + ")" + str(self.x) + "/" \
            + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    def update(self, *args, **kwargs):
        """
        Args:
            *args: list of non-keyworded arguments
            **kwargs: Dictionary for the keyword arguments
        """
        if args is not None and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        attrs = ["id", "size", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}
