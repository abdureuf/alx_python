#!/usr/bin/env python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
        return result
    
    finally:  
        print("Inside result: {}".format(result))
        return result

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))