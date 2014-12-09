from player import Player


class Board:
    def __init__(self):
        self.matrix = [[" " for row in range(3)] for col in range(3)]
        self.player_turn = 1
        self.bot_turn = 0

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += "|"
            for place in row:
                result += " {} |".format(place)
            result += "\n"

        return result

    def place_X(self, row, col):
        self.matrix[row-1][col-1] = "X"
        self.change_turn()

    def place_O(self, row, col):
        self.matrix[row-1][col-1] = "O"
        self.change_turn()

    def is_free(self, row, col):
        if not self.is_out(row, col):
            return self.matrix[row-1][col-1].isspace()
        else:
            return False

    def is_out(self, row, col):
        return not (row in range(1, 4) and col in range(1, 4))

    def change_turn(self):
        self.bot_turn, self.player_turn = self.player_turn, self.bot_turn


def main():
    asd = Board()
    pro = Player()
    print(asd)
    while not asd.is_over():
        if asd.bot_turn:
            asd.bot_move()
        else:
            (col, row) = pro.make_move()
            while not asd.is_free(col, row):
                (col, row) = pro.make_move()
            asd.place_X(col, row)
        print(asd)
    print(asd.print_winner())

if __name__ == '__main__':
    main()
