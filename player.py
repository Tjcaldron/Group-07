import pygame
# win = pygame.display.set_mode((1520,680))
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        # self.char1 = pygame.image.load('assetsgraphics/Girl Final.png')
        # self.char = pygame.transform.scale(self.char1, (50,80))
        # self.player = win.blit(self.char, (self.x,self.y))