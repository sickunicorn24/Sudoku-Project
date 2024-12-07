import pygame
import sys
from board import Board
from constants import *
from sudoku_generator import SudokuGenerator


def game_start(screen):
    #Initialize Font
    start_title_font = pygame.font.Font(None, 130)
    subtitle_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 90)

    title_board = SudokuGenerator(9,35)
    title_board.fill_values()
    title_board.remove_cells()
    disp = title_board.get_board()

    display_board = Board(100, 100, screen, 0)
    for i in range(9):
        for j in range(9):
            display_board.cells[i][j].value = disp[i][j]
            if disp[i][j] != 0:
                display_board.cells[i][j].editable = False




    #Main title text
    screen.fill(PINK)
    display_board.draw()
    main_title_surface = start_title_font.render("Welcome to Sudoku", True, PURPLE)
    main_title_rectangle = main_title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 300))
    screen.blit(main_title_surface, main_title_rectangle)

    #Subtitle text
    subtitle_surface = subtitle_font.render("Select Game Mode", True, PURPLE)
    subtitle_rectangle = subtitle_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(subtitle_surface, subtitle_rectangle)

    #Outline setup
    main_title_outline = start_title_font.render("Welcome to Sudoku", 0, WHITE)
    for i in range(-4, 5):
        for j in range(-4, 5):
            screen.blit(main_title_outline, main_title_surface.get_rect(center=(WIDTH // 2 + i, HEIGHT // 2 - 300 + j)))
    screen.blit(main_title_surface, main_title_rectangle)
    subtitle_outline = subtitle_font.render("Select Game Mode", 0, WHITE)
    for i in range(-4, 5):
        for j in range(-4, 5):
            screen.blit(subtitle_outline, subtitle_surface.get_rect(center=(WIDTH // 2 + i, HEIGHT // 2 - 50 + j)))
    screen.blit(subtitle_surface, subtitle_rectangle)

    #Main menu buttons
    button_data = [("Easy", WIDTH // 2 + 270), ("Medium", WIDTH // 2), ("Hard", WIDTH // 2 - 270)]
    buttons = []

    for text, x_pos in button_data:
        button_text = button_font.render(text, True, WHITE)
        button_surface = pygame.Surface((button_text.get_width() + 20, button_text.get_height() + 20))
        button_surface.fill(PURPLE)
        button_surface.blit(button_text, (10, 10))
        button_rectangle = button_surface.get_rect(center=(x_pos, HEIGHT // 2 + 150))
        buttons.append((button_surface, button_rectangle, text.lower()))
        button_ot_surface = pygame.Surface((button_text.get_width() + 30, button_text.get_height() + 30))
        button_ot_surface.fill(BLACK)
        screen.blit(button_ot_surface, button_rectangle)
        screen.blit(button_surface, button_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for _, button_rect, difficulty in buttons:
                    if button_rect.collidepoint(event.pos):
                        return difficulty
        pygame.display.update()

def during_game(screen, display_board, difficulty):

    #Font
    bottom_button_font = pygame.font.Font(None, 50)
    small_msg_font = pygame.font.Font(None, 40)

    #Difficulty text
    difficulty = difficulty.upper()
    small_msg_surface = small_msg_font.render(difficulty, 0, BLACK)
    small_msg_rectangle = small_msg_surface.get_rect(center=(WIDTH // 2 - 370, HEIGHT // 2 + 420))

    #Init text
    reset_text = bottom_button_font.render("RESET", 0, BLACK)
    restart_text = bottom_button_font.render("RESTART", 0, BLACK)
    exit_text = bottom_button_font.render("EXIT", 0, BLACK)

    #Init reset button
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(PINK)
    reset_surface.blit(reset_text, (10, 10))

    #Init restart button
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(PINK)
    restart_surface.blit(restart_text, (10, 10))

    #Init exit button
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(PINK)
    exit_surface.blit(exit_text, (10, 10))

    #Set button locations
    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT - 50))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 - 200, HEIGHT - 50))

    #Outline setup
    reset_ot_surface = pygame.Surface((reset_text.get_size()[0] + 30, reset_text.get_size()[1] + 30))
    reset_ot_surface.fill(BLACK)
    restart_ot_surface = pygame.Surface((restart_text.get_size()[0] + 30, restart_text.get_size()[1] + 30))
    restart_ot_surface.fill(BLACK)
    exit_ot_surface = pygame.Surface((exit_text.get_size()[0] + 30, exit_text.get_size()[1] + 30))
    exit_ot_surface.fill(BLACK)



    clicked_row, clicked_col = -1, -1

    while True:
        screen.fill(PURPLE)
        display_board.draw()

        if clicked_row != -1 and clicked_col != -1:
            display_board.select(clicked_row, clicked_col)
        screen.blit(reset_ot_surface, reset_rectangle)
        screen.blit(restart_ot_surface, restart_rectangle)
        screen.blit(exit_ot_surface, exit_rectangle)
        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)
        screen.blit(small_msg_surface, small_msg_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rectangle.collidepoint(event.pos):
                    display_board.reset_to_original()
                    display_board.draw()
                elif restart_rectangle.collidepoint(event.pos):
                    main()
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()

                if 0 <= event.pos[0] < WIDTH and 0 <= event.pos[1] < WIDTH:
                    row, col = display_board.click(event.pos[0], event.pos[1])
                    if display_board.cells[row][col].editable:
                        clicked_row, clicked_col = row, col
                    else:
                        clicked_row, clicked_col = -1, -1

            if event.type == pygame.KEYDOWN:
                if clicked_row != -1 and clicked_col != -1:
                    if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                     pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                        value = int(event.unicode)
                        if display_board.cells[clicked_row][clicked_col].editable:
                            display_board.cells[clicked_row][clicked_col].value = value
                    elif event.key == pygame.K_UP:
                        clicked_row = (clicked_row - 1) % 9
                    elif event.key == pygame.K_DOWN:
                        clicked_row = (clicked_row + 1) % 9
                    elif event.key == pygame.K_LEFT:
                        clicked_col = (clicked_col - 1) % 9
                    elif event.key == pygame.K_RIGHT:
                        clicked_col = (clicked_col + 1) % 9
                    while not display_board.cells[clicked_row][clicked_col].editable:
                        if event.key in (pygame.K_UP, pygame.K_DOWN):
                            clicked_row = (clicked_row - 1) % 9 if event.key == pygame.K_UP else (clicked_row + 1) % 9
                        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                            clicked_col = (clicked_col - 1) % 9 if event.key == pygame.K_LEFT else (clicked_col + 1) % 9
                if display_board.is_full():
                    if display_board.check_board():
                        draw_game_win(screen)
                    else:
                        draw_game_lose(screen)
        pygame.display.update()

def draw_game_win(screen):
    win_font = pygame.font.Font(None, 200)
    try_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 80)
    screen.fill(BLACK)
    color = WHITE
    b_color = WHITE
    b_color2 = b_color
    x_pos1 = 200
    x_pos2 = 70
    b_size = 50

    for i in range(5):
        if i == 0:
            color = GREEN
            b_color = WHITE
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
        elif i == 1:
            color = PURPLE
            b_color = WHITE
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
            b_size -= 10
        elif i == 2:
            color = PINK
            b_color = BLACK
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
        elif i == 3:
            color = RED
            b_color = BLACK
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
            b_size -= 10
        elif i == 4:
            b_color = RED
            b_color2 = GREEN
            color = WHITE
            x_pos1 += 5
            x_pos2 += 5
            b_size -= 10

        win_surface = win_font.render("YOU", True, color)
        win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - x_pos1))
        screen.blit(win_surface, win_rectangle)

        yw_surface = win_font.render("WIN!", 0, color)
        yw_rectangle = yw_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - x_pos2))
        screen.blit(yw_surface, yw_rectangle)

        try_surface = try_font.render("PLAY AGAIN?", True, GREEN)
        try_rectangle = try_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(try_surface, try_rectangle)

        restart_text = button_font.render("YES", True, BLACK)
        restart_surface = pygame.Surface((restart_text.get_width() + b_size, restart_text.get_height() + b_size))
        restart_surface.fill(b_color2)
        restart_surface.blit(restart_text, (10, 10))
        restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 200))
        exit_text = button_font.render("NO", True, BLACK)
        exit_surface = pygame.Surface((exit_text.get_width() + b_size, exit_text.get_height() + b_size))
        exit_surface.fill(b_color)
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 + 200))
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    main()
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


def draw_game_lose(screen):
    lose_font = pygame.font.Font(None, 200)
    try_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 80)
    screen.fill(BLACK)
    color = WHITE
    b_color = WHITE
    b_color2 = b_color
    x_pos1 = 200
    x_pos2 = 70
    b_size = 50

    for i in range(5):
        if i == 0:
            color = GREEN
            b_color = WHITE
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
        elif i == 1:
            color = PURPLE
            b_color = WHITE
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
            b_size -= 10
        elif i == 2:
            color = PINK
            b_color = BLACK
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
        elif i == 3:
            color = RED
            b_color = BLACK
            b_color2 = b_color
            x_pos1 += 5
            x_pos2 += 5
            b_size -= 10
        elif i == 4:
            b_color = RED
            b_color2 = GREEN
            color = WHITE
            x_pos1 += 5
            x_pos2 += 5
            b_size -= 10

        lose_surface = lose_font.render("YOU", True, color)
        lose_rectangle = lose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - x_pos1))
        screen.blit(lose_surface, lose_rectangle)

        yl_surface = lose_font.render("LOSE!", 0, color)
        yl_rectangle = yl_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - x_pos2))
        screen.blit(yl_surface, yl_rectangle)

        try_surface = try_font.render("TRY AGAIN?", True, RED)
        try_rectangle = try_surface.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(try_surface, try_rectangle)

        restart_text = button_font.render("YES", True, BLACK)
        restart_surface = pygame.Surface((restart_text.get_width() + b_size, restart_text.get_height() + b_size))
        restart_surface.fill(b_color2)
        restart_surface.blit(restart_text, (10, 10))
        restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 200))
        exit_text = button_font.render("NO", True, BLACK)
        exit_surface = pygame.Surface((exit_text.get_width() + b_size, exit_text.get_height() + b_size))
        exit_surface.fill(b_color)
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 + 200))
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    main()
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()






def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    difficulty = game_start(screen)


    removed_cells = {"easy": 30, "medium": 40, "hard": 50}
    sudoku = SudokuGenerator(9, removed_cells[difficulty])
    sudoku.fill_values()
    sudoku.remove_cells()
    board_state = sudoku.get_board()

    display_board = Board(WIDTH, WIDTH, screen, removed_cells[difficulty])
    for i in range(9):
        for j in range(9):
            display_board.cells[i][j].value = board_state[i][j]
            if board_state[i][j] != 0:
                display_board.cells[i][j].editable = False

    display_board.draw()
    during_game(screen, display_board, difficulty)

if __name__ == "__main__":
    main()