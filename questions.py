# import the pygame module
import pygame
import random

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *

# Initialize pygame objects.
pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# assigning values to X and Y variable
width = 650
height = 700

pixel = 64

# create the display surface object
# of specific dimension..e(X, Y).
screen = pygame.display.set_mode((width, height))

# set the pygame window name
pygame.display.set_caption('CORONA SCRAPER')

gameIcon = pygame.image.load('rectangleBlock.png')

backgroundImg = pygame.image.load('wallBackground.jpg')

playerImage = pygame.image.load('player.png')

playerXPosition = (width/2) - (pixel/2)
playerYPosition = height - pixel - 10

playerXPositionChange = 0

def player(x, y):
	screen.blit(playerImage, (x, y))

blockImage = pygame.image.load('rectangleBlock.png')

blockXPosition = random.randint(0, width - pixel)
blockYPosition = 0 - pixel

blockXPositionChange = 0
blockYPositionChange = 2

def block(x, y):
	screen.blit(blockImage, (x, y))

def crash():
	global blockYPosition

	if playerYPosition < (blockYPosition + pixel):
		if ((playerXPosition > blockXPosition 
			and playerXPosition < (blockXPosition + pixel))
			or (playerXPosition + pixel) > blockXPosition
			and (playerXPosition + pixel) < (blockXPosition + pixel)):
			blockYPosition = height + 1000

running = True

while running:

	screen.blit(backgroundImg, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				playerXPositionChange = 3

			if event.key == pygame.K_LEFT:
				playerXPosition = -3

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or pygame.K_LEFT:
				playerXPositionChange = 0

	if playerXPosition >= (width - pixel):
		playerXPosition = (width - pixel)

	if playerXPosition <= 0:
		playerXPosition = 0

	# Multiple Blocks Movement after each other
	# and condition used because of game over function
	if (blockYPosition >= height - 0 and
		blockYPosition <= (height + 200)):

		blockYPosition = 0 - pixel

		# randomly assign value in range
		blockXPosition = random.randint(0, (width - pixel))

	playerXPosition += playerXPositionChange
	blockYPosition += blockYPositionChange

	player(playerXPosition, playerYPosition)
	block(blockXPosition, blockYPosition)

	crash()

	pygame.display.update()


