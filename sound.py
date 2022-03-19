import pygame
from pygame import mixer

class Sound():
    def __init__(self):
        pygame.mixer.init()
        self.music = pygame.mixer.Sound("sound\math_bckgnd_classical.wav")
        #self.jump = pygame.mixer.Sound("sound\jump.wav")

    def play_music(self):
        self.music.play()
    