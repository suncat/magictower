from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc


class Smallmagic(Npc):
    images = ["smallmagic.png"]
    power = 90

    def __init__(self, location):
        super(Smallmagic, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.magic += self.power
        self.kill()