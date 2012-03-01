# coding:utf8
from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc


class MidSoldier(Npc):
    images = ["midsoldier.png"]
    hp = 420
    money = 10
    exp = 10

    def __init__(self, location):
        super(MidSoldier, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.hurt(self.hp)
        player.money += self.money
        player.exp += self.exp
        self.kill()


class Soldier(MidSoldier):
    images = ["soldier.png"]
    counter = 0
    hp = 320
    money = 9
    exp = 9

    def do_collide(self, player):
        super(Soldier, self).do_collide(player)
        Soldier.counter -= 1
        if Soldier.counter == 0:
            player.currentfloor.show_greenkeys()


class LargeSoldier(MidSoldier):
    images = ["largesoldier.png"]
    hp = 500
    money = 12
    exp = 12
