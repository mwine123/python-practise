# This program finds the common elements between two lists and returns a new list with those elements.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for num in a:
    if num in b:
        c.append(num)

print(c)
