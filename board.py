import pygame
from cell import Cell
from constants import*

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.current = None

    def draw(self):
        for row in range(10):
            thickness = 2 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, row * 60), (540, row * 60), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (row * 60, 0), (row * 60, 540), thickness)
        for row in self.cells:
            for cell in row:
                cell.draw()  # Draw each cell, and highlight the selected one

    def select(self, row, col):
        # Deselect any previously selected cell before selecting a new one
        if self.current:
            self.current.selected = False  # Unselect the previously selected cell

        self.cells[row][col].selected = True  # Select the new cell
        self.current = self.cells[row][col]  # Update the current selected cell

    def click(self, x, y):
        """
        Converts mouse click position (x, y) into a row and column, and selects the corresponding cell.
        """
        if x < self.width and y < self.height:
            # Calculate row and column based on click position
            row = y // 60  # Calculate the row (divide y by the cell height)
            col = x // 60  # Calculate the column (divide x by the cell width)

            # Select the clicked cell
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