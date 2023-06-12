import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1200, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reflective Walls")

# Load ball image
ball_image = pygame.image.load("ball.png")
ball_image = pygame.transform.scale(ball_image, (50, 50))  # Resize image

# Ball properties
ball_rect = ball_image.get_rect()
ball_radius = ball_rect.width // 2
ball_x = 0
ball_y = screen_height // 2

# Sine wave properties
amplitude = 200
frequency = 0.02

x=screen_width // 2
q=1

# Rotation angle
angle = 0

# Walls position
wall_left = 50
wall_right = screen_width 

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill('green')
    for a in range(screen_width):
        b = amplitude * math.sin(frequency * a) + screen_height // 2
        pygame.draw.circle(screen, (0, 0, 255), (a, b), 4)
    # Draw x and y coordinate lines
    pygame.draw.line(screen, (0, 0, 0), (0, screen_height // 2), (screen_width, screen_height // 2), 1)
    pygame.draw.line(screen, (0, 0, 0), (screen_width // 2, 0), (screen_width // 2, screen_height), 1)

    # Draw walls
    pygame.draw.line(screen, 'brown', ( 0, 0),(0, screen_height ), 50)
    pygame.draw.line(screen, 'brown', (screen_width, 0),(screen_width, screen_height ), 50)

    # Draw sine wave
    x=x+q*2
    #for x in range(screen_width):
    y = amplitude * math.sin(frequency * x) + screen_height // 2
    pygame.draw.circle(screen, 'blue', (x, y), 2)
    
    # Calculate ball position along the sine wave
    ball_x=x
    ball_y = amplitude * math.sin(frequency * ball_x) + screen_height // 2

    # Check for wall collisions

    if ball_x >= wall_right-40 or ball_x <= wall_left-20:
        q=q*-1

    # Rotate the ball image
    rotated_image = pygame.transform.rotate(ball_image, angle)
    rotated_rect = rotated_image.get_rect(center=(ball_x, ball_y))

    # Draw the rotated ball image
    screen.blit(rotated_image, rotated_rect)

    # Update the rotation angle
    angle -= 5

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()