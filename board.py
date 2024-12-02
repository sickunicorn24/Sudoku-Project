import pygame
from cell import Cell


class Board:

    def __init__(self, width, height, screen, difficulty):

        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.select_cell = (0,0)
        self.grid = []

        for x in range(0,9):
            self.grid.append([0] * 9)

        self.cells = []

        for i in range(0,9):
            cells_row = []
            for j in range(0,9):

                cells_row.append(Cell(0, i, j, self.screen))

            self.cells.append(cells_row)

    def draw(self):

        for x in range(0,10):

            width = 1

            if x % 3 == 0:
                width = 3

            pygame.draw.line(self.screen, (0,0,0), (0, x * self.height // 9), (self.width, x * self.height // 9), width)
            pygame.draw.line(self.screen, (0,0,0), (x * self.width // 9, 0), (x * self.width // 9, self.height), width)

        for x in self.cells:
            for y in x:
                y.draw()

    def select(self, row, col):

        self.select_cell = (row,col)

    def click(self, row, col):

        if  (row < self.width and row >=0 ) and (col < self.height and col >= 0):
            i = row // (self.height // 9)
            j = col // (self.width // 9)
            return i, j
        else:
            return None

    def clear(self):

        r, c = self.select_cell

        if self.grid[r][c] == 0:
            self.cells[r][c].set_cell_value(0)
            self.cells[r][c].set_sketched_value(0)

    def sketch(self, value):

        r,c = self.select_cell

        if self.grid[r][c] == 0:
            self.cells[r][c].set_sketched_value(value)

    def place_number(self, value):

        r,c = self.select_cell

        #for event in pygame.event.get():

           # if event.type == pygame.KEYDOWN:

              #  if event.key == pygame.K_RETURN:
        self.cells[r][c].set_cell_value(value)
        self.cells[r][c].set_sketched_value(value)

    def reset_to_original(self):

        for x in range(0,9):
            for y in range(0,9):

                self.cells[x][y].set_cell_value(self.grid[x][y])
                self.cells[x][y].set_sketched_value(0)

    def is_full(self):

        for x in self.cells:
            for y in x:
                if y.value == 0:
                    return False

        return True

    def update_board(self):

        for i in range(0,9):
            for j in range(0,9):
                self.grid[i][j] = self.cells[i][j].value

    def find_empty(self):

        for x in range(0,9):
            for y in range(0,9):
                if self.cells[x][y].value == 0:
                    return x,y

    def check_board(self):

        for x in range(0,9):
            values1 = []
            for y in range(0,9):
                values1.append(self.cells[x][y].value)
            if sorted(values1) != list(range(1,10)):
                return False

        for i in range(0,9):
            values2 = []
            for j in range(0,9):
                values2.append(self.cells[j][i].value)
            if sorted(values2)!= list(range(1,10)):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                threebox = []
                for x in range(0,3):
                    for y in range(0,3):
                        threebox.append(self.cells[row + x][col + y].value)
                if sorted(threebox) != list(range(1, 10)):
                    return False

        return True







