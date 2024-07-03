import unittest
from unittest.mock import mock_open, patch, MagicMock
from main import parse_arguments, process_file, parse_move, execute_moves
from exceptions import InvalidCommandError, InvalidCoordinatesError, InvalidFileError
from game_logic import TicTacToe


class TestMain(unittest.TestCase):

    def test_argument_parsing(self):
        test_args = ["program", "path/to/moves.txt", "--show-board"]
        with patch('sys.argv', test_args):
            args = parse_arguments()
            self.assertEqual(args.filepath, "path/to/moves.txt")
            self.assertTrue(args.show_board)


    def test_file_processing_success(self):
        m = mock_open(read_data='player X 1,2\nplayer O 2,3')
        with patch('builtins.open', m):
            result = process_file("path/to/moves.txt")
            self.assertEqual(result, ['player X 1,2\n', 'player O 2,3'])


    def test_file_processing_failure(self):
        with patch('builtins.open', mock_open()) as m:
            m.side_effect = IOError
            with self.assertRaises(InvalidFileError):
                process_file("invalid/path/to/moves.txt")


    def test_parse_move_success(self):
        line = "player X 1,2"
        result = parse_move(line)
        self.assertEqual(result, ('X', 1, 2))


    def test_parse_move_failures(self):
        with self.assertRaises(InvalidCommandError):
            parse_move("playerx 1,2")
        with self.assertRaises(InvalidCommandError):
            parse_move("player 1,2")
        with self.assertRaises(InvalidCoordinatesError):
            parse_move("player X 0,2")
        with self.assertRaises(InvalidCoordinatesError):
            parse_move("player X -2,-1")


    def test_execute_moves(self):
        game = TicTacToe(board_size=3)
        moves = ["player X 1,2", "player O 2,3"]
        with patch.object(TicTacToe, 'make_move', return_value=None) as mock_make_move:
            result = execute_moves(game, moves, False)
            self.assertEqual(mock_make_move.call_count, 2)
            self.assertEqual(result, "unfinished")

if __name__ == '__main__':
    unittest.main()
