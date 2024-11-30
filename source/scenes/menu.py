import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life - Start Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Font
font = pygame.font.Font(None, 50)

# Button dimensions
button_width = 200
button_height = 60
start_button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 - 100), (button_width, button_height))
exit_button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 + 50), (button_width, button_height))

# Render text
def render_text(text, font, color):
    return font.render(text, True, color)

# Main menu loop
def main_menu():
    while True:
        screen.fill(WHITE)

        # Draw buttons
        pygame.draw.rect(screen, GRAY, start_button_rect)
        pygame.draw.rect(screen, GRAY, exit_button_rect)

        # Highlight buttons on hover
        mouse_pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, DARK_GRAY, start_button_rect)
        if exit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, DARK_GRAY, exit_button_rect)

        # Button labels
        start_text = render_text("Start", font, BLACK)
        exit_text = render_text("Exit", font, BLACK)
        screen.blit(start_text, (start_button_rect.centerx - start_text.get_width() // 2, start_button_rect.centery - start_text.get_height() // 2))
        screen.blit(exit_text, (exit_button_rect.centerx - exit_text.get_width() // 2, exit_button_rect.centery - exit_text.get_height() // 2))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                if start_button_rect.collidepoint(event.pos):
                    print("Start Game!")
                    # Transition to the game logic here
                    return
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Update display
        pygame.display.flip()

# Run main menu
main_menu()