import pygame
import sys

from sudoku_config import *
from sudoku_utils import *

# Initialize Pygame
pygame.init()

# Setup display
screen = pygame.display.set_mode((SIZE, SIZE + 50))
pygame.display.set_caption('Sudoku Solver')

# Font
font = pygame.font.Font(None, 40)

# Create a copy of the original board to track changes
original_board = [row[:] for row in sudoku_board]

# Function to print the Sudoku board in Pygame
def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for x in range(10):
        width = LINE_WIDTH if x % 3 else 3 * LINE_WIDTH
        pygame.draw.line(screen, LINE_COLOR, (x * GRID_SIZE, 0), (x * GRID_SIZE, SIZE), width)
        pygame.draw.line(screen, LINE_COLOR, (0, x * GRID_SIZE), (SIZE, x * GRID_SIZE), width)

    for row in range(9):
        for col in range(9):
            number = board[row][col]
            if number != 0:
                color = SOLVED_COLOR if original_board[row][col] == 0 else TEXT_COLOR
                text = font.render(str(number), True, color)
                screen.blit(text, (col * GRID_SIZE + GRID_SIZE // 3, row * GRID_SIZE + GRID_SIZE // 3))
    
    pygame.display.flip()

# Function to draw the solve button at the bottom-center
def draw_solve_button():
    button_width = 100
    button_height = 30
    button_x = (SIZE - button_width) // 2  # Center the button horizontally
    button_y = SIZE + 10  # 10 pixels below the grid
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    text = font.render('Solve', True, BACKGROUND_COLOR)
    screen.blit(text, (button_rect.x + 10, button_rect.y + 5))
    pygame.display.flip()
    return button_rect

# Function to display "No solution" message
def display_no_solution():
    message = font.render("No solution", True, (255, 255, 255))  # White text
    message_rect = message.get_rect(center=(SIZE // 2, SIZE // 2))  # Center the text
    
    # Create a background rectangle
    background_rect = pygame.Rect(
        message_rect.x - 10,  # Extra padding on left
        message_rect.y - 10,  # Extra padding on top
        message_rect.width + 20,  # Extra padding on right
        message_rect.height + 20  # Extra padding on bottom
    )
    
    # Draw the background (use a color, e.g., red for the background)
    pygame.draw.rect(screen, (255, 0, 0), background_rect)  # Red background
    
    # Draw the "No solution" text on top of the background
    screen.blit(message, message_rect)
    
    pygame.display.flip()


# Main loop
def main():
    clock = pygame.time.Clock()
    draw_board(sudoku_board)
    button_rect = draw_solve_button()
    solving = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    if not solving:
                        solving = True
                        if solve_sudoku(sudoku_board):
                            draw_board(sudoku_board)
                        else:
                            display_no_solution()
                    else:
                        solving = False
        
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
