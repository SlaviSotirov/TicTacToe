class Player:

    def __init__(self):
        pass

    def make_move(self):
        col = input("Insert row: ")
        row = input("Insert colomn ")
        return int(row), int(col)

