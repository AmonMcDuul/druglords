import pygame


class Enemy():

    def __init__(self, pong_settings, screen):
        self.screen = screen
        self.pong_settings = pong_settings
        self.image = pygame.image.load('pong_game\\pong.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = self.screen_rect.top - self.pong_settings.offset_rec_y

        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.pong_settings.rectangle_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.pong_settings.rectangle_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
