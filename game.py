import copy
from board import Board
from player import Player


class Game:
    NOT_OVER = 0
    PLAYER_WINS = 1
    BOT_WINS = 2
    DRAW = 3
    PLAYER_WINS_MSG = "Congratz!! You are the winner!!!"
    BOT_WINS_MSG = "Looooooooser!!!"
    DRAW_GAME_MSG = "Draw"

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def is_over(self, matrix):
        if matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2]:
            if matrix[0][0] is "X":
                return self.PLAYER_WINS
            if matrix[0][0] is "O":
                return self.BOT_WINS

        if matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2]:
            if matrix[1][0] is "X":
                return self.PLAYER_WINS
            if matrix[1][0] is "O":
                return self.BOT_WINS

        if matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2]:
            if matrix[2][0] is "X":
                return self.PLAYER_WINS
            if matrix[2][0] is "O":
                return self.BOT_WINS

        if matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0]:
            if matrix[0][0] is "X":
                return self.PLAYER_WINS
            if matrix[0][0] is "O":
                return self.BOT_WINS

        if matrix[0][1] == matrix[1][1] and matrix[1][1] == matrix[2][1]:
            if matrix[0][1] is "X":
                return self.PLAYER_WINS
            if matrix[0][1] is "O":
                return self.BOT_WINS

        if matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2]:
            if matrix[0][2] is "X":
                return self.PLAYER_WINS
            if matrix[0][2] is "O":
                return self.BOT_WINS

        if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
            if matrix[0][0] is "X":
                return self.PLAYER_WINS
            if matrix[0][0] is "O":
                return self.BOT_WINS

        if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
            if matrix[0][2] is "X":
                return self.PLAYER_WINS
            if matrix[0][2] is "O":
                return self.BOT_WINS

        places = set()
        for row in matrix:
            for place in row:
                places.add(place)

        if ' ' not in places:
            return self.DRAW

        return self.NOT_OVER

    def get_available_moves(self, matrix):
        moves = []
        for row in range(3):
            for place in range(3):
                if matrix[row][place] == " ":
                    moves.append((row+1, place+1))
        return moves

    def player_move(self):
        (row, col) = self.player.make_move()
        while not self.board.is_free(row, col):
            (row, col) = self.player.make_move()
        self.board.place_X(row, col)

    def bot_move(self):
        best_turn = self.minimax(self.board, 0, None, True)
        (row, col) = self.get_available_moves(self.board.matrix)[best_turn]
        self.board.place_O(row, col)

### magic below
    def minimax(self, board, depth, move=None, main_minimax=False):
        if move is not None:
            if board.bot_turn:
                board.place_O(move[0], move[1])
            else:
                board.place_X(move[0], move[1])

        if self.is_over(board.matrix):
            return self.get_score(depth, board.matrix)

        depth += 1
        scores = []
        for move in self.get_available_moves(board.matrix):
            copy_board = copy.deepcopy(board)
            scores.append(self.minimax(copy_board, depth, move))

        if not main_minimax:
            if board.bot_turn:
                return max(scores)
            else:
                return min(scores)
        return scores.index(max(scores))

    def get_score(self, depth, matrix):
        if self.is_over(matrix) is self.PLAYER_WINS:
            return depth - 10
        elif self.is_over(matrix) is self.BOT_WINS:
            return 10 - depth
        else:
            return 0

    def print_winner(self):
        if self.is_over(self.board.matrix) is self.PLAYER_WINS:
            return self.PLAYER_WINS_MSG
        elif self.is_over(self.board.matrix) is self.BOT_WINS:
            return self.BOT_WINS_MSG
        else:
            return self.DRAW_GAME_MSG

    def execute(self):
        print(self.board)
        while not self.is_over(self.board.matrix):
            if self.board.bot_turn:
                self.bot_move()
            else:
                self.player_move()
            print(self.board)
        print(self.print_winner())


def main():
    asd = Board()
    pro = Player()
    game = Game(asd, pro)
    game.execute()


if __name__ == '__main__':
    main()
