from cmath import rect
import pygame
pygame.init()

win = pygame.display.set_mode((1520,680))
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
        self.bg1 = pygame.image.load('background.png')
        self.bg = pygame.transform.scale(self.bg1, (1520,680))
        self.char1 = pygame.image.load('Girl Final.png')
        self.char = pygame.transform.scale(self.char1, (50,80))
    def jumpu(self):
        self.jump = 1

    def redrawGameWindow(self):
        global walkCount
        rocket = pygame.Surface((20, 20))
        win.blit(self.bg, (0,0))  # This will draw our background image at (0,0)
        player = win.blit(self.char, (self.x,self.y))
        floor = pygame.draw.rect(win, (255,255,0), (0, 600, 2000, 60))
        
        pygame.display.update()
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

            if keys[pygame.K_RIGHT] and self.x + self.vel < 1500 :
                self.x = self.x + self.s

            if keys[pygame.K_UP] and self.y - self.vel > 0:
                if self.vel > 0:
                    F = ( 0.5 * self.m * (self.vel*self.vel) )
                else:
                    F = -( 0.5 * self.m * (self.vel*self.vel) )

                self.y = self.y - F

                self.vel = self.vel - 1

                if self.y >= 500:
                    self.y = 425
                    self.jump = 0
                    self.vel = 8
                self.jumpu()             
            if self.y < 525:
                self.y += 15
    
    
            win.fill((0,0,0))  # Fills the screen with black
            
    
            self.redrawGameWindow()
    
        pygame.quit()






def main():
    p = physics()
    p.run()
    

if __name__ == '__main__':
    main()