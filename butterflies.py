# coding:utf8
from __future__ import absolute_import
import pygame
import random

from consts import CELL_SIZE
from npc import Npc
from enemy import Enemy
from character import load_images
from msgbox import Msgbox


class Butterfly(Enemy):
    images = load_images(["butterfly.png", "butterfly2.png"])
    hp = 80
    money = 2
    exp = 2
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"

    def __init__(self, location):
        super(Butterfly, self).__init__(location, (CELL_SIZE, CELL_SIZE))


class MidButterfly(Butterfly):
    images = load_images(["midbutterfly.png", "midbutterfly2.png"])
    hp = 150
    money = 4
    exp = 4
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"


class LargeButterfly(Butterfly):
    images = load_images(["largebutterfly.png", "largebutterfly2.png"])
    hp = 550
    money = 13
    exp = 13
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"


class LightButterfly(Butterfly):
    images = load_images(["lightbutterfly.png", "lightbutterfly2.png"])
    hp = 960
    money = 20
    exp = 19
    feature = 'LIGHT'
    skill = "LIGHTNING-BOMB"
    condition = "NORMAL"

    def do_collide(self, player):
        Msgbox("Skill: Lightning-Bomb! Be careful!").show()
        miss = random.randint(1, 10)
        if miss == 1:
            Msgbox("The skill missed!").show()
        else:
            if player.feature in ["GRASS", "SOIL"]:
                player.weaken(120)
            elif player.feature in ["WATER", "SKY", "DARK"]:
                player.weaken(480)
                player.hurt(100)
            else:
                player.weaken(240)
        super(LightButterfly, self).do_collide(player)