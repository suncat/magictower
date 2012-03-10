import pygame, sys
from msgbox import draw_dialog


class Choicebox(pygame.sprite.Sprite):

	def __init__(self, msgs, location=(0, 0), surface=None):
		self.font = pygame.font.Font(None, 30)
		self.msgs = msgs
		self.surface = surface if surface else pygame.display.get_surface()
		self.x, self.y = location

	def show(self, player, d):
		draw_dialog(self.surface, [129, 155, 600, 200], [255, 255, 0], [255, 127, 0])
		y = 155 + self.y
		for msg in self.msgs:
			choice_msg = self.font.render(msg, 1, (0, 0, 0))
			self.surface.blit(choice_msg, (129 + self.x, y))
			y += 30
		pygame.display.update()
		waiting = True
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					m = d.get(event.key)
					if m is not None:
						getattr(player, m)()
					waiting = False
