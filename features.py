from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class Firerock(Npc):
    images = load_images(["firerock.png"])
    feature = "FIRE"

    def __init__(self, location):
        super(Firerock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.feature = self.feature
        self.kill()


class Aquarock(Firerock):
	images = load_images(["aquarock.png"])
	feature = "WATER"


class Skyrock(Firerock):
	images = load_images(["skyrock.png"])
	feature = "SKY"