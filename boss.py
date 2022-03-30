import imp
from matplotlib import animation
from numpy import character
import pygame
from support import import_folder
from fire_balls import Fire_balls
from questions import Question_NonEvent


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, level):
        super().__init__()
        # boss_files = ["scroll.png", "scroll2.png"]
        self.image = pygame.image.load('assets\graphics\scroll.png')

        x = 100
        y = 166
        # self.import_boss_assets()

        self.move_direction = 1
        self.move_counter = 0
        self.fire_ball_counter = 1
        self.image.blit(self.image, (x, y))
        self.rect = self.image.get_rect(center=pos)
        self.health = 5
        question = Question_NonEvent(level)
        box = question.create_text_box()
        level.question.append(question)
        level.text_box.add(box)

    def take_life(self):
        self.health -= 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def make_fire_balls(self, level):
        if self.fire_ball_counter % 300 != 0:
            self.fire_ball_counter += 1

        elif self.fire_ball_counter == 300:
            fire_ball_1 = Fire_balls(self.rect.x, self.rect.y, -4, 2)
            fire_ball_2 = Fire_balls(self.rect.x, self.rect.y, 0, 5)
            fire_ball_3 = Fire_balls(self.rect.x, self.rect.y, 4, 2)
            level.fire_balls.add(fire_ball_1)
            level.fire_balls.add(fire_ball_2)
            level.fire_balls.add(fire_ball_3)
            self.fire_ball_counter += 1

        elif self.fire_ball_counter == 600:
            fire_ball_1 = Fire_balls(self.rect.x, self.rect.y, -2, 0)
            fire_ball_2 = Fire_balls(self.rect.x, self.rect.y, 0, 2)
            fire_ball_3 = Fire_balls(self.rect.x, self.rect.y, 2, 0)
            fire_ball_4 = Fire_balls(self.rect.x, self.rect.y, -1, 1)
            fire_ball_5 = Fire_balls(self.rect.x, self.rect.y, 0, 4)
            fire_ball_6 = Fire_balls(self.rect.x, self.rect.y, 1, -1)
            level.fire_balls.add(fire_ball_1)
            level.fire_balls.add(fire_ball_2)
            level.fire_balls.add(fire_ball_3)
            level.fire_balls.add(fire_ball_4)
            level.fire_balls.add(fire_ball_5)
            level.fire_balls.add(fire_ball_6)
            self.fire_ball_counter += 1


        else:
            self.fire_ball_counter = 1
            fire_ball_1 = Fire_balls(self.rect.x, self.rect.y, -4, 0)
            fire_ball_2 = Fire_balls(self.rect.x, self.rect.y, 0, 4)
            fire_ball_3 = Fire_balls(self.rect.x, self.rect.y, 4, 0)
            level.fire_balls.add(fire_ball_1)
            level.fire_balls.add(fire_ball_2)
            level.fire_balls.add(fire_ball_3)
         
            

    def update(self, x_shift, level):
        self.rect.x += x_shift
        self.move_counter += 1
        if abs(self.move_counter) > 50:  # absolute value so it stays positive
            self.move_direction *= -1  # go right
            self.move_counter *= -1  # go left

        self.make_fire_balls(level)
