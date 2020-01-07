import pygame
import pygame.sysfont


class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.stats = stats
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.sysfont.SysFont(None, 38, italic=True)
        self.score_color = 255, 130, 0
        self.high_color = 255, 0, 0
        self.level_color = 0, 155, 0
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_level(self):
        self.level_str = "Level : " + str(self.stats.level)
        self.level_image = self.font.render(self.level_str, True, self.level_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.y = 4
        self.level_rect.centerx = int((self.screen_rect.centerx + self.ai_settings.screen_width) / 2)

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        self.score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(self.score_str, True, self.score_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.y = 4
        self.score_image_rect.right = self.ai_settings.screen_width - 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_image, self.high_image_rect)

    def prep_high_score(self):
        rounded_high_score = int(round(self.stats.high_score, -1))
        self.high_str = "High Score: " + "{:,}".format(rounded_high_score)
        self.high_image = self.font.render(self.high_str, True, self.high_color)
        self.high_image_rect = self.high_image.get_rect()
        self.high_image_rect.centerx = self.screen_rect.centerx
        self.high_image_rect.y = 4
