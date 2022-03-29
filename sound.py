import pygame
"""
Collision playlist methods:

Here any collision sound file will be loaded and have its own method
to be called in external files that require sound interaction with 
Sprints and blocks.
"""

class Sound():
    def __init__(self):
        pygame.mixer.init()
        self.jump = pygame.mixer.Sound("sound\Jump.wav")
        self.run = pygame.mixer.Sound("sound\Run.wav")
        self.stop = pygame.mixer.Sound("sound\Stop.wav")
        
    def play_jump_Sound(self):
        self.jump.play()
        
    def play_run_Sound(self):
        self.run.play()
                
    def play_stop_Sound(self):
        self.stop.play()
        

        
    