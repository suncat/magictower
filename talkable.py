from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from msgbox import Msgbox


class Talkable(Npc):

    def __init__(self, location):
        super(Talkable, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        for msg in self.msgs:
            Msgbox(msg).show()
        self.kill()


class Oldman(Talkable):
    images = ["oldman.png"]
    msgs = ["Do not think about everything is so easy. Mind traps.",]


class Franklin(Talkable):
    images = ["franklin.png"]
    msgs = [
        "My name is Franklin.",
        "And you'll see you have magic sum now.",
        "Some monsters have power to kill the magic.",
        "These monsters have their own special power.",
        "They have different features.",
        "The Leafies have leaf-feature.",
        "I just can tell you these informations. Good luck.",
        ]
