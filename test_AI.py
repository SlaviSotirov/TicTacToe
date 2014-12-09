from game import Game
from board import Board
from player import Player
import unittest


class TestGame(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.player = Player()
        self.tictac = Game(self.board, self.player)

    def test_minimax_one_empty_place(self):
        self.tictac.board.matrix = [['X', 'X', 'O'],
                                    ['O', 'X', 'X'],
                                    ['O', 'O', ' ']]
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(0, minimax)

    ### In order not to lose, if the enemy plays in the corner
    ### the best move is in the center in the matrix

    ### Counting indexes starts from top left to the end of the row
    ### Then countinues with the lower row (It counts free places!)

    def test_minimax_must_play_in_center(self):
        self.tictac.board.matrix = [['X', ' ', ' '],
                                    [' ', ' ', ' '],
                                    [' ', ' ', ' ']]
        self.tictac.board.change_turn()
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(3, minimax, "Index of the center in the matrix (4th position)")

    def test_minimax_must_play_in_center_v2(self):
        self.tictac.board.matrix = [[' ', ' ', 'X'],
                                    [' ', ' ', ' '],
                                    [' ', ' ', ' ']]
        self.tictac.board.change_turn()
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(3, minimax, "Index of the center in the matrix (4th position)")

    def test_minimax_must_play_in_center_v3(self):
        self.tictac.board.matrix = [[' ', ' ', ' '],
                                    [' ', ' ', ' '],
                                    ['X', ' ', ' ']]
        self.tictac.board.change_turn()
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(4, minimax, "Index of the center in the matrix (5th position)")

    def test_minimax_must_play_in_center_v4(self):
        self.tictac.board.matrix = [[' ', ' ', ' '],
                                    [' ', ' ', ' '],
                                    [' ', ' ', 'X']]
        self.tictac.board.change_turn()
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(4, minimax, "Index of the center in the matrix (5th position)")

    def test_minimax_must_block_enemy(self):
        self.tictac.board.matrix = [[' ', ' ', ' '],
                                    [' ', 'X', ' '],
                                    [' ', ' ', 'X']]
        self.tictac.board.change_turn()
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(0, minimax, "Index of the move that blocks the enemy (1st position)")

    def test_minimax_must_block_enemy_v2(self):
        self.tictac.board.matrix = [['X', 'X', ' '],
                                    [' ', ' ', ' '],
                                    [' ', ' ', ' ']]
        self.tictac.board.change_turn()
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(0, minimax, "Index of the move that blocks the enemy (1st position)")

    def test_minimax_winning_before_blocking(self):
        self.tictac.board.matrix = [['X', 'X', ' '],
                                    ['O', 'O', ' '],
                                    [' ', ' ', ' ']]
        self.tictac.board.change_turn()
        minimax = self.tictac.minimax(self.tictac.board, 0, None, True)
        self.assertEqual(1, minimax, "Index of the move that wins the game (2nd position)")

if __name__ == '__main__':
    unittest.main()
