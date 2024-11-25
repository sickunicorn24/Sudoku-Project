import pygame, sys
from constants import *
from sudoku_generator import *

def game_start(screen):
    #Title/Button font init
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    #Background coloring
    screen.fill(BG_COLOR_1)

    #Creating title text
    title_surface = start_title_font.render("Welcome to Sudoku", 0, TITLE_TEXT)
    title_rectangle = title_surface.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    #Init Button
    start_text = button_font.render("Start", 0, BUTTON_TEXT)
    quit_text = button_font.render("Quit", 0, BUTTON_TEXT)

    #Init START/QUIT Button Text Box Background
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    start_surface.fill(BUTTON_COLOR)
    start_surface.blit(start_text, (10, 10))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(BUTTON_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    #Init Button Rectangle
    start_rectangle = start_surface.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 50))
    quit_rectangle = quit_surface.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 150))

    #Draw Buttons
    screen.blit(start_surface, start_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    return
                elif quit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()



def main ():
    game_over  = False

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Prog 1 Sudoku")

    game_start(screen)


if __name__ == "__main__":
    main()
