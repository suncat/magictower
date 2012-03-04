from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc


class UpStair(Npc):
    images = ["upstair.png"]

    def __init__(self, location):
        super(UpStair, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.go_upstair()


class DownStair(Npc):
    images = ["downstair.png"]

    def __init__(self, location):
        super(DownStair, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.go_downstair()