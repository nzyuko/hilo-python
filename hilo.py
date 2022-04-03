import random


def user_range():
    try:
        # calculate range for integer input
        floor = int(input("Input the floor of your range(Minimum guessable number: )"))
        ceiling = int(input("Input the ceiling of your range(Maximum guessable number: )"))
        return ceiling - floor
    except ValueError:
        try:
            # convert it to a float
            number = float(input("Enter your number and hit Enter: "))
            return number
        except ValueError:
            # recall function again
            print("Please input a number")
            userinput()

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

def pick_random():
