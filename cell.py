import pygame
from constants import TEXT

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

        # Only display number if the cell value is not 0
        if self.value != 0:
            num_surface = font_num.render(str(self.value), True, TEXT)
            num_rectangle = num_surface.get_rect(
                center=(60 * self.col + 30, 60 * self.row + 30))
            self.screen.blit(num_surface, num_rectangle)

        # Highlight the cell if it's selected
        if self.selected:
            red_square = pygame.Rect(self.col * 60, self.row * 60, 60, 60)
            pygame.draw.rect(self.screen, (255, 0, 0), red_square, 3)  # Red outline with 3 px thickness

        # If the cell has a sketch value, display it
        if self.sketched_val is not None:
            font_sketch = pygame.font.Font(None, 40)
            sketch_surface = font_sketch.render(str(self.sketched_val), True, TEXT)
            sketch_rectangle = sketch_surface.get_rect(
                center=(60 * self.col + 30, 60 * self.row + 30))
            self.screen.blit(sketch_surface, sketch_rectangle)