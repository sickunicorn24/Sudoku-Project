import pygame, sys
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
                    return
                elif medium_rectangle.collidepoint(event.pos):
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()



def main ():
    game_over = False

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Prog 1 Sudoku")

    difficulty = game_start(screen)
    board = SudokuGenerator(9, difficulty)

    #board.print_board()
    #For debugging ^


if __name__ == "__main__":
    main()
