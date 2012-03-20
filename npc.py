#! /usr/bin/env python
#coding=utf-8
import character

from consts import CELL_SIZE


class Npc(character.Character):
	feature = "NONE"
	skill = "NO"
	condition = "NORMAL"

	def __init__(self, location, realsize=(CELL_SIZE, CELL_SIZE)):
	    super(Npc, self).__init__(location, realsize)

	def do_collide(self, player):
		pass

class GrassMixin(object):
	feature = "GRASS"