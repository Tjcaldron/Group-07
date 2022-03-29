import pygame

class Teleport(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('assets/graphics/erasersprite.png')
        x = (size)
        y = (size)
        self.image.blit(self.image, (x, y))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift):
        self.rect.x += x_shift