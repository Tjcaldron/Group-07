import pygame

class Text_Box(pygame.sprite.Sprite):
	def __init__(self,pos,size,msg):
		super().__init__()
		self.image = pygame.Surface((size[0],size[1]))
		self.image.fill('white')
		self.rect = self.image.get_rect(topleft = pos)
		self.font = pygame.font.Font("ocraextended.ttf", 30)
		
		question = self.get_question("What is 2 + 2?", pos[0] + 10, pos[1] + 10)
		self.image.blit(question)

		answers = self.get_answers("A. 1-B. 2-C. 4", pos[0] + 100, pos[1] + 10)
		self.image.blit(answers[0], answers[1], answers[2])

	def get_question(self, msg, pos_x, pos_y):
		text = self.font.render(msg, True, (0, 0, 0))
		textRect = text.get_rect()
		textRect.topleft = (pos_x, pos_y) 
		return (text, textRect)

	def get_answers(self, msg, pos_x, pos_y):
		answers = msg.split("-")
		text0 = self.font.render(answers[0], True, (0, 0, 0))
		text0_rect = text0.get_rect()
		text0_rect.topleft = (pos_x, pos_y)

		text1 = self.font.render(answers[1], True, (0, 0, 0))
		text1_rect = text1.get_rect()
		text1_rect.topleft = ((pos_x + self.size) / 2, pos_y)

		text2 = self.font.render(answers[2], True, (0, 0, 0))
		text2_rect = text2.get_rect()
		text2_rect.topleft = (pos_x + self.size, pos_y)

		return ((text0, text0_rect), (text1, text1_rect), (text2, text2_rect))

