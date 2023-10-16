#!/usr/bin/python3
"""
no import
"""
class BaseGeometry:
    """
    BaseGeometry is an empty class.
    """
    def __dir__(self):
        """
        Customizes the behavior of dir() method.
        """
        attrs = set(dir(type(self))) | set(self.__dict__) | set(dir(BaseGeometry))
        attrs = attrs - {'__init_subclass__'}  # Exclude '__init_subclass__' method
        return sorted(attrs)