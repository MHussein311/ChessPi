import pygame
import sys
from splash_screen import SplashScreen
from home import Home

# Initialize Pygame
pygame.init()

# Initial screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("ChessPi")

# Colors
white = (255, 255, 255)

# Font and logo setup
font_path = "../assets/font.ttf"
logo_path = "../assets/logo.png"

# Create SplashScreen instance
splash_screen = SplashScreen(screen, font_path, logo_path)

# Create home instance
product_name = "ChessPi"
home = Home(screen, font_path, logo_path, product_name)

# Main loop variables
frame_count = 0
running = True
animation_done = False  # Variable to track if splash screen animation is done

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    screen.fill(white)

    if not animation_done:
        # Run splash screen animation
        animation_done = splash_screen.run()  # Returns True when animation is complete
    else:
        # Display home
        home.run()

    pygame.display.flip()
    pygame.time.delay(30)  # Approximately 30 frames per second

pygame.quit()
sys.exit()
