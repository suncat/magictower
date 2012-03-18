from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class Wall(Npc):
    images = load_images(["wall.png"])

    def do_collide(self, player):
        player.undo()


class Fakewall(Wall):
    images = load_images(["wall.png"])

    def do_collide(self, player):
        self.kill()