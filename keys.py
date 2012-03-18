from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class BaseKey(Npc):

    def do_collide(self, player):
        player.pick_key(self.key)
        self.kill()


class YellowKey(BaseKey):
    images = load_images(["yellowkey.png"])
    key = 'y'


class BlueKey(BaseKey):
    images = load_images(["bluekey.png"])
    key = 'b'


class RedKey(BaseKey):
    images = load_images(["redkey.png"])
    key = 'r'


class GreenKey(BaseKey):
    images = load_images(["greenkey.png"])
    key = 'g'


class NormalGkey(BaseKey):
    images = load_images(["greenkey.png"])
    key = 'g'


class SwordKey(BaseKey):
    images = load_images(["swordkey.png"])
    key = 'sword'