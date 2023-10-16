#!/usr/bin/python3
"""
no import
"""
class BaseGeometry:
    """
    BaseGeometry is an empty class.
    """
    def __init_subclass__(cls):
        raise NotImplementedError
    # pass