import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.ship = ship
        # for rectangular bullets

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        self.x = float(self.rect.x)
        self.speed_factor = ai_settings.bullet_speed_factor
        self.color = ai_settings.bullet_color
        """
        # for circular bullets
        self.speed_factor = ai_settings.bullet_speed_factor
        self.color = ai_settings.bullet_color
        self.coordx = ship.rect.right
        self.coordy = ship.rect.centery
        self.coord = [ship.rect.right, ship.rect.centery]
        self.radius = ai_settings.bullet_radius
        """
    def update(self):

        self.x += self.speed_factor
        self.rect.x = self.x
        """
        self.coordx += self.speed_factor
        self.coord = [self.coordx, self.coordy]
        """

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # pygame.draw.circle(self.screen, self.color, self.coord, self.radius)
