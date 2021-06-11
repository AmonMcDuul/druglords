import pygame
from pygame.sprite import Group

from pong_game.settings import Settings
from pong_game.rectangle import Rectangle
from pong_game.enemy import Enemy
from pong_game.ball import Ball
import pong_game.pong_functions as gf


clock = pygame.time.Clock()


def run_game():
    pygame.init()
    pong_settings = Settings()
    screen = pygame.display.set_mode(
        (pong_settings.screen_width, pong_settings.screen_height))
    pygame.display.set_caption("Pong")

    rectangle = Rectangle(pong_settings, screen)
    enemy = Enemy(pong_settings, screen)

    ball = Ball(pong_settings, pong_settings.black, 20, 20)
    ball.rect.x = pong_settings.screen_width / 2
    ball.rect.y = pong_settings.screen_height / 2

    all_sprites_list = pygame.sprite.Group()

    all_sprites_list.add(ball)

    while True:
        gf.check_events(pong_settings, screen, rectangle)
        rectangle.update()
        enemy.update()

        all_sprites_list.update()
        gf.check_ball(pong_settings, ball)
        gf.collide(ball, rectangle)

        screen.fill(pong_settings.bg_color)
        all_sprites_list.draw(screen)
        rectangle.blitme()
        enemy.blitme()

        pygame.display.flip()

        clock.tick(60)

        #gf.update_screen(pong_settings, screen, rectangle, ball)
