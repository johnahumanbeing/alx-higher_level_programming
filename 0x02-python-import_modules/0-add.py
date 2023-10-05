#!/usr/bin/python3
# importing the add function from the add_0.py file
from add_0 import add
if __name__ == "__main__":
    # the values 'a' and 'b'
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
