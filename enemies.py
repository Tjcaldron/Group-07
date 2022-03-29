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
blue = (0, 0, 128)

x = 1200
y = 700

display_surface = pygame.display.set_mode((x,y))

font = pygame.font.Font('freesansbold.ttf', 64)

text = font.render('Game Over!', True, white, blue)
textRect = text.get_rect()

textRect.center = (x // 2, y // 2)

while True:
    display_surface.fill(red)
    display_surface.blit(text,textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
