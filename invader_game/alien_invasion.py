import pygame
from pygame.sprite import Group

from invader_game.settings import Settings
from invader_game.ship import Ship
from invader_game.alien import Alien
import invader_game.game_functions as gf


def run_alien():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # make group to store bullets and aliens
    bullets = Group()
    aliens = Group()

    # make fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
