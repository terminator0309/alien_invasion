import pygame.sysfont


class Button:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255, 255, 255)
        self.button_color = (205, 0, 0)

        self.font = pygame.sysfont.SysFont('showcardgothic', 40)
        self.width, self.height = 200, 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 125

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


