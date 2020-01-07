import pygame
import sys
from bullets import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            high_score_save_and_exit(stats)

        elif event.type == pygame.KEYDOWN:
            check_events_down(event, ai_settings, screen, ship, bullets, stats)

        elif event.type == pygame.KEYUP:
            check_events_up(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, sb)


def check_events_up(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False

    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events_down(event, ai_settings, screen, ship, bullets, stats):
    if event.key == pygame.K_q:
        high_score_save_and_exit(stats)

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:

        if len(bullets) <= ai_settings.bullet_allowed:
            pygame.mixer.music.play()
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def high_score_save_and_exit(stats):
    with open('high_score\\high_score.dat', 'r') as file:
        line = file.read()
        if int(line) < stats.high_score:
            file.close()
            file = open('high_score\\high_score.dat', 'w')
            file.write(str(stats.high_score))

        else:
            pass
    sys.exit()


def check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.game_active = True

        stats.reset_stats()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_score()

        aliens.empty()
        bullets.empty()
        ai_settings.initialise_dynamic_settings()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_the_ship()


def update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb, poster, life):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        poster.blitme()
        play_button.draw_button()

    sb.show_score()
    life.show_life()
    life.blitme()
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb, level_sound, alien_gone):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.left >= ai_settings.screen_width:
            bullets.remove(bullet)

    check_bullets_aliens_collision(ai_settings, screen, ship, bullets, aliens, stats, sb, level_sound, alien_gone)


def check_bullets_aliens_collision(ai_settings, screen, ship, bullets, aliens, stats, sb, level_sound, alien_gone):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # for magic bullet, change first True to False

    if collisions:
        pygame.mixer.Sound.play(alien_gone)
        for aliens in collisions.values():
            stats.score += (ai_settings.alien_point * len(aliens))
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        pygame.mixer.Sound.play(level_sound)
        sleep(2)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_aliens(ai_settings, screen, ship, bullets, aliens, stats, life):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, ship, bullets, aliens, stats, life)

    check_aliens_reach(ai_settings, screen, ship, bullets, aliens, stats, life)


def ship_hit(ai_settings, screen, ship, bullets, aliens, stats, life):
    stats.ship_left -= 1
    if stats.ship_left > 0:
        life.prep_life(stats)
        bullets.empty()
        aliens.empty()
        sleep(1)
        ship.center_the_ship()
        create_fleet(ai_settings, screen, ship, aliens)

    else:
        game_over = pygame.mixer.Sound('sound\\game_over.wav')
        pygame.mixer.Sound.play(game_over)
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_reach(ai_settings, screen, ship, bullets, aliens, stats, life):
    for alien in aliens.sprites():
        if alien.rect.left <= ship.rect.width:
            # do remember not to flip this '>' sign !!!
            ship_hit(ai_settings, screen, ship, bullets, aliens, stats, life)
        break


def get_number_aliens_y(ai_settings, alien_height):
    available_space_y = ai_settings.screen_height - alien_height
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y


def get_number_col(ai_settings, ship, alien_width):
    available_space_x = ai_settings.screen_width - 3 * alien_width - ship.rect.width
    number_cols = int(available_space_x / alien_width)
    return number_cols


def create_alien(ai_settings, screen, alien_number, alien_height, aliens, col_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.rect.y = (alien_height / 2) + 2 * alien_height * alien_number
    alien.rect.x = ai_settings.screen_width - alien_width * (col_number + 1) * 1.15
    # 1.15 is separation factor(spacing between ships)
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    alien_width = alien.rect.width
    number_aliens_y = get_number_aliens_y(ai_settings, alien_height)
    number_cols = get_number_col(ai_settings, ship, alien_width)

    for col_number in range(number_cols):
        for alien_number in range(number_aliens_y):
            create_alien(ai_settings, screen, alien_number, alien_height, aliens, col_number)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.x -= ai_settings.fleet_speed
    ai_settings.fleet_direction *= -1
