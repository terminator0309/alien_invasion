import pygame
import pygame.sysfont


class Life:
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images\\life.png")
        self.img_rect = self.image.get_rect()
        self.img_rect.x, self.img_rect.y = 10, 0
        self.color = 255, 255, 255
        self.font = pygame.sysfont.SysFont(None, 38)
        self.prep_life(stats)

    def blitme(self):
        self.screen.blit(self.image, self.img_rect)

    def prep_life(self, stats):
        self.life_str = " X " + str(stats.ship_left)
        self.life_img = self.font.render(self.life_str, True, self.color)
        self.life_rect = self.life_img.get_rect()
        self.life_rect.y = 0
        self.life_rect.x = 30

    def show_life(self):
        self.screen.blit(self.life_img, self.life_rect)

