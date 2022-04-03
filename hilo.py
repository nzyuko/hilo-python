import random


def userinput():
    try:
        # convert input to integer
        number = int(input("Enter your number and hit Enter: "))
        return number
    except ValueError:
        try:
            # convert it to a float
            number = float(input("Enter your number and hit Enter: "))
            return number
        except ValueError:
            # recall function again
            print("Please input a number")
            userinput()

