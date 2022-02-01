from cmath import rect
# Sound & Music PyGame Class
from pygame import mixer
import pygame
pygame.init()
# Mixer needs to be called - do not remove!
mixer.init()



win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

gravity = 1
x = 50
y = 50
width = 40
height = 60
vel = 5
jump = 25
increase = 1

run = True

while run:
    clock = pygame.time.Clock()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x - vel > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x + vel < 500 :
        x += vel

    if keys[pygame.K_UP] and y - vel > 0:
        y -= jump

    if y + vel + height < 400:
        y += 5
    # else:
    #     y = 0
    
    win.fill((0,0,0))  # Fills the screen with black
    player = pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    floor = pygame.draw.rect(win, (255,255,0), (0, 400, 1000, height))   
    # if player.colliderect(floor):
    #     vel = 0
    #     y = 0

    pygame.display.update() 
    
pygame.quit()