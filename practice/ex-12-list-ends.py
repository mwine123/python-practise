# This function takes a list of numbers and returns a new list containing the first and last elements of the input list.

def list_ends(numbers):
    return [numbers[0], numbers[-1]]


a = [5, 10, 15, 20, 25]

result = list_ends(a)

print(result)