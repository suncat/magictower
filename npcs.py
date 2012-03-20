#! /usr/bin/env python
#coding=utf-8
from __future__ import absolute_import
import random

from consts import *
from character import load_images
from npc import Npc
from msgbox import Msgbox

from snakes import *
from butterflies import *
from soldiers import *
from doors import *
from dprocks import *
from drugs import *
from features import *
from keys import *
from magics import *
from shops import *
from stairs import *
from talkable import *
from walls import *
from enemy import Enemy


class Leafy(Enemy):
    hp = 500
    money = 13
    exp = 12
    images = load_images(["leafy.png", "leafy2.png"])
    feature = 'Grass'
    skill = "NO"
    condition = "NORMAL"

    def do_collide(self, player):
        if player.feature in ["FIRE", "SKY", "SNOW"]:
            player.weaken(10)
        else:
            player.weaken(20)
        super(Leafy, self).do_collide(player)


class Fleavey(Enemy):
    hp = 560
    money = 15
    exp = 15
    images = load_images(["fleavey.png", "fleavey2.png"])
    feature = 'Grass'
    skill = "GREEN AIR-SHOT"
    condition = "NORMAL"

    def do_collide(self, player):
        Msgbox("Skill: Green Air-Shot! Be careful!").show()
        miss = random.randint(1, 10)
        if miss == 1:
            Msgbox("The skill missed!").show()
        else:
            player.defence -= 50
            if player.feature in ["FIRE", "SKY", "SNOW"]:
                player.weaken(50)
            elif player.feature in ["WATER", "ELECTRIC"]:
                player.weaken(200)
            else:
                player.weaken(100)
            if player.defence < 0:
                player.defence = 0
        if player.feature in ["FIRE", "SKY", "SNOW"]:
            player.weaken(40)
        elif player.feature in ["WATER", "ELECTRIC"]:
            player.weaken(160)
        else:
            player.weaken(80)
        super(Fleavey, self).do_collide(player)


class SnakeRock(Npc):
    images = load_images(["snakerock.png"])

    def do_collide(self, player):
        player.snakerocknum += 1
        self.kill()


class TopFloorGate(Npc):
    images = load_images(["topfloorgate.png"])

    def do_collide(self, player):
        if player.get_top == True:
            Msgbox("I'll let you go on the top floor...").show()
            player.goto_floor(len(ALLMAP))
            self.kill()
        else:
            Msgbox("Go away, you're so weak!").show()
            player.undo()


class Trap(Npc):
    images = load_images(["trap.png"])

    def do_collide(self, player):
        self.kill()
        player.suicide()


class SKeyKiller(Npc):
    images = load_images(["skeykiller.png"])

    def do_collide(self, player):
        if player.speed != [0, 0]:
            player.ykeynum = player.ykeynum - 1 if player.ykeynum > 0 else 0
            player.bkeynum = player.bkeynum - 1 if player.bkeynum > 0 else 0
            player.rkeynum = player.rkeynum - 1 if player.rkeynum > 0 else 0
            player.gkeynum = player.gkeynum - 1 if player.gkeynum > 0 else 0
