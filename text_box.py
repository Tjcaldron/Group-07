import pygame

class Text_Box(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill('white')
		self.rect = self.image.get_rect(topleft = pos)
		self.font = pygame.font.Font("ocraextended.ttf", 30)

	def get_question(self, msg, pos_x, pos_y):
		text = self.font.render(msg, True, (0, 0, 0))
		textRect = text.get_rect()
		textRect.topleft = (pos_x, pos_y) 
		return (text, textRect)

	def get_answers(self, msg, pos_x, pos_y):
		answers = msg.split("-")
