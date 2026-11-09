# This program checks if a number is odd or even, and also checks divisibility by 4 and another number.

number = input("Enter a number: ")

if number.isdigit():
    number = int(number)
    if number <= 0:
        print("Please enter a positive number.")
        exit()
else:
    print("Please enter a valid number.")
    exit()

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

if number % 4 == 0:
    print(f"{number} is divisible by 4.")
else:
    print(f"{number} is not divisible by 4.")

num = input("Enter another number: ")

if num.isdigit():
    num = int(num)
    if num <= 0:
        print("Please enter a positive number.")
        exit()
else:
    print("Please enter a valid number.")
    exit()

check = input("Enter a third number: ")

if check.isdigit():
    check = int(check)
    if check <= 0:
        print("Please enter a positive number.")
        exit()
else:
    print("Please enter a valid number.")
    exit()

if num % check == 0:
    print(f"{num} is divisible by {check}.")
else:
    print(f"{num} is not divisible by {check}.")
