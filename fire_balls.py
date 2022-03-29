from matplotlib import animation
from numpy import character
import pygame
from support import import_folder


class Fire_balls(pygame.sprite.Sprite):
    def __init__(self, x, y, dir_x, dir_y):
        super().__init__()
        self.image = pygame.image.load('assets/graphics/fire.png')
        self.x = x
        self.y = y
        # self.radius = 100
        # self.color = "red"
        self.image.blit(self.image, (x, y))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = (dir_x, dir_y)
        self.life = 1000

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        self.life -= 1
        if self.life <= 0:
            pygame.sprite.Sprite.kill(self)
