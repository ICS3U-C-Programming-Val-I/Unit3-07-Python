#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 30, 2023
# This program asks the user for their age
# and lets them know if they can date their grandchild.


def main():
    userAgeStr = input("how old are you??  \n")
    try:
        userAgeStr = input("Enter your age: ")
        userAgeFlt = float(userAgeStr)

        if userAgeFlt < 1 or userAgeFlt > 119:
            print("Please enter your real age.")
        elif userAgeFlt > 40:
            print("You are too old to date my grandchild.")
        elif userAgeFlt < 25:
            print("You are too young to date my grandchild.")
        else:
            print("You can date my grandchild.")
    except ValueError:
        print("Please enter a number.")


if __name__ == "__main__":
    main()
