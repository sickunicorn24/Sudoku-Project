from idlelib.pyshell import restart_line
from sys import displayhook

import pygame, sys
from pygame.display import update

from constants import *
from sudoku_generator import *

def game_start(screen):
    #Title/Button font init
    start_title_font = pygame.font.Font(None, 100)
    subtitle_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 70)
    
    #Background coloring
    screen.fill(BG_COLOR_1)

    #Creating title text
    main_title_surface = start_title_font.render("Welcome to Sudoku", 0, TITLE_TEXT)
    main_title_rectangle = main_title_surface.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 300))
    screen.blit(main_title_surface, main_title_rectangle)
    subtitle_surface = subtitle_font.render("Select Game Mode:", 0, TITLE_TEXT)
    subtitle_rectangle = subtitle_surface.get_rect(center = (WIDTH // 2 , HEIGHT // 2 - 50))
    screen.blit(subtitle_surface, subtitle_rectangle)

    #Init Buttons
    easy_text = button_font.render("Easy", 0, BUTTON_TEXT)
    medium_text = button_font.render("Medium", 0, BUTTON_TEXT)
    hard_text = button_font.render("Hard", 0, BUTTON_TEXT)

    #Init Easy/Medium/Hard Button Text Box Background
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (10, 10))


    #Init Button Rectangle
    easy_rectangle = easy_surface.get_rect(center = (WIDTH // 2 + 200 , HEIGHT // 2 + 150))
    medium_rectangle = medium_surface.get_rect(center = (WIDTH // 2 , HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(center = (WIDTH // 2 - 200, HEIGHT // 2 + 150))

    #Draw Buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return EASY
                elif medium_rectangle.collidepoint(event.pos):
                    return MEDIUM
                elif hard_rectangle.collidepoint(event.pos):
                    return HARD
        pygame.display.update()

def during_game(screen, difficulty):
    #Init Fonts
    bottom_button_font = pygame.font.Font(None, 50)
    small_msg_font = pygame.font.Font(None, 30)

    # BG color
    screen.fill(BG_COLOR_2)
    
    #Init small message that displays the difficulty
    small_msg_surface = small_msg_font.render(difficulty, 0, TEXT)
    small_msg_rectangle = small_msg_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(small_msg_surface, small_msg_rectangle)


    #Text displays for the RESET/RESTART/EXIT buttons
    reset_text = bottom_button_font.render("RESET", 0, TEXT)
    restart_text = bottom_button_font.render("RESTART", 0, TEXT)
    exit_text = bottom_button_font.render("EXIT", 0, TEXT)

    #
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(BUTTON_COLOR)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    #
    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT - 150))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 150))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 - 200, HEIGHT - 150))

    #
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rectangle.collidepoint(event.pos):
                    return
                elif restart_rectangle.collidepoint(event.pos):
                    return
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()
    


def main ():
    game_over = False
    dif = ""

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Prog 1 Sudoku")

    difficulty = game_start(screen)
    board = SudokuGenerator(9, difficulty)
    if difficulty == 30:
        dif = "EASY"
    elif difficulty == 40:
        dif = "MEDIUM"
    elif difficulty == 50:
        dif = "HARD"
    screen.fill(BG_COLOR_1)
    during_game(screen, dif)

    #board.print_board()
    #For debugging ^


if __name__ == "__main__":
    main()
