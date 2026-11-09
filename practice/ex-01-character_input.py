# This program asks for the user's name and age, calculates the year they will turn 100, and repeats a message a specified number of times.

name = input("What is your name? ")
# checking if input is valid (only letters)
if not name.isalpha():
    print("Please enter a valid name.")
    exit()

age = input("How old are you? ")
# checking if input is valid (only digits)
if age.isdigit():
    age = int(age)
    # checking if age is a positive number and realistic
    if age <= 0:
        print("Please enter a positive age.")
        exit()
    elif age > 100:
        print("Please enter a realistic age.")
        exit()
else:
    print("Please enter a valid age.")
    exit()

year = 2026 + ( 100 - age)

rep = input("How many times do you want to repeat the message? ")
# checking if input is valid (only digits)
if rep.isdigit():
    rep = int(rep)
    # checking if rep is a positive number
    if rep <= 0:
        print("Please enter a positive number.")
        exit()
else:
    print("Please enter a valid number.")
    exit()

for _ in range(rep):
    print(f"{name}, you will turn 100 years old in the year {year}.")
