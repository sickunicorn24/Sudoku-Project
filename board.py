import pygame
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.current = None
        self.original_values = [[cell.value for cell in row] for row in self.cells]

    def draw(self):
        for row in range(10):
            thickness = 2 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, row * 60), (540, row * 60), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (row * 60, 0), (row * 60, 540), thickness)
        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.current:
            self.current.selected = False

        if self.cells[row][col].editable:
            self.cells[row][col].selected = True
            self.current = self.cells[row][col]
        else:
            self.current = None

    def click(self, x, y):
        if x < self.width and y < self.height:
            row = y // 60
            col = x // 60
            self.select(row, col)
            return row, col
        return None

    def clear(self):
        if self.current and self.current.value == 0:
            self.current.set_sketched_value(0)

    def sketch(self, value):
        if self.current and self.current.value == 0:
            self.current.set_sketched_value(value)

    def place_number(self, value):
        if self.current and self.current.value == 0:
            self.current.set_cell_value(value)
            self.current.set_sketched_value(0)

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].editable:
                    self.cells[i][j].set_cell_value(self.original_values[i][j])
                    self.cells[i][j].set_sketched_value(0)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        board = [[cell.value for cell in row] for row in self.cells]
        return board

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        for row in self.cells:
            if not self._is_valid_group([cell.value for cell in row]):
                return False
        for col in range(9):
            if not self._is_valid_group([self.cells[row][col].value for row in range(9)]):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [self.cells[x][y].value for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self._is_valid_group(subgrid):
                    return False
        return True

    def _is_valid_group(self, values):
        nums = [v for v in values if v != 0]
        return len(nums) == len(set(nums))
