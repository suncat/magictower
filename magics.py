from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class Basemagic(Npc):

	def do_collide(self, player):
		player.magic += self.power
		self.kill()


class Smallmagic(Basemagic):
    images = load_images(["smallmagic.png"])
    power = 90


class Midmagic(Basemagic):
	images = load_images(["midmagic.png"])
	power = 160
