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
        self.image.blit(self.image, (x, y))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = (dir_x, dir_y)
        self.life = 300
        size = self.image.get_size()
        smaller_img = pygame.transform.scale(self.image, (int(size[0]/2), int(size[1]/2)))
        self.image = smaller_img

    def update(self, x_shift):
        self.rect.x += self.speed[0] + x_shift
        self.rect.y += self.speed[1]
        self.life -= 1
        if self.life <= 0:
            pygame.sprite.Sprite.kill(self)
