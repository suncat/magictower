# coding:utf8
from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from enemy import Enemy
from character import load_images


class Butterfly(Enemy):
    images = load_images(["butterfly.png", "butterfly2.png"])
    hp = 80
    money = 2
    exp = 2
    feature = 'None'

    def __init__(self, location):
        super(Butterfly, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        player.hurt(self.hp)
        player.money += self.money
        player.exp += self.exp
            


class MidButterfly(Butterfly):
    images = load_images(["midbutterfly.png", "midbutterfly2.png"])
    hp = 150
    money = 4
    exp = 4
    feature = 'None'

