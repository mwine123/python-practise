# This program generates the Fibonacci sequence up to a specified number of terms.

def fibonacci(n):
    sequence = [1, 1]

    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]


number = int(input("How many Fibonacci numbers do you want? "))

print(fibonacci(number))