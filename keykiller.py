# coding:utf8
from __future__ import absolute_import
import pygame
import random

from consts import CELL_SIZE
from npc import Npc
from enemy import Enemy
from character import load_images
from msgbox import Msgbox


class KeyKiller(Npc):
	keys = 1

	def do_collide(self, player):
		if player.speed != [0, 0]:
			player.ykeynum = player.ykeynum - self.keys if player.ykeynum > 0 else 0
			player.bkeynum = player.bkeynum - self.keys if player.bkeynum > 0 else 0
			player.rkeynum = player.rkeynum - self.keys if player.rkeynum > 0 else 0
			player.gkeynum = player.gkeynum - self.keys if player.gkeynum > 0 else 0


class SKeyKiller(KeyKiller):
	images = load_images(["skeykiller.png"])


class MKeyKiller(KeyKiller):
	keys = 2
	images = load_images(["mkeykiller.png"])