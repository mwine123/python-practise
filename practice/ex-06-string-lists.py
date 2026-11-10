# This program checks if a word is a palindrome (a word that reads the same backward as forward).

list = str(input("Enter a word: "))

# checking if input is valid (only letters)
if not list.isalpha():
    print("Please enter a valid word (only letters).")
else:
    list = list.lower()

rvs = list[::-1]
print(rvs)
if list == rvs:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
