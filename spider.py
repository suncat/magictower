# coding:utf8
from __future__ import absolute_import
import pygame
import random

from consts import CELL_SIZE
from npc import Npc
from enemy import Enemy
from character import load_images
from msgbox import Msgbox


class BaseSpider(Enemy):

	def do_collide(self, player):
		Msgbox("It may poison you, so watch out!").show()
		pois = random.randint(1, self.pois_improb)
		if pois == 1:
			Msgbox("Unluckily, you are poisoned!").show()
			player.poison()
		super(BaseSpider, self).do_collide(player)


class Spider(BaseSpider):
	images = load_images(["spider.png", "spider2.png"])
	hp = 540
	money = 13
	exp = 12
	condition = "POISON"
	pois_improb = 10
