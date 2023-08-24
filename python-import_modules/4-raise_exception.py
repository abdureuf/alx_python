#!/usr/bin/env python3
def raise_exception():
    raise 
try:
    raise_exception()
except TypeError as te:
    print("Exception has been raised")