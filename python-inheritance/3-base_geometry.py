#!/usr/bin/python3
"""
no import
"""
class BaseGeometry:
    """
    BaseGeometry is an empty class.
    """
    @classmethod
    def __init_subclass__(cls):
        pass

    def __dir__(self):
        return sorted(set(dir(type(self))) | set(self.__dict__) | set(dir(BaseGeometry)))

    def __repr__(self):
        return "<{} object>".format(self.__class__.__name__)