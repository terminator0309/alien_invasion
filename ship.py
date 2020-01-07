import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images\\rocket (1).png")

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.y = self.rect.centery
        self.moving_up = False
        self.moving_down = False

    def update_ship(self):
        if self.moving_up and self.rect.top >= 30:
            self.y -= self.ai_settings.ship_speed_factor

        elif self.moving_down and self.rect.bottom <= self.ai_settings.screen_height:
            self.y += self.ai_settings.ship_speed_factor

        self.rect.centery = self.y

    def center_the_ship(self):
        self.y = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
