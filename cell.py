import pygame
from constants import *

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_val = None
        self.editable = True

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font_num = pygame.font.Font(None, 80)
        if self.value != 0:
            num_surface = font_num.render(str(self.value), True, BLACK)
            num_rectangle = num_surface.get_rect(
                center=(100 * self.col + 50, 100 * self.row + 50))
            self.screen.blit(num_surface, num_rectangle)
        if self.selected:
            red_square = pygame.Rect(self.col * 100, self.row * 100, 100, 100)
            pygame.draw.rect(self.screen, (255, 0, 0), red_square, 3)  # Red outline with 3 px thickness
        if self.sketched_val is not None:
            font_sketch = pygame.font.Font(None, 40)
            sketch_surface = font_sketch.render(str(self.sketched_val), True, BLACK)
            sketch_rectangle = sketch_surface.get_rect(
                center=(100 * self.col + 50, 100 * self.row + 50))
            self.screen.blit(sketch_surface, sketch_rectangle)