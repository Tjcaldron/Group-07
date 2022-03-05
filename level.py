import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self,level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        # self.world_shift = 0
        # self.bg1 = pygame.image.load('assetsgraphics/background.png')

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
            
    def horizonal_movment_collision(self):
        
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.left = sprite.rect.left
                    player.direction.x = 0

    def virtical_movment_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        # self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.horizonal_movment_collision()
        self.virtical_movment_collision()
        self.player.draw(self.display_surface)
        