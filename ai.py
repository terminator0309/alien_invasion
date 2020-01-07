import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from games_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from wel_poster import Poster
from ships_left import Life


def game():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION (press 'q' to exit)")

    ship = Ship(screen, ai_settings)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    poster = Poster(ai_settings, screen)
    life = Life(ai_settings, screen, stats)

    bullets = Group()
    aliens = Group()

    pygame.mixer.music.load('sound\\laser.mp3')
    level_sound = pygame.mixer.Sound("sound\\level_up.wav")
    alien_gone = pygame.mixer.Sound("sound\\alien_gone.wav")

    play_button = Button(ai_settings, screen, "Play")
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)

        if stats.game_active:
            ship.update_ship()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb, level_sound, alien_gone)
            gf.update_aliens(ai_settings, screen, ship, bullets, aliens, stats, life)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb, poster, life)


game()
