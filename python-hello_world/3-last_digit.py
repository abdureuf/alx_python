import random

number = random.randint(-10000, 10000)
number_str = str(number)
last_digit_str = number_str[-1]
last_digit = int(last_digit_str)

if number >= 0:
    if last_digit > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
    elif last_digit < 6 and last_digit != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
    else:
        print("Last digit of {} is {} and is 0".format(number, last_digit))
else:
    if last_digit == 0:
        print("Last digit of {} is {} and is 0".format(number, last_digit))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, -last_digit))