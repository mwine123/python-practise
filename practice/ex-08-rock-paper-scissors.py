# This is a simple rock, paper, scissors game for two players. The players will be prompted to enter their choices, and the program will determine the winner based on the rules of the game. The game will continue until the players decide to stop playing.

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}

    player_a = str(input("Player a: ")).lower()
    player_b = str(input("Player b: ")).lower()

    # Validate that Player A entered one of the allowed choices.
    if player_a not in game_dict:
        print("Invalid choice for Player A. Please choose rock, scissors, or paper.")
        continue

    # Validate that Player B entered one of the allowed choices.
    if player_b not in game_dict:
        print("Invalid choice for Player B. Please choose rock, scissors, or paper.")
        continue

    a = game_dict.get(player_a)
    b = game_dict.get(player_b)

    dif = a - b

    if dif in [-1, 2]:
        print('Player A wins.')

    elif dif in [-2, 1]:
        print('Player B wins.')

    else:
        print('Draw. Please continue.')

    # Ask whether the players want to start another round.
    play_again = input('Do you want to play another game, yes or no?\n').lower()

    # Validate the response before deciding whether to continue.
    while play_again not in ['yes', 'no']:
        play_again = input("Please enter 'yes' or 'no': ").lower()

    if play_again == 'yes':
        continue
    else:
        print('Game over.')
        break
