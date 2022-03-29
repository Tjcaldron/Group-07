import pygame
'''
BOO!
   V
     ------
   /        \
  | O      O |
(\      0     /)  
  |         |
   |       |
   |     /
    |  /
  
'''
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)

x = 400
y = 400

display_surface = pygame.display.set_mode((x,y))
pygame.display.set_caption("Game Over")

font = pygame.font.Font('freesansbold.ttf', 64)

screen_width = 1200
screen_height = 700
win = pygame.display.set_mode((1200,700))
screen = pygame.display.set_mode((screen_width,screen_height))
