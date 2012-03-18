from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class Smallmagic(Npc):
    images = load_images(["smallmagic.png"])
    power = 90

    def do_collide(self, player):
        player.magic += self.power
        self.kill()