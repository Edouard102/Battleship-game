
import random
from random import randint

# python3 run.py


class BattleshipGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.num_ships = 4
        self.ship_length = 1
        self.player_board = self.create_board()
        self.computer_board = self.create_board()

    def create_board(self):
        """
        Create a grid 5x5
        """
        board = [['~' for _ in range(self.cols + 1)]
                 for _ in range(self.rows + 1)]

    # Set row headers (latitude indices)
        for i in range(1, self.rows + 1):
            board[i][0] = str(i)

    # Set column headers (longitude indices)
        for j in range(1, self.cols + 1):
            board[0][j] = str(j)

        return board


def display_board(board, hide_ships=False):
    """
    Display the grid's current state.
    """
    for row in board:
        row_display = []
        for cell in row:
            if hide_ships and cell == 'O':
                row_display.append('~')
            else:
                row_display.append(cell)
        print(' '.join(row_display))


def place_ship(board, length):

    """
    Place a ship of given length randomly on the player and computer grid.
    """
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(1, len(board) - 1)
            col = random.randint(1, len(board[0]) - length)
        else:
            row = random.randint(1, len(board) - length)
            col = random.randint(1, len(board[0]) - 1)

# Check if the positions are available
        if all(board[row + (i if orientation == 'vertical' else 0)]
               [col + (i if orientation == 'horizontal' else 0)] == '~'
               for i in range(length)):
            for i in range(length):
                board[row + (i if orientation == 'vertical' else 0)][col + (i if orientation == 'horizontal' else 0)] = 'O'
            break


# handle the guess for the player
def handle_player_guess(computer_board, guess_row, guess_col, player_type):
    '''
    handling attacks and determining whether a shot has hit a ship or not
    X = Hit
    x = miss
    G guess Already
    '''
    if computer_board[guess_row][guess_col] == 'O':
        computer_board[guess_row][guess_col] = 'X'
        return 'X'
    elif computer_board[guess_row][guess_col] == '~':
        computer_board[guess_row][guess_col] = 'x'
        return 'x'
    else:
        return 'G'


# handle the guess for the computer
def handle_computer_guess(player_board, guess_row, guess_col, player_type):
    '''
    handling attacks and determining whether a shot has hit a ship or not
    X = Hit
    x = miss
    G guess Already
    '''
    if player_board[guess_row][guess_col] == 'O':
        player_board[guess_row][guess_col] = 'X'
        return 'X'
    elif player_board[guess_row][guess_col] == '~':
        player_board[guess_row][guess_col] = 'x'
        return 'x'
    else:
        return 'G'


# Main logic of the game
def play_game(player_board, computer_board, num_ships, player_ships_remaining,
              computer_ships_remaining,
              current_player, name, rank):
    """
    Main logic handling player and computer attacks, determines winner.
    """
    while player_ships_remaining > 0 and computer_ships_remaining > 0:
        if current_player == 'player':
            print(f"\n {rank} {name}s Turn")

            while True:
                try:
                    guess_row = int(input("Guess Row (1-5): "))
                    if 1 <= guess_row <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Please enter a valid number.")

            while True:
                try:
                    guess_col = int(input("Guess Col (1-5): "))
                    if 1 <= guess_col <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Please enter a valid number.")

            result_player = handle_player_guess(computer_board,
                                                guess_row, guess_col, 'player')

            if result_player == 'X':
                print("You hit an enemy ship!")
                computer_ships_remaining -= 1
            elif result_player == 'x':
                print("You missed.")
            else:
                print("You already guessed.")

# Update computer board with the result of the computer's attack
            computer_board[guess_row][guess_col] = result_player

            current_player = 'computer'

        else:
            print("\nComputer's Turn")
            guess_row = randint(1, len(player_board) - 1)
            guess_col = randint(1, len(player_board[0]) - 1)

            result_computer = handle_computer_guess(player_board, guess_row, guess_col, 'computer')

            if result_computer == 'X':
                print("The computer hit your ship!")
                player_ships_remaining -= 1
            elif result_computer == 'x':
                print("The computer missed.")

# Update player board with the result of the player's attack
            player_board[guess_row][guess_col] = result_computer

            current_player = 'player'


# Update player and computer board and display it
        print(f"\nHere's {rank} {name} game board")
        display_board(player_board)
        print("Number of Battleships:", player_ships_remaining)

        print("\nHere's the computer game board")
        display_board(computer_board, hide_ships=True)
        print("Number of Battleships:", computer_ships_remaining)

    if player_ships_remaining == 0:
        print("The computer sank all your ships. Computer wins :(")
    else:
        print("Congratulations! You sank all enemy ships. You win :)")


# function to start a new game
def new_game(name, rank):
    """
    Function that asks if we want to play again at the end of the game
    """
    while True:
        player = input(f"{rank} {name} Do you want to play? (y/n): ")
        if player == 'y':
            start_game()
        elif player == 'n':
            print(f"{rank} {name} Thanks for playing! Goodbye.:)")
            exit()
        else:
            print("Answer with 'y' or 'n'.")


# function to start the game
def start_game():
    """
    Starts the Battleship game by guiding the player through the initial steps.
    """
# display title and ask player name
    print("eBattleship")
    print("Enter your Name and Rank to start the game")
    name = input("Enter your Name here: ")
    rank = input("Enter your Rank here: ")
    print(f"Welcome, {rank} {name} :)")

# Display the game rules
    print("\nRules of the Game:")
    print(". Battleship is a two-player game.")
    print(". Each player will have a random placement on board.")
    print(". Each player will have for 4 ships on his board.")
    print(". Players take turns guessing the coordinates of the ships.")
    print(". The first player to sink all of the opponent's ships wins.")
    print(". The boats will be 5represented by O")
    print(". Successful shot will be represented  by X")
    print(". Missed shot  will be represented  by x")

    input("Press Enter to start the game...")

# display board for player and computer
    game = BattleshipGame(5, 5)
    player_board = game.create_board()
    computer_board = game.create_board()

# Define the number and the length of the ships
    num_ships = 4
    ship_length = 1

# Place ships on player and computer board
    print(f"\nHere's {rank} {name} game board")
    for _ in range(num_ships):
        place_ship(player_board, ship_length)
    display_board(player_board)
    print("Number of Battleships:", num_ships)

    print("\nHere's the computer game board")
    for _ in range(num_ships):
        place_ship(computer_board, ship_length)
    display_board(computer_board, hide_ships=True)
    print("Number of Battleships:", num_ships)

    player_ships_remaining = num_ships
    computer_ships_remaining = num_ships
    current_player = 'player'

    play_game(player_board, computer_board, num_ships, player_ships_remaining,
              computer_ships_remaining,
              current_player, name, rank)

    new_game(name, rank)


start_game()
