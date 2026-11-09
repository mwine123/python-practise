# This program demonstrates basic list operations, including filtering elements based on conditions and user input.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(f"{i}")

b = []
for i in a:
    if i < 5:
        b.append(i)

print(b)

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

c = []

for i in a:
    if i < num:
        c.append(i)

print(c)
