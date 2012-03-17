# coding:utf8
from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from enemy import Enemy
from character import load_images


class MidSoldier(Enemy):
    images = load_images(["midsoldier.png", "midsoldier2.png"])
    hp = 420
    money = 10
    exp = 10
    feature = 'None'
    skill = "NO"

    def __init__(self, location):
        super(MidSoldier, self).__init__(location, (CELL_SIZE, CELL_SIZE))


class Soldier(MidSoldier):
    images = load_images(["soldier.png", "soldier2.png"])
    counter = 0
    hp = 320
    money = 9
    exp = 9
    feature = 'None'
    skill = "NO"

    def do_collide(self, player):
        super(Soldier, self).do_collide(player)
        Soldier.counter -= 1
        if Soldier.counter == 0:
            player.currentfloor.show_greenkeys()


class LargeSoldier(MidSoldier):
    images = load_images(["largesoldier.png", "largesoldier2.png"])
    hp = 500
    money = 12
    exp = 12
    feature = 'None'
    skill = "NO"