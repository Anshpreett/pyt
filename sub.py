import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
PLAYER_COLOR = (255, 0, 0)
OBSTACLE_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subway Surfers")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player position
player_x = WIDTH // 2
player_y = HEIGHT - PLAYER_SIZE * 2

# Obstacles list
obstacles = []

# Score
score = 0

# Font for displaying score
font = pygame.font.Font(None, 36)

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(window, PLAYER_COLOR, (x, y, PLAYER_SIZE, PLAYER_SIZE))

# Function to draw an obstacle
def draw_obstacle(x, y):
    pygame.draw.rect(window, OBSTACLE_COLOR, (x, y, OBSTACLE_SIZE, OBSTACLE_SIZE))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += 5

    # Add obstacles randomly
    if random.randint(0, 100) < 5:
        obstacle_x = random.randint(0, WIDTH - OBSTACLE_SIZE)
        obstacle_y = -OBSTACLE_SIZE
        obstacles.append((obstacle_x, obstacle_y))

    # Update obstacle positions
    for i in range(len(obstacles)):
        obstacles[i] = (obstacles[i][0], obstacles[i][1] + 5)

        # Check for collisions with player
        if (
            player_x < obstacles[i][0] < player_x + PLAYER_SIZE
            and player_y < obstacles[i][1] < player_y + PLAYER_SIZE
        ):
            pygame.quit()
            sys.exit()

        # Remove obstacles that are off-screen
        if obstacles[i][1] > HEIGHT:
            obstacles.pop(i)
            score += 1

    # Draw background
    window.fill(BACKGROUND_COLOR)

    # Draw player
    draw_player(player_x, player_y)

    # Draw obstacles
    for obstacle in obstacles:
        draw_obstacle(obstacle[0], obstacle[1])

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)