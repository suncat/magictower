#! /usr/bin/env python
#coding=utf-8
from __future__ import absolute_import
import random
import time

from consts import *
from character import load_images
from npc import Npc, GrassMixin
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
from keykiller import *
from spider import *
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
            Msgbox("The skill hit!").show()
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


class Flowey(Enemy, GrassMixin):
    hp = 570
    money = 14
    exp = 13
    images = load_images(["flowey.png", "flowey2.png"])
    skill = "FLOWERBED-MACHINEGUN"
    condition = "POISON"

    def do_collide(self, player):
        player.poison()
        Msgbox("Skill: Flowerbed-machinegun! Too much shooting...").show()
        misscount = 1
        hitcount = 1
        for i in range(1, 6):
            miss = random.randint(1, 10)
            if miss == 1:
                if misscount == 1:
                    Msgbox("The skill missed!").show()
                else:
                    Msgbox("The skill missed again!").show()
                misscount += 1
            else:
                if hitcount == 1:
                    Msgbox("The skill hit!").show()
                else:
                    Msgbox("The skill hit again!").show()
                hitcount += 1
                player.defence -= 40
                if player.feature in ["FIRE", "SKY", "SNOW"]:
                    player.weaken(20)
                    player.hurt(25)
                elif player.feature in ["WATER", "ELECTRIC"]:
                    player.weaken(80)
                    player.hurt(100)
                else:
                    player.weaken(40)
                    player.hurt(50)
                if player.defence < 0:
                    player.defence = 0
        if player.feature in ["FIRE", "SKY", "SNOW"]:
            player.weaken(60)
        elif player.feature in ["WATER", "ELECTRIC"]:
            player.weaken(240)
        else:
            player.weaken(120)
        super(Flowey, self).do_collide(player)


class Bloompire(Enemy, GrassMixin):
    hp = 600
    money = 15
    exp = 15
    images = load_images(["bloompire.png", "bloompire2.png"])
    skill = "HONEY-BLOOM-IMAGINATION"
    condition = "DIZZY"

    def do_collide(self, player):
        player.dizzy()
        Msgbox("Skill: Honey-bloom-imagination! I feel so dizzy!").show()
        miss = random.randint(1, 5)
        if miss == 1:
            Msgbox("The skill missed, but maybe come again!").show()
            again = random.randint(1, 5)
            if again == 1:
                self.do_collide(player)
            else:
                Msgbox("Hush, the skill didn't come again.").show()
        else:
            Msgbox("The skill hit!").show()
            player.defence -= 250
            if player.feature in ["FIRE", "SKY", "SNOW"]:
                player.weaken(100)
                player.hurt(120)
            elif player.feature in ["WATER", "ELECTRIC"]:
                player.weaken(400)
                player.hurt(480)
            else:
                player.weaken(200)
                player.hurt(240)
            if player.defence < 0:
                player.defence = 0
        if player.feature in ["FIRE", "SKY", "SNOW"]:
            player.weaken(320)
        elif player.feature in ["WATER", "ELECTRIC"]:
            player.weaken(1280)
        else:
            player.weaken(640)
        super(Bloompire, self).do_collide(player)
        Msgbox("Huh, don't be happy so early.").show()


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


class FlyFloor(Npc):
    images = load_images(["flyfloor.png"])

    def do_collide(self, player):
        player.flyable = True
