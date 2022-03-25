import pygame
from player import Player
from text_box import Text_Box
import json
import random
from settings import screen_width, screen_height

class Quesion_Event:
	def __init__(self, level, player, right, wrong):
		(self.question, self.answers, self.answer) = self.pull_question()
		self.get_and_stop_movement(player)
		self.function_right = right
		self.function_wrong = wrong
		
	def pull_question(self):
		file = open('questions.json')
		questions = json.load(file)

		data = questions[str(random.randrange(0, len(questions)))]
		return (data[0],data[1],data[2])

	def get_and_stop_movement(self, player):
		player.input = False
		player.graviy = 0
		player.direction.x = 0

	def create_text_box(self):
		width_fourth = screen_width / 4
		height_tenth = screen_height / 10

		box = Text_Box((width_fourth, height_tenth * 6), (width_fourth * 2, height_tenth * 3), self.question, self.answers)
		return box

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_1]:
			if self.answer == 1:
				return True
		if keys[pygame.K_2]:
			if self.answer == 2:
				return True
		if keys[pygame.K_3]:
			if self.answer == 3:
				return True
		if keys[pygame.K_1]:
			if self.answer != 1:
				return False
		if keys[pygame.K_2]:
			if self.answer != 2:
				return False
		if keys[pygame.K_3]:
			if self.answer != 3:
				return False

	def reset_game(self, player):
		player.input = True
		player.graviy = 0.8
		player.direction.x = 8

	def update(self, level, player):
		if self.get_input():
			self.function_right(player, level)
			self.reset_game(player)
			level.text_box.empty()
		elif self.get_input == False:
			self.function_wrong(player, level)
			self.reset_game(player, level)
			level.text_box.empty()
