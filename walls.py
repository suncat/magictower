from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc


class Wall(Npc):
    images = ["wall.png"]

    def __init__(self, location):
        super(Wall, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()


class Fakewall(Wall):
    images = ["wall.png"]

    def do_collide(self, player):
        self.kill()