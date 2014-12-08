from board import Board
import unittest


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.tictac = Board()

    def test_init(self):
        check_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.tictac.board, check_board)

    def test_is_X_placed(self):
        self.tictac.place_X(1, 1)
        self.assertEqual(self.tictac.board[0][0], "X")

    def test_is_O_placed(self):
        self.tictac.place_O(1, 1)
        self.assertEqual(self.tictac.board[0][0], "O")

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

    def test_is_not_over(self):
        self.tictac.board = [['X', 'O', 'X'],
                             ['O', 'O', 'X'],
                             ['X', 'X', 'O']]
        self.assertEqual(self.tictac.is_over(), self.tictac.DRAW)

    def test_is_not_over_empty_board(self):
        self.assertEqual(self.tictac.is_over(), self.tictac.NOT_OVER)

    def test_is_over_row(self):
        self.tictac.board = [['X', 'X', 'X'],
                             ['1', '2', '3'],
                             ['4', '5', '6']]
        self.assertEqual(self.tictac.is_over(), self.tictac.PLAYER_WINS)

    def test_is_over_row_v2(self):
        self.tictac.board = [['6', '5', '4'],
                             ['O', 'O', 'O'],
                             ['3', '2', '1']]
        self.assertEqual(self.tictac.is_over(), self.tictac.BOT_WINS)

    def test_is_over_row_v3(self):
        self.tictac.board = [['1', '2', '3'],
                             ['4', '5', '6'],
                             ['O', 'O', 'O']]
        self.assertEqual(self.tictac.is_over(), self.tictac.BOT_WINS)

    def test_is_over_col(self):
        self.tictac.board = [['X', '6', '5'],
                             ['X', '4', '3'],
                             ['X', '2', '1']]
        self.assertEqual(self.tictac.is_over(), self.tictac.PLAYER_WINS)

    def test_is_over_col_v2(self):
        self.tictac.board = [['1', 'O', '2'],
                             ['3', 'O', '4'],
                             ['5', 'O', '6']]
        self.assertEqual(self.tictac.is_over(), self.tictac.BOT_WINS)

    def test_is_over_col_v3(self):
        self.tictac.board = [['1', '2', 'O'],
                             ['3', '4', 'O'],
                             ['5', '6', 'O']]
        self.assertEqual(self.tictac.is_over(), self.tictac.BOT_WINS)

    def test_is_over_diagonal(self):
        self.tictac.board = [['X', '1', '2'],
                             ['3', 'X', '4'],
                             ['5', '6', 'X']]
        self.assertEqual(self.tictac.is_over(), self.tictac.PLAYER_WINS)

    def test_is_over_diagonal_v2(self):
        self.tictac.board = [['6', '5', 'O'],
                             ['4', 'O', '3'],
                             ['O', '2', '1']]
        self.assertEqual(self.tictac.is_over(), self.tictac.BOT_WINS)

##--------------AI tests----------------------------

    def test_get_score_draw(self):
        self.tictac.board = [['X', 'X', 'O'],
                             ['O', 'O', 'X'],
                             ['X', 'O', 'X']]
        self.assertEqual(0, self.tictac.get_score(0))

    def test_get_score_player_win(self):
        self.tictac.board = [['X', 'X', 'X'],
                             ['O', 'O', 'X'],
                             ['X', 'O', 'X']]
        self.assertEqual(-10, self.tictac.get_score(0))

    def test_get_score_bot_wins(self):
        self.tictac.board = [['X', 'X', 'O'],
                             ['O', 'O', 'X'],
                             ['O', 'O', 'X']]
        self.assertEqual(10, self.tictac.get_score(0))

    def test_minimax_one_empty_place(self):
        self.tictac.board = [['X', 'X', 'O'],
                             ['O', 'X', 'X'],
                             ['O', 'O', ' ']]
        minimax = self.tictac.minimax(self.tictac, 0, None, True)
        self.assertEqual(0, minimax)


if __name__ == '__main__':
    unittest.main()
