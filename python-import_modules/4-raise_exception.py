#!/usr/bin/python3

def raise_exception():
    raise TypeError

def handle_exception():
    try:
        raise_exception()
    except TypeError as te:
        return "Exception has been raised"