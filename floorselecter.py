from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from choicebox import Choicebox
from npc import Npc
from character import load_images


class FloorSelecter(Choicebox):
	rect = (300, 200, 100, 40)

	def __init__(self, player, surface=None):
		self.floornum = player.currentfloor.floornum
		msgs = [str(self.floornum)]
		keydict = {pygame.K_DOWN: 'dec_floornum' , pygame.K_UP: 'inc_floornum'}
		super(FloorSelecter, self).__init__(msgs, keydict=keydict, surface=surface)

	def dec_floornum(self):
		self.floornum -= 1
		self.msgs = [str(self.floornum)]

	def inc_floornum(self):
		self.floornum += 1
		self.msgs = [str(self.floornum)]
