from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from msgbox import Msgbox
from character import load_images


class Defencerock(Npc):
    images = load_images(["defencerock.png"])
    dp = 8

    def do_collide(self, player):
        player.defence += self.dp
        self.kill()


class MiddleDProck(Defencerock):
    images = load_images(["middledprock.png"])
    dp = 30

    def do_collide(self, player):
        super(MiddleDProck, self).do_collide(player)
        for group in self.groups():
            if isinstance(sprite, Trap):
                sprite.kill()
        Msgbox("You killed the trap, you are so clever.").show()


class Largedprock(Defencerock):
    images = load_images(["largedprock.png"])
    dp = 60
