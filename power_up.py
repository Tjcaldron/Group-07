import pygame

class Power_Up(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('assetsgraphics/heart.png')
        x = (size)
        y = (size)
        self.image.blit(self.image, (x, y))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift):
        self.rect.x += x_shift

    def right(question, player, level): {print('life += 1')}
    def wrong(question, player, level): {print('suck butts noob')}

class Teleport(Power_Up):
    def __inti__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load('assetsgraphics/erasersprite.png')
        x = (size)
        y = (size)
        self.image.blit(self.image, (x,y))
        self.rect = self.image.get_rect(topleft = pos)
