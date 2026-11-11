# This program generates two lists of random integers and finds the common elements between them.

import random

a = [random.randint(1, 20) for _ in range(10)]
b = [random.randint(1, 20) for _ in range(15)]

common = []

for number in a:
    if number in b and number not in common:
        common.append(number)

print("List A:", a)
print("List B:", b)
print("Common elements:", common)
