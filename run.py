
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
        
def place_ship(grid, length):

    """
    Place a ship of given length randomly on the player and computer grid.
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
        if all(grid[row + (i if orientation == 'vertical' else 0)][col + (i if orientation == 'horizontal' else 0)] == 'o'
               for i in range(length)):
            for i in range(length):
                grid[row + (i if orientation == 'vertical' else 0)][col + (i if orientation == 'horizontal' else 0)] = '-'
            break

def start_game():
    """
    Starts the Battleship game by guiding the player through the initial steps.
    """
# display title and ask player name
    print("Battleship")
    print("Enter your name to start the game")

    player_name= input("Enter your Name here: ")
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

# Place ships on player and computer grids
    for _ in range(num_ships):
        place_ship(player_grid, ship_length)

    for _ in range(num_ships):
        place_ship(computer_grid, ship_length)

    player_ships_remaining = num_ships  
    computer_ships_remaining = num_ships
    current_player = 'player'   

    play_game(player_grid, computer_grid, num_ships, player_ships_remaining, computer_ships_remaining, current_player)

def handle_guess(grid, guess_row, guess_col):
    '''
    handling attacks and determining whether a shot has hit a ship or not
    '''

    if grid[guess_row][guess_col] == '-':

        grid[guess_row][guess_col] = 'hit'  
        return 'hit'  
    elif grid[guess_row][guess_col] == 'o':
        grid[guess_row][guess_col] = 'miss'  
        return 'miss'  
    else:
        return 'already_guessed' 

def play_game(player_grid, computer_grid, num_ships, player_ships_remaining, computer_ships_remaining, current_player):
    """
    Main logic handling player and computer attacks, determines winner.
    """
    while player_ships_remaining > 0 and computer_ships_remaining > 0:
        if current_player == 'player':
            print("\nPlayer's Turn")
            
            while True:
                try:
                    guess_row = int(input("Guess Row (1-5): "))
                    if 1 <= guess_row <= 5:
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            while True:
                try:
                    guess_col = int(input("Guess Col (1-5): "))
                    if 1 <= guess_col <= 5:
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            result = handle_guess(computer_grid, guess_row, guess_col)

            if result == 'hit':
                print("You hit an enemy ship!")
                computer_ships_remaining -= 1
            elif result == 'miss':
                print("You missed.")
            else:
                print("You already guessed that.")

                current_player = 'computer'

        else:
                print("\nComputer's Turn")
                guess_row = randint(1, len(player_grid) - 1)
                guess_col = randint(1, len(player_grid[0]) - 1)
                result = handle_guess(player_grid, guess_row, guess_col)

                if result == 'hit':
                    print("The computer hit your ship!")
                    player_ships_remaining -= 1
                elif result == 'miss':
                    print("The computer missed.")
                else:
                    break
                    continue

                current_player = 'player'

        if player_ships_remaining == 0:
            print("Congratulations! You sank all enemy ships. You win :(")
        else:
            print("The computer sank all your ships. Computer wins :(")

# 
# Mise à jour de la grille après les attaques 


start_game()



