from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from msgbox import Msgbox
from character import load_images


class Talkable(Npc):

    def __init__(self, location):
        super(Talkable, self).__init__(location, (CELL_SIZE, CELL_SIZE))
        self.index = -1

    def do_collide(self, player):
        for msg in self.msgs:
            Msgbox(msg).show()
        self.kill()

class Oldman(Talkable):
    images = load_images(["oldman.png"])
    msgs = ["Do not think about everything is so easy. Mind traps.",]


class Franklin(Talkable):
    images = load_images(["franklin.png"])
    msgs = [
        "My name is Franklin.",
        "And you'll see you have magic sum now.",
        "Some monsters have power to kill the magic.",
        "These monsters have their own special power.",
        "They have different features.",
        "The Leafies have leaf-feature.",
        "I just can tell you these informations. Good luck.",
        ]

    def do_collide(self, player):
        if player.currentfloor.floornum == 11:
            super(Franklin, self).do_collide(player)
        elif player.currentfloor.floornum == 14:
            self.msgs = [
                "Worior: It's you! We're meet again!",
                "Franklin: Yep. I just want to tell you about the sword.",
                "Worior: The sword on the 13th floor?",
                "Franklin: You know it! You will use it to open a strange door.",
                "Worior: Which door?",
                "Franklin: It is...",
                "(Suddenly some smelly grass-smells come.)",
                "Franklin: Sorry, I can't bear the grass smell here. I must go.",
                "Worior: Oh no, please wait...",
                "Worior: Dad gone it! I must look for him later.",
                ]
            super(Franklin, self).do_collide(player)
