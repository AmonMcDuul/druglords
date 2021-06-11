import sys
import pygame


def check_keydown_events(event, pong_settings, screen, rectangle):
    if event.key == pygame.K_RIGHT:
        rectangle.moving_right = True
    elif event.key == pygame.K_LEFT:
        rectangle.moving_left = True
    elif event.key == pygame.K_q:
        pygame.display.quit()
        pygame.quit()


def check_keyup_events(event, pong_settings, screen, rectangle):
    if event.key == pygame.K_RIGHT:
        rectangle.moving_right = False
    elif event.key == pygame.K_LEFT:
        rectangle.moving_left = False


def check_events(pong_settings, screen, rectangle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pong_settings, screen, rectangle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pong_settings, screen, rectangle)


def check_ball(pong_settings, ball):
    if ball.rect.x >= pong_settings.screen_width:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > pong_settings.screen_height:
        #ball.velocity[1] = -ball.velocity[1]
        pygame.display.quit()
        pygame.quit()
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]


def collide(ball, rectangle):
    if ball.rect.colliderect(rectangle):
        ball.bounce()


def update_screen(pong_settings, screen, rectangle, ball):
    screen.fill(pong_settings.bg_color)

    rectangle.blitme()
    pygame.display.flip()
