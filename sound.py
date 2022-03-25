# from marshal import load
import pygame
from pygame import mixer

class Sound():
    def __init__(self):
        pygame.mixer.init()
        
        mixer.init.load()
        
        self.music = pygame.mixer.Sound("sound\background.wav")
        self.jump = pygame.mixer.Sound("sound\Jump.wav")
        self.run = pygame.mixer.Sound("sound\Run.wav")
        self.stop = pygame.mixer.Sound("sound\Stop.wav")
        # self.fall = mixer.load.Sound("sound\Fall.wav") --- 1st import load statement for init method
        

    def play_music(self):
        
        self.music.play()
        # mixer.music.play(-1) --- play background infinite -- how to impliment.
        
    