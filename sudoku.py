import pygame
import sys
from board import Board
from constants import *
from sudoku_generator import SudokuGenerator


def game_start(screen):
    # Initialize title, subtitle, and button fonts
    start_title_font = pygame.font.Font(None, 120)
    subtitle_font = pygame.font.Font(None, 90)
    button_font = pygame.font.Font(None, 70)

    # Color background and display title
    screen.fill(BG_COLOR_1)
    main_title_surface = start_title_font.render("Welcome to Sudoku", True, TITLE_TEXT)
    main_title_rectangle = main_title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 300))
    screen.blit(main_title_surface, main_title_rectangle)

    subtitle_surface = subtitle_font.render("Select Game Mode:", True, TITLE_TEXT)
    subtitle_rectangle = subtitle_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(subtitle_surface, subtitle_rectangle)

    # Define buttons
    button_data = [("Easy", WIDTH // 2 + 200), ("Medium", WIDTH // 2), ("Hard", WIDTH // 2 - 200)]
    buttons = []
    for text, x_pos in button_data:
        button_text = button_font.render(text, True, TEXT)
        button_surface = pygame.Surface((button_text.get_width() + 20, button_text.get_height() + 20))
        button_surface.fill(BUTTON_COLOR)
        button_surface.blit(button_text, (10, 10))
        button_rectangle = button_surface.get_rect(center=(x_pos, HEIGHT // 2 + 150))
        buttons.append((button_surface, button_rectangle, text.lower()))
        screen.blit(button_surface, button_rectangle)

    # Wait for user to select difficulty
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
    # Init Fonts
    bottom_button_font = pygame.font.Font(None, 50)
    small_msg_font = pygame.font.Font(None, 30)

    # Init small message that displays the difficulty
    small_msg_surface = small_msg_font.render(difficulty, 0, TEXT)
    small_msg_rectangle = small_msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(small_msg_surface, small_msg_rectangle)

    # Text displays for the RESET/RESTART/EXIT buttons
    reset_text = bottom_button_font.render("RESET", 0, TEXT)
    restart_text = bottom_button_font.render("RESTART", 0, TEXT)
    exit_text = bottom_button_font.render("EXIT", 0, TEXT)

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(BUTTON_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT - 150))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 150))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 - 200, HEIGHT - 150))

    clicked_row, clicked_col = -1, -1

    while True:
        screen.fill(BG_COLOR_1)
        display_board.draw()
        if clicked_row != -1 and clicked_col != -1:
            display_board.select(clicked_row, clicked_col)
        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        # Event handling
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

                # Handle board clicks (select the cell)
                if 0 <= event.pos[0] < 540 and 0 <= event.pos[1] < 540:
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

                    # Skip non-editable cells when navigating
                    while not display_board.cells[clicked_row][clicked_col].editable:
                        # Logic to prevent getting stuck on non-editable cells
                        if event.key in (pygame.K_UP, pygame.K_DOWN):
                            clicked_row = (clicked_row - 1) % 9 if event.key == pygame.K_UP else (clicked_row + 1) % 9
                        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                            clicked_col = (clicked_col - 1) % 9 if event.key == pygame.K_LEFT else (clicked_col + 1) % 9

        pygame.display.update()

def draw_game_win(screen):
    win_font = pygame.font.Font(None, 120)
    button_font = pygame.font.Font(None, 50)

    # Set background and text
    screen.fill(BG_COLOR_1)
    win_surface = win_font.render("Game Won!", True, WIN_BG)
    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(win_surface, win_rectangle)

    # Display exit button
    exit_text = button_font.render("EXIT", True, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_width() + 20, exit_text.get_height() + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    screen.blit(exit_surface, exit_rectangle)

    # Handle button clicks for exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


def draw_game_lose(screen):
    lose_font = pygame.font.Font(None, 120)
    button_font = pygame.font.Font(None, 50)

    # Set background and text
    screen.fill(BG_COLOR_1)
    lose_surface = lose_font.render("Game Over :(", True, LOSE_BG)
    lose_rectangle = lose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(lose_surface, lose_rectangle)

    # Display restart button
    restart_text = button_font.render("RESTART", True, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_width() + 20, restart_text.get_height() + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    screen.blit(restart_surface, restart_rectangle)

    # Handle button clicks for restart
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    main()
        pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    # Get the difficulty from the game start screen
    difficulty = game_start(screen)

    # Board generation based on difficulty
    removed_cells = {"easy": 30, "medium": 40, "hard": 50}
    sudoku = SudokuGenerator(9, removed_cells[difficulty])
    sudoku.fill_values()
    sudoku.remove_cells()
    board_state = sudoku.get_board()

    # Fill the screen with background color to clear the starting screen
    screen.fill(BG_COLOR_1)

    # Initialize board display (this is where we create the display_board)
    display_board = Board(630, 630, screen, removed_cells[difficulty])  # Ensure Board is initialized here
    for i in range(9):
        for j in range(9):
            display_board.cells[i][j].value = board_state[i][j]
            if board_state[i][j] != 0:
                display_board.cells[i][j].editable = False

    # Start the game
    display_board.draw()  # Draw the board initially
    during_game(screen, display_board, difficulty)  # Pass display_board to during_game

if __name__ == "__main__":
    main()