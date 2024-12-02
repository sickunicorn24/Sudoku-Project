class Board:
    def __init__(self, row_length=9):
        self.row_length = row_length
        self.board = [[0] * row_length for _ in range(row_length)]

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) if cell != 0 else '.' for cell in row))

    def update_cell(self, row, col, num):
        if 1 <= num <= 9 and self.board[row][col] == 0:
            self.board[row][col] = num
            return True
        return False

    def is_solved(self):
        for row in self.board:
            if 0 in row:
                return False
        return True
