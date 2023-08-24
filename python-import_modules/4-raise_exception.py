#!/usr/bin/env python3
def raise_exception():
    raise TypeError("Exception raised")

try:
    raise_exception()
except TypeError as te:
    print(te)