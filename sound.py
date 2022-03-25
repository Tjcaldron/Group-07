# from marshal import load
import pygame
from pygame import mixer

class Sound():
    def __init__(self):
        pygame.mixer.init()
        
        mixer.music.load()
        
        self.music = pygame.mixer.Sound("sound\background.wav")
        self.jump = pygame.mixer.Sound("sound\Jump.wav")
        self.run = pygame.mixer.Sound("sound\Run.wav")
        # self.stop = pygame.mixer.Sound("sound\Stop.wav")
        
        

    def play_music(self):
        
        self.music.play()
        self.jump.play()
        self.run.play()
        
        # mixer.music.play(-1) --- play background infinite -- how to impliment.
        
    