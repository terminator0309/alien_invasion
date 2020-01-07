import pygame


class Poster:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images\\alien_invasion.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx, self.image_rect.centery = self.screen_rect.centerx, self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
