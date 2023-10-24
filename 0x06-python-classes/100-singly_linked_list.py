#!/usr/bin/python3
"""A node & SinglyLinkedList classes"""


class Node:
    """
    A class that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Function that initializes a new Node instance.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Function that retrieves the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Function that sets the data of the node.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If the data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Function that retrieves the next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.

        Args:
            value (Node): The next node in the list.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.
    """

    def __init__(self):
        """
        Function that initializes a new SinglyLinkedList instance.
        """
        self.head = None

    def __repr__(self):
        """
        Function that returns a string representation of the list.
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Function that inserts a new Node
        into the correct sorted position in the list (increasing order).
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None and \
                    current_node.next_node.data < value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
