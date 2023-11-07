#!/usr/bin/python3
"""
Define class student
"""


class Student():
    """
    Defining class student

    Methods:
        to_json: retrieves a dictionary representation of
        a Student instance
        reload_from_json: replaces all attributes of the Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in
                    attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
