from matplotlib import animation
from numpy import character
import pygame
from support import import_folder


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # boss_files = ["scroll.png", "scroll2.png"]
        self.image = pygame.image.load('assets\graphics\scroll.png')

        x = 100
        y = 166
        # self.import_boss_assets()

        self.move_direction = 1
        self.move_counter = 0
        self.image.blit(self.image, (x, y))
        self.rect = self.image.get_rect(center=pos)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:  # absolute value so it stays positive
            self.move_direction *= -1  # go right
            self.move_counter *= -1  # go left
