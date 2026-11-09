# This program finds all the divisors of a given positive integer.

num = input("Enter a number: ")

# checking if input is valid (only digits)
if num.isdigit():
    num = int(num)
    # checking if num is a positive number
    if num <= 0:
        print("Please enter a positive number.")
        exit()
else:
    print("Please enter a valid number.")
    exit()

divisors = []

for number in range(1, num + 1):
    if num % number == 0:
        divisors.append(number)

print(f"The divisors of {num} are: {divisors}")