import pygame
from random import randint
 
class Ball(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, pong_settings, color, width, height):
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.pong_settings = pong_settings

        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [10, 10, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
