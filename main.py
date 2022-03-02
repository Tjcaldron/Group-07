import pygame, sys
from settings import *
from level import Level
# from game_data import level_0
from pygame import mixer
pygame.init()
# Mixer needs to be called for sound
mixer.init()
mixer.music.load("sound\english_bckgnd_lofi.wav")
mixer.music.play(-1)
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
# level = Level(level_0,screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('grey')
	# level.run()

	pygame.display.update()
	clock.tick(60)