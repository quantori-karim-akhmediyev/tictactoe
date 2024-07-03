from exceptions import InvalidMoveError, InvalidPlayerError


class TicTacToe:
    '''
    Represents a TicTacToe game.

        1 represents 'X',
        -1 represents 'O',
        0 represents an empty cell.
    '''

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.winner = None
        self.is_draw = False
        self.__current_player = 1 # X starts


    def __check_rows(self):
        for row in self.board:
            if abs(sum(row)) == self.board_size:
                return "X" if sum(row) > 0 else "O"
        return None


    def __check_columns(self):
        for col in range(self.board_size):
            column_sum = sum(self.board[row][col] for row in range(self.board_size))
            if abs(column_sum) == self.board_size:
                return "X" if column_sum > 0 else "O"
        return None


    def __check_diagonals(self):
        diag1_sum = sum(self.board[i][i] for i in range(self.board_size))
        diag2_sum = sum(self.board[i][self.board_size-1-i] for i in range(self.board_size))
        if abs(diag1_sum) == self.board_size:
            return "X" if diag1_sum > 0 else "O"
        if abs(diag2_sum) == self.board_size:
            return "X" if diag2_sum > 0 else "O"
        return None


    def __check_winner(self):
        # Check each type of line for a winner
        return self.__check_rows() or self.__check_columns() or self.__check_diagonals()


    def __check_draw(self):
        if all(cell != 0 for row in self.board for cell in row) and not self.winner:
            self.is_draw = True


    def make_move(self, player, x, y):
        if not (1 <= x <= self.board_size and 1 <= y <= self.board_size):
            raise InvalidMoveError("Move is out of bounds.")

        if self.board[x-1][y-1] != 0:
            raise InvalidMoveError("Position already occupied.")

        if self.__current_player != (1 if player == 'X' else -1):
            raise InvalidPlayerError("Not your turn.")

        self.board[x-1][y-1] = self.__current_player
        self.__current_player *= -1  # Toggle player

        self.winner = self.__check_winner()
        self.__check_draw()


    def print_board(self):
        symbol_map = {1: 'X', -1: 'O', 0: ' '}
        for row in self.board:
            print("|".join(symbol_map[cell] for cell in row))
            print("-" * (2 * self.board_size - 1))
        print()



