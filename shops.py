from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from choicebox import Choicebox
from character import load_images


class Shop(Npc):

    def do_collide(self, player):
        player.undo()
        Choicebox(self.msgs, keydict=self.funcdict).show()


class MoneyShop(Shop):
    images = load_images(["moneyshop.png"])
    funcdict = {pygame.K_1:'buy_y', pygame.K_2:'buy_b', pygame.K_3:'buy_r', pygame.K_4:'buy_g'}
    msgs = ["Press 1 to buy a yellow key, $ 20.", 
                "Press 2 to buy a blue key, $ 30.", 
                "Press 3 to buy a red key, $ 50.", 
                "Press 4 to buy a green key, $ 80.",
                "Press other key to quit."]


class SecondMoney(Shop):
    images = load_images(["secondmoney.png"])
    funcdict = {pygame.K_1:'buy_y2', pygame.K_2:'buy_b2', pygame.K_3: 'buy_r2', pygame.K_4:'buy_g2'}
    msgs = ["Press 1 to buy five yellow keys, $ 80.",
                "Press 2 to buy five blue keys, $ 130.",
                "Press 3 to buy five red keys, $ 220.",
                "Press 4 to buy five green keys, $ 360.",
                "Press other key to quit."]


class ExpShop(Shop):
    images = load_images(["expshop.png"])
    funcdict = {pygame.K_1:'buy_smalldr', pygame.K_2:'buy_defrk', pygame.K_3:'buy_snakerk', pygame.K_4:'buy_level'}
    msgs = ["Press 1 to buy a small drug, EXP 20.",
                "Press 2 to buy a defencerock, EXP 20.",
                "Press 3 to buy a snakerock, EXP 20.",
                "Press 4 to buy a level, EXP 100.",
                "Press other key to quit."]


class SecondExp(Shop):
    images = load_images(["secondexp.png"])
    funcdict = {pygame.K_1:'buy_largedr', pygame.K_2:'buy_largedef', pygame.K_3:'buy_magic', pygame.K_4:'buy_level2'}
    msgs = ["Press 1 to buy a large drug, EXP 70.",
                "Press 2 to buy a large defence, EXP 150.",
                "Press 3 to buy a magic jewer, EXP 80.",
                "Press 4 to buy three levels, EXP 270.",
                "Press other key to quit."]
