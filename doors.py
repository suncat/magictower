from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from character import load_images


class AbstractDoor(Npc):

    def __init__(self, location):
        super(AbstractDoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        if self.can_open(player):
            self.kill()
        else:
            player.undo()


class KeyDoor(AbstractDoor):

    def can_open(self, player):
        return player.use_key(self.key)


class YellowDoor(KeyDoor):
    images = load_images(["yellowdoor.png"])
    key = 'y'


class RedDoor(KeyDoor):
    images = load_images(["reddoor.png"])
    key = 'r'


class BlueDoor(KeyDoor):
    images = load_images(["bluedoor.png"])
    key = 'b'


class GreenDoor(KeyDoor):
    images = load_images(["greendoor.png"])
    key = 'g'


class Specialdoor(AbstractDoor):
    images = load_images(["specialdoor.png"])

    def can_open(self, player):
        return player.on_power


class Ftendoor(Npc):
    images = load_images(["specialdoor.png"])

    def __init__(self, location):
        super(Ftendoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        for sprite in player.currentfloor.group:
            if isinstance(sprite, Ftendoor):
                sprite.kill()


class Switchdoor(AbstractDoor):
    images = load_images(["specialdoor.png"])

    def can_open(self, player):
        return False
