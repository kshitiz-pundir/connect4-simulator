import unittest
from connect4 import (
    create_board, get_next_open_row, drop_piece,
    is_valid_column, check_win, simulate_move
)

class TestConnect4(unittest.TestCase):
    def test_board_creation(self):
        board = create_board()
        self.assertEqual(len(board), 6)
        self.assertEqual(len(board[0]), 7)
        self.assertTrue(all(cell == '-' for row in board for cell in row))

    def test_drop_piece(self):
        board = create_board()
        row = get_next_open_row(board, 0)
        drop_piece(board, row, 0, 'X')
        self.assertEqual(board[5][0], 'X')

    def test_valid_column(self):
        board = create_board()
        self.assertTrue(is_valid_column(board, 0))
        for i in range(6):
            drop_piece(board, get_next_open_row(board, 0), 0, 'O')
        self.assertFalse(is_valid_column(board, 0))

    def test_win_horizontal(self):
        board = create_board()
        for col in range(4):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 'X')
        self.assertTrue(check_win(board, 'X'))

    def test_simulate_move(self):
        board = create_board()
        temp = simulate_move(board, 3, 'O')
        self.assertEqual(temp[5][3], 'O')
        self.assertEqual(board[5][3], '-')  # original should be unchanged

if __name__ == '__main__':
    unittest.main()