#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = str(number)
last_number = int(number2[-1])

if (number >= 0):
    if (last_number > 5):
        print("Last digit of {} is {} and is greater than 5".format(
            number2, last_number))
    elif (last_number < 6 and last_number != 0):
        print("Last digit of {} is {} and is less than 6 and not 0".format(
            number2, last_number))
    else:
        print("Last digit of {} is {} and is 0".format(number2, last_number))
else:

    if (last_number == 0):
        print("Last digit of {} is {} and is 0".format(number2, last_number))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(
            number2, -last_number))
