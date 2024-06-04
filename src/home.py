import pygame
import sys

class Home:
    def __init__(self, screen, font_path, logo_path, product_name):
        self.screen = screen
        self.font_path = font_path
        self.logo_path = logo_path
        self.product_name = product_name
        self.screen_width, self.screen_height = screen.get_size()

        # Initialize font and logo
        self.initialize_fonts_and_logo()

    def initialize_fonts_and_logo(self):
        # Font setup
        font_size = int(self.screen_width * 0.05)  # Adjust font size based on screen width
        self.font = pygame.font.Font(self.font_path, font_size)
        self.text_surface = self.font.render(self.product_name, True, (255, 255, 255))

        # Logo setup
        logo_size = (int(self.screen_height * 0.09), int(self.screen_height * 0.225))  # Adjust logo size based on screen height
        self.logo = pygame.image.load(self.logo_path)
        self.logo = pygame.transform.scale(self.logo, logo_size)

        # Header bar setup
        self.header_height = int(self.screen_height * 0.25)  # Header bar takes 1/4 of the screen height
        self.header_rect = pygame.Rect(0, 0, self.screen_width, self.header_height)

        # Box setup
        self.num_boxes = 6
        self.box_width = self.screen_width // self.num_boxes
        self.box_height = self.screen_height - self.header_height

    def draw(self):
        # Draw background
        self.screen.fill((255, 255, 255))

        # Draw header bar with gradient
        self.draw_gradient(self.screen, (187, 31, 31), (207, 75, 125), self.header_rect)

        # Draw product name and logo in header bar
        text_rect = self.text_surface.get_rect(center=(self.screen_width // 2, self.header_height // 2))
        logo_rect = self.logo.get_rect(center=(self.screen_width // 3, self.header_height // 2))
        self.screen.blit(self.text_surface, text_rect.topleft)
        self.screen.blit(self.logo, logo_rect.topleft)

        # Calculate box dimensions and margin
        box_width = (self.screen_width - 40) // 3  # Adjusted for margin
        box_height = (self.screen_height - self.header_height - 40) // 2  # Adjusted for margin
        margin_x = (self.screen_width - (box_width * 3)) // 4  # Center the boxes horizontally
        margin_y = 20

        # Draw left border of each box
        for i in range(3):
            for j in range(2):
                box_x = margin_x + i * (box_width + margin_x)
                box_y = self.header_height + margin_y + j * (box_height + margin_y)
                pygame.draw.rect(self.screen, (0, 0, 0), (box_x, box_y, 1, box_height))

        # Draw background
        self.screen.fill((255, 255, 255))

        # Draw header bar with gradient
        self.draw_gradient(self.screen, (187, 31, 31), (207, 75, 125), self.header_rect)

        # Draw product name and logo in header bar
        text_rect = self.text_surface.get_rect(center=(self.screen_width // 2, self.header_height // 2))
        logo_rect = self.logo.get_rect(center=(self.screen_width // 3, self.header_height // 2))
        self.screen.blit(self.text_surface, text_rect.topleft)
        self.screen.blit(self.logo, logo_rect.topleft)

        # Calculate box dimensions and margin
        box_width = (self.screen_width - 40) // 3  # Adjusted for margin
        box_height = (self.screen_height - self.header_height - 40) // 2  # Adjusted for margin
        margin_x = (self.screen_width - (box_width * 3)) // 4  # Center the boxes horizontally
        margin_y = 20

        # Draw 6 boxes in a 3x2 grid with margins
        for i in range(3):
            for j in range(2):
                box_x = margin_x + i * (box_width + margin_x)
                box_y = self.header_height + margin_y + j * (box_height + margin_y)
                box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
                pygame.draw.rect(self.screen, (0, 0, 0), box_rect, 1)


    def draw_gradient(self, surface, color1, color2, rect):
        color_rect = pygame.Surface((2, 2))
        pygame.draw.line(color_rect, color1, (0, 0), (1, 0))
        pygame.draw.line(color_rect, color2, (0, 1), (1, 1))
        color_rect = pygame.transform.smoothscale(color_rect, (rect.width, rect.height))
        surface.blit(color_rect, rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.screen_width, self.screen_height = self.screen.get_size()
                    self.initialize_fonts_and_logo()  # Re-initialize fonts and logo on screen resize

            self.draw()
            pygame.display.flip()

        pygame.quit()
        sys.exit()


