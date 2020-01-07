class Settings:
    def __init__(self):

        # screen
        self.screen_width = 1200
        self.screen_height = 690
        self.bg_color = (25, 25, 25)

        # ship
        self.ship_limit = 3

        # bullets

        self.bullet_width = 15
        self.bullet_height = 4
        self.bullet_color = 0, 151, 255
        self.bullet_allowed = 2
        # self.bullet_radius = 5

        # aliens
        self.fleet_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

    def initialise_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
