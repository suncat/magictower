from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class Smalldrug(Npc):
    images = load_images(["smalldrug.png"])
    heal = 130

    def do_collide(self, player):
        player.health += self.heal
        self.kill()


class Middledrug(Smalldrug):
    images = load_images(["middledrug.png"])
    heal = 300


class Largedrug(Smalldrug):
    images = load_images(["largedrug.png"])
    heal = 500


class Exlargedrug(Smalldrug):
    images = load_images(["exlargedrug.png"])
    heal = 650
