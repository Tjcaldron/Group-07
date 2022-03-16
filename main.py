import pygame, sys
from settings import *
from level import Level


pygame.init()
screen_width = 1200
screen_height = 700
win = pygame.display.set_mode((1200,700))
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
bg1 = pygame.image.load('assets/graphics/background.png')
bg = pygame.transform.scale(bg1, (1200,700))


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.blit(bg, (0,0))
    # screen.fill('black')
    level.run()


    pygame.display.update()
    clock.tick(60)
