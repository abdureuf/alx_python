#!/usr/bin/python3
"""
no import
"""
def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class