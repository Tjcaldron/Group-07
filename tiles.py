import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos,size,img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        x = (size)
        y = (size)
        self.image.blit(self.image, (x, y))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

##where enemy creation begins, it is part of the level tiles
def enemies(self, layout, level_data):
    enemy_layout = layout(level_data['enemies'])
    self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')