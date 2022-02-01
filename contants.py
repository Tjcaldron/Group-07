import pygame

#frames per second
CLOCK = pygame.time.Clock()
FPS = 60

#screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#define colors !!!these are just temp CHANGE THESE TO WHAT ARE NEEDED
BLUE = (200, 255, 255)
LBLUE = (50, 255, 255)
DBLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 86, 221)

# load images
PLAYER = pygame.image.load("Assets/temp_sun.png")

#define font - if we want to have things written on the screen this is the font style and size
FONT = pygame.font.SysFont('Bauhaus 93', 70)
FONT_SCORE = pygame.font.SysFont('Bauhaus 93', 30)


# load sounds and set volume
ITEM_COLLECT = pygame.mixer.Sound("Assets/sounds/itemcollect.wav")
ITEM_COLLECT.set_volume(0.5)