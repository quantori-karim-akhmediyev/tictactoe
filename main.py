import argparse
import sys
from exceptions import InvalidCommandError, InvalidCoordinatesError, InvalidFileError, InvalidPlayerError
from game_logic import TicTacToe

PLAYER_X = "X"
PLAYER_O = "O"
VALID_PLAYERS = {PLAYER_X, PLAYER_O}
BOARD_SIZE = 3
EMPTY_CELL = " "

def parse_arguments():
    parser = argparse.ArgumentParser(description="Play TicTacToe from a file of moves.")
    parser.add_argument("filepath", type=str, help="Path to the file with moves")
    parser.add_argument("--show-board", action="store_true", help="Flag to display the board after each move")
    return parser.parse_args()


def process_file(filepath):
    try:
        with open(filepath, 'r') as file:
            moves = file.readlines()
        return moves
    except IOError:
        raise InvalidFileError("Failed to read the file.")


def parse_move(line):
    parts = line.strip().split()

    if len(parts) != 3:
        raise InvalidCommandError("Invalid input format. Expected 3 parts.")
    if parts[0].lower() != "player":
        raise InvalidCommandError("Invalid input format. 'player' keyword missing.")
    if parts[1].upper() not in {PLAYER_X, PLAYER_O}:
        raise InvalidCommandError(f"Invalid input format. Invalid player: {parts[1]}")

    player = parts[1]
    coordinates = parts[2].split(',')
    if len(coordinates) != 2:
        raise InvalidCoordinatesError("Invalid coordinates format")
    x, y = map(int, coordinates)
    if x <= 0 or x > BOARD_SIZE or y <= 0 or y > BOARD_SIZE:
        raise InvalidCoordinatesError("Invalid coordinates")

    return player, x, y


def execute_moves(game, moves, show_board):
    for line in moves:
        player, x, y = parse_move(line)
        game.make_move(player, x, y)
        if show_board:
            game.print_board()
        if game.winner:
            print(f"The winner is {game.winner}")
            return "win"
    if game.is_draw:
        return "draw"
    return "unfinished"



def main():
    args = parse_arguments()
    game = TicTacToe(board_size=BOARD_SIZE)

    try:
        moves = process_file(args.filepath)
        game_status = execute_moves(game, moves, args.show_board)
        if game_status == "draw":
            print("The game is a draw.")
        elif game_status == "unfinished":
            print("The game is not yet finished.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
