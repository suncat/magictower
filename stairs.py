from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class UpStair(Npc):
    images = load_images(["upstair.png"])

    def do_collide(self, player):
        player.go_upstair()


class DownStair(Npc):
    images = load_images(["downstair.png"])

    def do_collide(self, player):
        player.go_downstair()