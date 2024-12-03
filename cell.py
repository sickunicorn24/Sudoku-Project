import pygame

class Cell:
    def __init__(self, value, row, col, screen, size=60):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.size = size
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * self.size
        y = self.row * self.size

        color = (255, 0, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(self.screen, color, (x, y, self.size, self.size), 2)

        font = pygame.font.Font(None, 40)

        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + self.size // 3, y + self.size // 4))
        elif self.sketched_value != 0:
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))
