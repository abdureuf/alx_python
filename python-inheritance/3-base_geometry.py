#!/usr/bin/python3
"""
no import
"""
class BaseGeometry:
    """
    BaseGeometry is a class with an area method that raises an exception.
    """
    def __dir__(self):
        """
        Customizes the behavior of dir() method.
        """
        attrs = set(dir(type(self))) | set(self.__dict__) | set(dir(BaseGeometry))
        attrs = attrs - {'__init_subclass__'}  # Exclude '__init_subclass__' method
        return sorted(attrs)

    # def area(self):
    #     """
    #     Raises an exception when called.
    #     """
    #     raise Exception("area() is not implemented")