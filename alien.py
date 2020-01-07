import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images\\ufo2.png")
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height
        self.rect.x = ai_settings.screen_width - 1.35 * self.rect.width

    def update(self):
        self.rect.y += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= screen_rect.top + 30:
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)
