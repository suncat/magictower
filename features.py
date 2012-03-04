from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc


class Firerock(Npc):
    images = ["firerock.png"]
    feature = "FIRE"

    def __init__(self, location):
        super(Firerock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.feature = self.feature
        self.kill()