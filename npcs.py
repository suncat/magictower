#! /usr/bin/env python
#coding=utf-8
from __future__ import absolute_import
import pygame
import random

from consts import *
from character import load_images
from npc import Npc
from msgbox import Msgbox
from choicebox import Choicebox
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
    images = load_images(["leafy.png", "leafy2.png"])
    feature = 'Grass'

    def __init__(self, location):
        super(Leafy, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.hurt(500)
        if player.feature == "FIRE":
            player.weaken(10)
        else:
            player.weaken(20)
        player.money += 13
        player.exp += 12
        self.kill()


class Fleavey(Enemy):
    images = load_images(["fleavey.png"])
    feature = 'Grass'

    def __init__(self, location):
        super(Fleavey, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        Msgbox("Skill: Green Air-Shot! Be careful!").show()
        miss = random.randint(1, 10)
        if miss == 1:
            Msgbox("The skill missed!").show()
        else:
            player.defence -= 50
            if player.feature == "FIRE":
                player.weaken(50)
            else:
                player.weaken(100)
            player.hurt(560)
            if player.defence < 0:
                player.defence = 0
            player.flash_image("greenairshotwor.png", 2000)
        player.hurt(560)
        if player.feature == "FIRE":
            player.weaken(40)
        else:
            player.weaken(80)
        player.money += 15
        player.exp += 15
        self.kill()


class SnakeRock(Npc):
    images = load_images(["snakerock.png"])

    def __init__(self, location):
        super(SnakeRock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.snakerocknum += 1
        self.kill()


class TopFloorGate(Npc):
    images = load_images(["topfloorgate.png"])

    def __init__(self, location):
        super(TopFloorGate, self).__init__(location, (CELL_SIZE, CELL_SIZE))

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

    def __init__(self, location):
        super(Trap, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        player.suicide()

NPC_DICT = {
    '1': Wall,
    '2': Snake,
    '3': UpStair,
    '4': DownStair,
    '6': Defencerock,
    '7': Smalldrug,
    '8': Butterfly,
    '9': YellowKey,
    'a': MiddleSnake,
    'b': Middledrug,
    'c': SnakeRock,
    'd': YellowDoor,
    'e': Oldman,
    'f': Trap,
    'g': MiddleDProck,
    'h': MidButterfly,
    'i': Soldier,
    'j': MoneyShop,
    'k': ExpShop,
    'l': GreenKey,
    'm': Fakewall,
    'n': Specialdoor,
    'o': MidSoldier,
    'p': Largedprock,
    'q': Largedrug,
    'r': LargeSoldier,
    's': LargeSnake,
    't': RedDoor,
    'u': BlueDoor,
    'v': GreenDoor,
    'w': TopFloorGate,
    'x': NormalGkey,
    'y': Ftendoor,
    'z': MagicSnake,
    'A': KingSnake,
    'B': Switchdoor,
    'C': BlueKey,
    'D': Franklin,
    'E': Leafy,
    'F': Smallmagic,
    'G': Fleavey,
    'H': Firerock,
    'I': SecondMoney,
    'J': SecondExp
}