from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc


class BaseKey(Npc):

    def __init__(self, location, size=(CELL_SIZE,CELL_SIZE)):
        super(BaseKey, self).__init__(location, size)

    def do_collide(self, player):
        player.pick_key(self.key)
        self.kill()


class YellowKey(BaseKey):
    images = ["yellowkey.png"]
    key = 'y'


class BlueKey(BaseKey):
    images = ["bluekey.png"]
    key = 'b'


class RedKey(BaseKey):
    images = ["redkey.png"]
    key = 'r'


class GreenKey(BaseKey):
    images = ["greenkey.png"]
    key = 'g'


class NormalGkey(BaseKey):
    images = ["greenkey.png"]
    key = 'g'