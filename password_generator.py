"""simple password generator for terminal"""

import random

print("Welcome to your password generator!\n")

# characters the generator will pick from randomly
letters = "abcdefghijklmnopqrstuvwxyz"
cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()_.,?"
numbers = "0123456789"
space = " "


# variable for the amount of passwords the user wants generated at one time
number = input("Input amount of passwords you want generated: ")
number = int(number)

# number of characters the user wants to password to be
length = input("Input number of characters you would like your passwords to be: ")
length = int(length)

# special password requirements
requirement_1 = input("Would you like capital letters in your passwords, type 'y' for yes and 'n' for no: ")
requirement_1 = requirement_1.lower()
requirement_2 = input("Would you like numbers in your passwords, type 'y' for yes and 'n' for no: ")
requirement_2 = requirement_2.lower()
requirement_3 = input("Would you like special characters in your passwords, type 'y' for yes and 'n' for no: ")
requirement_3 = requirement_3.lower()
requirement_4 = input("Would you like spaces in your passwords, type 'y' for yes and 'n' for no: ")
requirement_4 = requirement_4.lower()

# logic to determine password requirements based on user's inputs
chars = letters
if requirement_1 == "y":
    chars += cap_letters
if requirement_2 == "y":
    chars += special_characters
if requirement_3 == "y":
    chars += numbers
if requirement_4 == "y":
    chars += space

# logic to calculate number of permutations the passwords have
exponent = len(chars)
permutations = length ** exponent

print(f"\nHere are your passwords, there are {permutations} possible permutations in each password: ")

for password in range(number):
    PWD = ""

    for character in range(length):
        PWD += random.choice(chars)

    print(PWD)
