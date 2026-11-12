# This program checks if a given number is prime or not using a function.

def is_prime(number):
    # Check if a number is prime.
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


while True:
    try:
        number = int(input("Enter a number: "))

        # Check if the number is prime and print the result.
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

        break

    except ValueError:
        print("Please enter a valid whole number.")