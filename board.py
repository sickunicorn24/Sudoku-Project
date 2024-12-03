import pygame
from cell import Cell
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        self.selected_cell = None
        self.generate_board()
    def generate_board(self):
        board_values = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            cell_row = []
            for col in range(9):
                cell_row.append(Cell(board_values[row][col], row, col, self.screen))
            self.cells.append(cell_row)
    def draw(self):
        for row in range(10):
            thickness = 2 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, row * 60), (540, row * 60), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (row * 60, 0), (row * 60, 540), thickness)
        for row in self.cells:
            for cell in row:
                cell.draw()
    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True
    def click(self, x, y):
        if x < self.width and y < self.height:
            row, col = y // 60, x // 60
            self.select(row, col)
            return row, col
        return None
    def clear(self):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(0)
    def sketch(self, value):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(value)
    def place_number(self, value):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_cell_value(value)
            self.selected_cell.set_sketched_value(0)
    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    cell.set_cell_value(0)
                    cell.set_sketched_value(0)
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
        pass