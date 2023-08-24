

import random
from random import randint 

# python3 run.py

def start_game():
    """
    Starts the Battleship game by guiding the player through the initial steps.
    """
# display title and ask player name
    print("Battleship")
    print("Enter your name to start the game")
    print("David")

    player_name= input("Enter your data here: ")
    print(f"Welcome, {player_name}!")

# Display the game rules
    print("\nRules of the Game:")
    print("1. Battleship is a two-player game.")
    # print("2. Each player sets up their ships on their own grid.")
    print("3. Players take turns guessing the coordinates to target the opponent's ships.")
    print("4. The first player to sink all of the opponent's ships wins.")
    
    input("Press Enter to start the game...")

start_game()



