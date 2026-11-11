# This is a simple number guessing game where the player has to guess a randomly generated number between 1 and 9. The player can exit the game at any time by typing 'exit'. The program provides feedback on whether the guess is too low, too high, or correct, and counts the number of valid attempts made by the player.

import random

rd = random.randint(1, 9)
guess = 0
c = 0

while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9 (or type 'exit'): ")

    # Allow the player to quit the game.
    if guess.lower() == "exit":
        print("Game exited.")
        break

    # Check that the input is a number before converting it to an integer.
    if not guess.isdigit():
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    guess = int(guess)

    # Check that the number is within the allowed range.
    if guess < 1 or guess > 9:
        print("Invalid guess. Please enter a number between 1 and 9.")
        continue

    # Only count valid guesses as attempts.
    c += 1

    if guess < rd:
        print("Too low")

    elif guess > rd:
        print("Too high")

    else:
        print("Right!")
        print("You took only", c, "tries!")

input()
