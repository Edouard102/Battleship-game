

import random
from random import randint 

# python3 run.py

def create_grid(rows, cols):
    """
    Create a grid 5x5
    """

    grid = [['o' for _ in range(cols + 1)] for _ in range(rows + 1)] 

    # Set row headers (latitude indices)
    for i in range(1, rows + 1):
        grid[i][0] = str(i)  

    # Set column headers (longitude indices)
    for j in range(1, cols + 1):
        grid[0][j] = str(j)  
    return grid

def display_grid(grid):
    """
    Display the grid's current state.
    """
    for row in grid:
        print(' '.join(row))
        
def start_game():
    """
    Starts the Battleship game by guiding the player through the initial steps.
    """
# display title and ask player name
    print("Battleship")
    print("Enter your name to start the game")
    print("David")

    player_name= input("Enter your data here: ")
    print(f"Welcome, {player_name} :)")

# Display the game rules
    print("\nRules of the Game:")
    print("1. Battleship is a two-player game.")
    print("2. Each player will have a random placement for these ships on his grid.")
    print("3. Players take turns guessing the coordinates to target the opponent's ships.")
    print("4. The first player to sink all of the opponent's ships wins.")
    
    input("Press Enter to start the game...")

# display grid for player and computer
    player_grid = create_grid(5, 5)
    
    computer_grid = create_grid(5, 5)

    print("\nHere's your game grid:")
    display_grid(player_grid)

    print("\nHere's the computer's game grid:")
    display_grid(computer_grid)
# Define the number of the ships   
    num_ships = 4
# Define the length of the ships
    ship_length = 2  
    for _ in range(num_ships):
        place_ship(player_grid, ship_length)

    for _ in range(num_ships):
        place_ship(computer_grid, ship_length)

#play_game(player_grid, computer_grid, num_ships)

#The actual game logic would be add here
# This would include player turns,  4 random ship placement , shooting, score rest game etc.

def place_ship(grid, length):
    """
    Place a ship of given length randomly on the player's grid.
    """
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(1, len(grid) - 1)
            col = random.randint(1, len(grid[0]) - length)
        else:
            row = random.randint(1, len(grid) - length)
            col = random.randint(1, len(grid[0]) - 1)
        
        # Check if the positions are available
        if all(grid[row + (i if orientation == 'vertical' else 0)][col + (i if orientation == 'horizontal' else 0)] == 'O'
               for i in range(length)):
            for i in range(length):
                grid[row + (i if orientation == 'vertical' else 0)][col + (i if orientation == 'horizontal' else 0)] = '-'
            break



start_game()



