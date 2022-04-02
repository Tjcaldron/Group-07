import pygame


"""


Text box in which questions and answers will be generated and displayed:


"""
class Text_Box(pygame.sprite.Sprite):
	def __init__(self,pos,size,question,answers):
		super().__init__()
		self.image = pygame.Surface((size[0],size[1]))
		self.image.fill('white')
		self.rect = self.image.get_rect(topleft = pos)
		self.font = pygame.font.SysFont("ocraextended", 30)
		
		question_object = self.get_question(question, 20, 10)
		self.image.blit(question_object[0], question_object[1])

		answers_object = self.get_answers(answers, 20, 110)
		self.image.blit(answers_object[0][0], answers_object[0][1])
		self.image.blit(answers_object[1][0], answers_object[1][1])
		self.image.blit(answers_object[2][0], answers_object[2][1])


	def get_question(self, msg, pos_x, pos_y):
		text = self.font.render(msg, True, "black")
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
		text1_rect.topleft = ((pos_x + 250), pos_y)

		text2 = self.font.render(answers[2], True, (0, 0, 0))
		text2_rect = text2.get_rect()
		text2_rect.topleft = (pos_x + 450, pos_y)

		return ((text0, text0_rect), (text1, text1_rect), (text2, text2_rect))

