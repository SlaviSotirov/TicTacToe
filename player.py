class Player:

    def __init__(self):
        pass

    def make_move(self):
        col = input("Insert colomn: ")
        row = input("Insert row: ")
        return int(row), int(col)

