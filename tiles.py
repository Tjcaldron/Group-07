import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

##where enemy creation begins, it is part of the level tiles
def enemies(self, layout, level_data):
    enemy_layout = layout(level_data['enemies'])
    self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')