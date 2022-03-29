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


    def right(question, player, level): 
        level.hearts += 1
        level.display_surface.blit(level.font.render(str(level.hearts), True, (0, 0, 0)), (32, 48))

    def wrong(question, player, level): 
        level.hearts -= 1
        level.display_surface.blit(level.font.render(str(level.hearts), True, (0, 0, 0)), (32, 48))
