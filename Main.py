import pygame
import random

# Constants
WIDTH = 640
HEIGHT = 480
GRID_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Initialize the game state
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (0, 1)
food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
game_over = False


def update_game():
    global snake, direction, food, game_over

    # Get the current head position
    head = snake[0]

    # Get the new head position based on the current direction
    new_head = (head[0] + direction[0] * GRID_SIZE, head[1] + direction[1] * GRID_SIZE)

    # Check if the new head position is out of bounds or hits the snake's body
    if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
    ):
        game_over = True
        return

    # Update the snake's position
    snake.insert(0, new_head)

    # Check if the snake eats the food
    if new_head == food:
        # Generate new food position
        food = (
        random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        # Remove the tail segment
        snake.pop()


def render_game():
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw the food
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()


# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)

    # Update the game state
    update_game()

    # Render the game
    render_game()

    # Delay to control the game speed
    clock.tick(10)

# Quit Pygame
pygame.quit()
