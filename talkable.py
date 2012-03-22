from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from msgbox import Msgbox
from character import load_images


class Talkable(Npc):
    msgs = []

    def do_collide(self, player):
        for msg in self.msgs:
            Msgbox(msg).show()
        self.kill()

class Oldman(Talkable):
    images = load_images(["oldman.png"])
    msgs = ["Do not think about everything is so easy. Mind traps.",]

    def do_collide(self, player):
        if player.currentfloor.floornum == 5:
            super(Oldman, self).do_collide(player)
        elif player.currentfloor.floornum == 17:
            self.msgs = [
                "Oldman: The fairy on the 23rd floor is waiting for you.",
                "Worior: What? Waiting for me?",
                "Oldman: Right. She is looking for something.",
                "Oldman: And she need you to bring it.",
                "Worior: And could you tell me the thing?",
                "Oldman: Sorry, I don't know. You can go and ask her yourself.",
                "Worior: Can you help me to beat the monsters above us?",
                "Oldman: No, it is your stuff. Do it yourself.",
                "Oldman: But it's really difficult. Really. So good luck, boy.",
                "Worior: OK. Thanks...",
                ]
            super(Oldman, self).do_collide(player)


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
