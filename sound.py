import pygame
from pygame import mixer

class Sound():
    def __init__(self):
        pygame.mixer.init()
        self.music = pygame.mixer.Sound("sound\math_bckgnd_classical.wav")
        self.jump = pygame.mixer.Sound("sound\Jump.wav")
        self.run = pygame.mixer.Sound("sound\Run.wav")
        self.stop = pygame.mixer.Sound("sound\Stop.wav")
        # self.fall = pygame.mixer.Sound("sound\Fall.wav")
        

    def play_music(self):
        self.music.play()
    