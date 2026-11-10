# This program creates a list of the squares of numbers from 1 to 10 and then filters out the even squares into a new list.

a =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [num for num in a if num % 2 == 0]
print(b)
