import pygame

class SplashScreen:
    def __init__(self, screen, font_path, logo_path):
        self.screen = screen
        self.font_path = font_path
        self.logo_path = logo_path
        self.screen_width, self.screen_height = screen.get_size()
        self.frame_count = 0
        self.animation_done = False
        self.white = (255, 255, 255)
        self.color1 = pygame.Color("#bb1f1f")
        self.color2 = pygame.Color("#cf4b7d")
        self.font_size = 72

        self.font = pygame.font.Font(font_path, self.font_size)
        self.text_surface = self.font.render("ChessPi", True, self.white)

        self.logo = pygame.image.load(logo_path)
        self.logo = pygame.transform.scale(self.logo, (160, 400))

        self.center_elements()

    def center_elements(self):
        self.logo_rect = self.logo.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        self.text_rect = self.text_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + self.logo.get_height() // 2))

    def draw_gradient(self, surface, color1, color2, rect):
        color_rect = pygame.Surface((2, 2))
        pygame.draw.line(color_rect, color1, (0, 0), (1, 0))
        pygame.draw.line(color_rect, color2, (0, 1), (1, 1))
        color_rect = pygame.transform.smoothscale(color_rect, (rect.width, rect.height))
        surface.blit(color_rect, rect)

    def update(self):
        self.screen.fill(self.white)
        
        if not self.animation_done:
            if self.frame_count < 120:
                # Fade in animation
                alpha = min(255, (self.frame_count / 120) * 255)
                self.logo.set_alpha(alpha)
                self.text_surface.set_alpha(alpha)
                self.draw_gradient(self.screen, self.color1, self.color2, self.screen.get_rect())
                self.screen.blit(self.logo, self.logo_rect.topleft)
                self.screen.blit(self.text_surface, self.text_rect.topleft)
            elif 120 <= self.frame_count < 130:
                # Waiting period
                self.draw_gradient(self.screen, self.color1, self.color2, self.screen.get_rect())
                self.screen.blit(self.logo, self.logo_rect.topleft)
                self.screen.blit(self.text_surface, self.text_rect.topleft)
            elif 130 <= self.frame_count < 190:
                # Slide up and fade out animation
                progress = (self.frame_count - 130) / 60.0
                alpha = min(255, 255 - (255 * progress))
                fade_color = self.color1.lerp(self.white, progress)
                self.draw_gradient(self.screen, fade_color, self.white, self.screen.get_rect())
                self.logo.set_alpha(alpha)
                self.text_surface.set_alpha(alpha)
                self.logo_rect.y -= 2  # Move up 2 pixels per frame
                self.text_rect.y -= 2
                self.screen.blit(self.logo, self.logo_rect.topleft)
                self.screen.blit(self.text_surface, self.text_rect.topleft)
            else:
                self.animation_done = True  # Animation is done

            self.frame_count += 1
        else:
            # After the animation is done, you can draw other things or leave the screen white
            self.screen.fill(self.white)
        
        pygame.display.flip()
        pygame.time.delay(30)  # Approximately 30 frames per second

    def run(self):
        running = True
        while running and not self.animation_done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.screen_width, self.screen_height = event.w, event.h
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
                    self.center_elements()  # Recenter elements on resize
            
            self.update()

        # After splash screen is done, return control to the main program
        return running
