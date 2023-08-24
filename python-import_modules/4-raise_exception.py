#!/usr/bin/env python3
def raise_exception():
    raise 

try:
    raise_exception()
except TypeError as te:
    pass
finally:
    print("Exception has been raised")