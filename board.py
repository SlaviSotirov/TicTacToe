from player import Player
import copy


class Board:
    NOT_OVER = 0
    PLAYER_WINS = 1
    BOT_WINS = 2
    DRAW = 3

    def __init__(self):
        self.board = [[" " for row in range(3)] for col in range(3)]
        self.player_turn = 1
        self.bot_turn = 0

    def __str__(self):
        result = ''
        for row in self.board:
            result += "|"
            for place in row:
                result += " {} |".format(place)
            result += "\n"

        return result

    def place_X(self, row, col):
        self.board[col-1][row-1] = "X"
        self.bot_turn, self.player_turn = self.player_turn, self.bot_turn

    def place_O(self, row, col):
        self.board[col-1][row-1] = "O"
        self.bot_turn, self.player_turn = self.player_turn, self.bot_turn

    def is_free(self, row, col):
        return self.board[col-1][row-1].isspace()

    def is_out(self, row, col):
        return not (row in range(1, 4) and col in range(1, 4))

    def get_available_moves(self, board):
        moves = []
        for row in range(3):
            for place in range(3):
                if board[row][place] == " ":
                    moves.append((place+1, row+1))
        return moves

    def is_over(self):
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
            if self.board[0][0] is "X":
                return self.PLAYER_WINS
            if self.board[0][0] is "O":
                return self.BOT_WINS

        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]:
            if self.board[1][0] is "X":
                return self.PLAYER_WINS
            if self.board[1][0] is "O":
                return self.BOT_WINS

        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]:
            if self.board[2][0] is "X":
                return self.PLAYER_WINS
            if self.board[2][0] is "O":
                return self.BOT_WINS

        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]:
            if self.board[0][0] is "X":
                return self.PLAYER_WINS
            if self.board[0][0] is "O":
                return self.BOT_WINS

        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]:
            if self.board[0][1] is "X":
                return self.PLAYER_WINS
            if self.board[0][1] is "O":
                return self.BOT_WINS

        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]:
            if self.board[0][2] is "X":
                return self.PLAYER_WINS
            if self.board[0][2] is "O":
                return self.BOT_WINS

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if self.board[0][0] is "X":
                return self.PLAYER_WINS
            if self.board[0][0] is "O":
                return self.BOT_WINS

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            if self.board[0][2] is "X":
                return self.PLAYER_WINS
            if self.board[0][2] is "O":
                return self.BOT_WINS

        places = set()
        for row in self.board:
            for place in row:
                places.add(place)

        if ' ' not in places:
            return self.DRAW

        return self.NOT_OVER

    def player_move(self):
        col = input("Insert colomn: ")
        row = input("Insert row: ")
        return int(row), int(col)

    def bot_move(self):
        pass

### magic below
    def minimax(self, board, depth, move=None, main_minimax=False):
        if move is not None:
            if board.bot_turn:
                board.place_O(move[0], move[1])
            else:
                board.place_X(move[0], move[1])

        if board.is_over():
            return board.get_score(depth)

        depth += 1
        scores = []
        for move in board.get_available_moves(board.board):
            copy_board = copy.deepcopy(board)
            scores.append(board.minimax(copy_board, depth, move))

        if not main_minimax:
            if self.bot_turn:
                return min(scores)
            else:
                return max(scores)
        return scores.index(max(scores))

    def get_score(self, depth):
        if self.is_over() is self.PLAYER_WINS:
            return depth - 10
        elif self.is_over() is self.BOT_WINS:
            return 10 - depth
        else:
            return 0

    def get_winner(self):
        if self.is_over() is self.PLAYER_WINS:
            return "Congratz!! You are the winner!!!"
        elif self.is_over() is self.BOT_WINS:
            return "Looooooooser!!!"
        else:
            return "You both suck!!!"


def main():
    asd = Board()
    pro = Player()
    print(asd)
    while not asd.is_over():
        if asd.bot_turn:
            best_turn = asd.minimax(asd, 0, None, True)
            (col, row) = asd.get_available_moves(asd.board)[best_turn]
            asd.place_O(col, row)
        else:
            (col, row) = pro.make_move()
            while asd.is_free(col,row):
                (col, row) = pro.make_move()
            asd.place_X(col, row)
        print(asd)
    print(asd.get_winner())

if __name__ == '__main__':
    main()
