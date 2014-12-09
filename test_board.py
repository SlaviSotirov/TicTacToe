from board import Board
import unittest


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.tictac = Board()

    def test_init(self):
        check_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.tictac.matrix, check_board)

    def test_is_X_placed(self):
        self.tictac.place_X(1, 1)
        self.assertEqual(self.tictac.matrix[0][0], "X")

    def test_is_O_placed(self):
        self.tictac.place_O(1, 1)
        self.assertEqual(self.tictac.matrix[0][0], "O")

    def test_is_free(self):
        self.assertTrue(self.tictac.is_free(1, 1))

    def test_is_not_free(self):
        self.tictac.place_X(1, 1)
        self.assertFalse(self.tictac.is_free(1, 1))

    def test_is_out(self):
        self.assertTrue(self.tictac.is_out(4, 4))

    def test_is_out_col(self):
        self.assertTrue(self.tictac.is_out(2, 4))

    def test_is_out_row(self):
        self.assertTrue(self.tictac.is_out(4, 2))

    def test_is_in(self):
        self.assertFalse(self.tictac.is_out(3, 3))


if __name__ == '__main__':
    unittest.main()
