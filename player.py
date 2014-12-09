class Player:

    def __init__(self):
        pass

    def make_move(self):
        row = input("Insert row: ")
        col = input("Insert colomn ")
        return int(row), int(col)
