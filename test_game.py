from game import Game
from board import Board
from player import Player
import unittest


class TestGame(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.player = Player()
        self.tictac = Game(self.board, self.player)

    def test_is_not_over(self):
        self.tictac.board.matrix = [['X', 'O', 'X'],
                                    ['O', 'O', 'X'],
                                    ['X', 'X', 'O']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.DRAW)

    def test_is_not_over_empty_board(self):
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.NOT_OVER)

    def test_is_over_row(self):
        self.tictac.board.matrix = [['X', 'X', 'X'],
                                    ['1', '2', '3'],
                                    ['4', '5', '6']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.PLAYER_WINS)

    def test_is_over_row_v2(self):
        self.tictac.board.matrix = [['6', '5', '4'],
                                    ['O', 'O', 'O'],
                                    ['3', '2', '1']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.BOT_WINS)

    def test_is_over_row_v3(self):
        self.tictac.board.matrix = [['1', '2', '3'],
                                    ['4', '5', '6'],
                                    ['O', 'O', 'O']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.BOT_WINS)

    def test_is_over_col(self):
        self.tictac.board.matrix = [['X', '6', '5'],
                                    ['X', '4', '3'],
                                    ['X', '2', '1']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.PLAYER_WINS)

    def test_is_over_col_v2(self):
        self.tictac.board.matrix = [['1', 'O', '2'],
                                    ['3', 'O', '4'],
                                    ['5', 'O', '6']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.BOT_WINS)

    def test_is_over_col_v3(self):
        self.tictac.board.matrix = [['1', '2', 'O'],
                                    ['3', '4', 'O'],
                                    ['5', '6', 'O']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.BOT_WINS)

    def test_is_over_diagonal(self):
        self.tictac.board.matrix = [['X', '1', '2'],
                                    ['3', 'X', '4'],
                                    ['5', '6', 'X']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.PLAYER_WINS)

    def test_is_over_diagonal_v2(self):
        self.tictac.board.matrix = [['6', '5', 'O'],
                                    ['4', 'O', '3'],
                                    ['O', '2', '1']]
        self.assertEqual(self.tictac.is_over(self.tictac.board.matrix), self.tictac.BOT_WINS)

    def test_get_score_draw(self):
        self.tictac.board.matrix = [['X', 'X', 'O'],
                                    ['O', 'O', 'X'],
                                    ['X', 'O', 'X']]
        self.assertEqual(0, self.tictac.get_score(0, self.tictac.board.matrix))

    def test_get_score_player_win(self):
        self.tictac.board.matrix = [['X', 'X', 'X'],
                                    ['O', 'O', 'X'],
                                    ['X', 'O', 'X']]
        self.assertEqual(-10, self.tictac.get_score(0, self.tictac.board.matrix))

    def test_get_score_bot_wins(self):
        self.tictac.board.matrix = [['X', 'X', 'O'],
                                    ['O', 'O', 'X'],
                                    ['O', 'O', 'X']]
        self.assertEqual(10, self.tictac.get_score(0, self.tictac.board.matrix))

    def test_print_player_winner(self):
        self.tictac.board.matrix = [['X', 'X', 'X'],
                                    ['O', 'O', 'X'],
                                    ['O', 'O', 'X']]
        self.assertEqual(self.tictac.PLAYER_WINS_MSG, self.tictac.print_winner())

    def test_print_bot_winner(self):
        self.tictac.board.matrix = [['X', 'X', 'O'],
                                    ['O', 'O', 'X'],
                                    ['O', 'O', 'X']]
        self.assertEqual(self.tictac.BOT_WINS_MSG, self.tictac.print_winner())

    def test_print_draw_game(self):
        self.tictac.board.matrix = [['X', 'X', 'O'],
                                    ['O', 'O', 'X'],
                                    ['X', 'O', 'X']]
        self.assertEqual(self.tictac.DRAW_GAME_MSG, self.tictac.print_winner())

if __name__ == '__main__':
    unittest.main()
