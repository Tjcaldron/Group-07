from cmath import rect
from pygame import mixer
import pygame
pygame.init()
# Mixer needs to be called for sound
mixer.init()
mixer.music.load('sound\english_bckgnd_lofi.wav')
mixer.music.play(-1)

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")


class physics():
    on_ground = True
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 40
        self.height = 60
        self.vel = 4
        self.frame = 0
        self.health = 10
        self.jump = 0
        self.m = 2
        self.s = 10
    def jumpu(self):
        self.jump = 1
    def run(self):
        run = True
        floors = 400
           
        
        while run:
            clock = pygame.time.Clock()
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
    
            if keys[pygame.K_LEFT] and self.x - self.vel > 0:
                self.x = self.x - self.s

            if keys[pygame.K_RIGHT] and self.x + self.vel < 500 :
                self.x = self.x + self.s

            if keys[pygame.K_UP] and self.y - self.vel > 0:
                if self.vel > 0:
                    F = ( 0.5 * self.m * (self.vel*self.vel) )
                else:
                    F = -( 0.5 * self.m * (self.vel*self.vel) )

                self.y = self.y - F

                self.vel = self.vel - 1

                if self.y >= 300:
                    self.y = 300
                    self.jump = 0
                    self.vel = 8
                self.jumpu()             
            if self.y + self.vel + self.height < floors:
                self.y += 15
    
    
            win.fill((0,0,0))  # Fills the screen with black
            player = pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))
            floor = pygame.draw.rect(win, (255,255,0), (0, 400, 1000, self.height))
    

            pygame.display.update() 
    
        pygame.quit()






def main():
    p = physics()
    p.run()
    

if __name__ == '__main__':
    main()