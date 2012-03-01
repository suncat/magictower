from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from msgbox import Msgbox


class Defencerock(Npc):
    images = ["defencerock.png"]
    dp = 8

    def __init__(self, location):
        super(Defencerock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.defence += self.dp
        self.kill()


class MiddleDProck(Defencerock):
    images = ["middledprock.png"]
    dp = 30

    def do_collide(self, player):
        super(MiddleDProck, self).do_collide(player)
        for group in self.groups():
            if isinstance(sprite, Trap):
                sprite.kill()
        Msgbox("You killed the trap, you are so clever.").show()


class Largedprock(Defencerock):
    images = ["largedprock.png"]
    dp = 60
