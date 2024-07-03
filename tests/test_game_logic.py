import unittest
from game_logic import TicTacToe
from exceptions import InvalidMoveError

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_board_initialization(self):
        self.assertEqual(self.game.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                         "Board should be initialized with all zeros.")

    def test_valid_move(self):
        self.game.make_move('X', 1, 1)
        self.assertEqual(self.game.board[0][0], 1,
                         "Making a move should set the correct board cell.")

    def test_invalid_move_out_of_bounds(self):
        with self.assertRaises(InvalidMoveError):
            self.game.make_move('X', 4, 1)

    def test_move_on_occupied_space(self):
        self.game.make_move('X', 1, 1)
        with self.assertRaises(InvalidMoveError):
            self.game.make_move('O', 1, 1)

    def test_alternate_turns(self):
        self.game.make_move('X', 1, 1)
        self.game.make_move('O', 1, 2)
        self.assertEqual(self.game.board[0][1], -1,
                         "O should be able to make a move after X.")

    def test_horizontal_win(self):
        self.game.make_move('X', 1, 1)
        self.game.make_move('O', 2, 1)
        self.game.make_move('X', 1, 2)
        self.game.make_move('O', 2, 2)
        self.game.make_move('X', 1, 3)
        self.assertEqual(self.game.winner, 'X',
                         "X should win with a horizontal line.")

    def test_vertical_win(self):
        self.game.make_move('X', 1, 1)
        self.game.make_move('O', 1, 2)
        self.game.make_move('X', 2, 1)
        self.game.make_move('O', 2, 2)
        self.game.make_move('X', 3, 1)
        self.assertEqual(self.game.winner, 'X',
                         "X should win with a vertical line.")

    def test_diagonal_win(self):
        self.game.make_move('X', 1, 1)
        self.game.make_move('O', 1, 2)
        self.game.make_move('X', 2, 2)
        self.game.make_move('O', 1, 3)
        self.game.make_move('X', 3, 3)
        self.assertEqual(self.game.winner, 'X',
                         "X should win with a diagonal line.")

    def test_draw(self):
    # This sequence should fill the board completely without any player winning.
        moves = [(1, 1), (1, 2), (2, 2),
                (3, 3), (3, 2), (3, 1),
                (2, 3), (2, 1), (1, 3)]
        players = ['X', 'O'] * 5
        for (player, move) in zip(players, moves):
            self.game.make_move(player, *move)
        self.assertTrue(self.game.is_draw, "The game should be a draw with no empty spaces and no winner.")



if __name__ == '__main__':
    unittest.main()
