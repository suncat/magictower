#! /usr/bin/env python
#coding=utf-8
import pygame
import random

from consts import *
from npc import Npc
from msgbox import Msgbox
from choicebox import Choicebox


class Snake(Npc):
    images = ["snake.png"]

    def __init__(self, location):
        super(Snake, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        if player.snakerocknum == 0:
            self.kill()
            player.hurt(10)
            player.money += 1
            player.exp += 1


class MiddleSnake(Npc):
    images = ["middlesnake.png"]

    def __init__(self, location):
        super(MiddleSnake, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        if player.snakedp == 0:
            player.hurt(105)
            player.money += 4
            player.exp += 3
        else:
            if player.snakerocknum * 13 < 105:
                player.hurt(105 - player.snakerocknum * 13)
                player.money += 4
                player.exp += 3


class LargeSnake(Npc):
    images = ["largesnake.png"]

    def __init__(self, location):
        super(LargeSnake, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        if player.snakedp == 0:
            player.hurt(280)
            player.money += 8
            player.exp += 8
        else:
            if player.snakerocknum * 13 < 280:
                player.hurt(280 - player.snakerocknum * 13)
                player.money += 8
                player.exp += 8


class MagicSnake(Npc):
    images = ["magicsnake.png"]

    def __init__(self, location):
        super(MagicSnake, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        if player.snakedp == 0:
            player.hurt(300)
        else:
            if player.snakerocknum * 13 < 300:
                player.hurt(300 - player.snakerocknum * 13)
        player.money += 9
        player.exp += 8


class KingSnake(Npc):
    images = ["kingsnake.png"]

    def __init__(self, location):
        super(KingSnake, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        if player.snakedp == 0:
            player.hurt(350)
        else:
            if player.snakerocknum * 13 < 350:
                player.hurt(350 - player.snakerocknum * 13)
        for sprite in player.currentfloor.group:
            if isinstance(sprite, Switchdoor):
                sprite.kill()
        player.currentfloor.group.add(
            Largedprock((3.5 * CELL_SIZE, 3.5 * CELL_SIZE)),
            Largedprock((4.5 * CELL_SIZE, 3.5 * CELL_SIZE)),
            Middledrug((3.5 * CELL_SIZE, 4.5 * CELL_SIZE)),
            Middledrug((4.5 * CELL_SIZE, 4.5 * CELL_SIZE)),
            BlueKey((3.5 * CELL_SIZE, 5.5 * CELL_SIZE)),
            BlueKey((4.5 * CELL_SIZE, 5.5 * CELL_SIZE))
        )
        player.money += 10
        player.exp += 10
        if player.health > 0:
            Msgbox("No!!! How can you kill me! How can you be so terrible!").show()


class Butterfly(Npc):
    images = ["butterfly.png"]

    def __init__(self, location):
        super(Butterfly, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        player.hurt(80)
        player.money += 2
        player.exp += 2
            


class MidButterfly(Npc):
    images = ["midbutterfly.png"]

    def __init__(self, location):
        super(MidButterfly, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        player.hurt(150)
        player.money += 4
        player.exp += 4


class Soldier(Npc):
    images = ["soldier.png"]
    counter = 0

    def __init__(self, location):
        super(Soldier, self).__init__(location, (CELL_SIZE, CELL_SIZE))
        Soldier.counter += 1

    def do_collide(self, player):
        player.hurt(320)
        player.money += 9
        player.exp += 9
        self.kill()
        Soldier.counter -= 1
        if Soldier.counter == 0:
            player.currentfloor.show_greenkeys()


class MidSoldier(Npc):
    images = ["midsoldier.png"]

    def __init__(self, location):
        super(MidSoldier, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.hurt(420)
        player.money += 10
        player.exp += 10
        self.kill()


class LargeSoldier(Npc):
    images = ["largesoldier.png"]

    def __init__(self, location):
        super(LargeSoldier, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.hurt(500)
        player.money += 12
        player.exp += 12
        self.kill()


class Leafy(Npc):
    images = ["leafy.png"]

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


class Fleavey(Npc):
    images = ["fleavey.png"]

    def __init__(self, location):
        super(Fleavey, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        skill = random.randint(1, 1)
        if skill == 1:
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


class UpStair(Npc):
    images = ["upstair.png"]

    def __init__(self, location):
        super(UpStair, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.go_upstair()


class DownStair(Npc):
    images = ["downstair.png"]

    def __init__(self, location):
        super(DownStair, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.go_downstair()


class Wall(Npc):
    images = ["wall.png"]

    def __init__(self, location):
        super(Wall, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()


class Fakewall(Npc):
    images = ["wall.png"]

    def __init__(self, location):
        super(Fakewall, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        self.kill()


class Defencerock(Npc):
    images = ["defencerock.png"]

    def __init__(self, location):
        super(Defencerock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.defence += 8
        self.kill()


class MiddleDProck(Npc):
    images = ["middledprock.png"]

    def __init__(self, location):
        super(MiddleDProck, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.defence += 30
        self.kill()
        for group in self.groups():
            if isinstance(sprite, Trap):
                sprite.kill()
        Msgbox("You killed the trap, you are so clever.").show()


class Largedprock(Npc):
    images = ["largedprock.png"]

    def __init__(self, location):
        super(Largedprock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.defence += 60
        self.kill()


class SnakeRock(Npc):
    images = ["snakerock.png"]

    def __init__(self, location):
        super(SnakeRock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.snakerocknum += 1
        self.kill()


class Smallmagic(Npc):
    images = ["smallmagic.png"]

    def __init__(self, location):
        super(Smallmagic, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.magic += 90
        self.kill()


class Smalldrug(Npc):
    images = ["smalldrug.png"]

    def __init__(self, location):
        super(Smalldrug, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.health += 130
        self.kill()


class Middledrug(Npc):
    images = ["middledrug.png"]

    def __init__(self, location):
        super(Middledrug, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.health += 300
        self.kill()


class Largedrug(Npc):
    images = ["largedrug.png"]

    def __init__(self, location):
        super(Largedrug, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.health += 500
        self.kill()


class Firerock(Npc):
    images = ["firerock.png"]

    def __init__(self, location):
        super(Firerock, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.feature = "FIRE"
        self.kill()


class YellowKey(Npc):
    images = ["yellowkey.png"]

    def __init__(self, location):
        super(YellowKey, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.ykeynum += 1
        self.kill()


class BlueKey(Npc):
    images = ["bluekey.png"]

    def __init__(self, location):
        super(BlueKey, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.bkeynum += 1
        self.kill()


class GreenKey(Npc):
    images = ["greenkey.png"]

    def __init__(self,location):
        super(GreenKey, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.gkeynum += 1
        self.kill()


class NormalGkey(Npc):
    images = ["greenkey.png"]

    def __init__(self, location):
        super(NormalGkey, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.gkeynum += 1
        self.kill()



class YellowDoor(Npc):
    images = ["yellowdoor.png"]

    def __init__(self, location):
        super(YellowDoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        if player.ykeynum > 0:
            player.ykeynum -= 1
            self.kill()
        else:
            player.rect = player.oldpos


class RedDoor(Npc):
    images = ["reddoor.png"]

    def __init__(self, location):
        super(RedDoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        if player.rkeynum > 0:
            player.rkeynum -= 1
            self.kill()
        else:
            player.undo()


class BlueDoor(Npc):
    images = ["bluedoor.png"]

    def __init__(self, location):
        super(BlueDoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        if player.bkeynum > 0:
            player.bkeynum -= 1
            self.kill()
        else:
            player.undo()


class GreenDoor(Npc):
    images = ["greendoor.png"]

    def __init__(self, location):
        super(GreenDoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        if player.gkeynum > 0:
            player.gkeynum -= 1
            self.kill()
        else:
            player.undo()


class Specialdoor(Npc):
    images =["specialdoor.png"]

    def __init__(self, location):
        super(Specialdoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        if player.on_power:
            self.kill()


class Ftendoor(Npc):
    images = ["specialdoor.png"]

    def __init__(self, location):
        super(Ftendoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        for sprite in player.currentfloor.group:
            if isinstance(sprite, Ftendoor):
                sprite.kill()


class Switchdoor(Npc):
    images = ["specialdoor.png"]

    def __init__(self, location):
        super(Switchdoor, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()


class TopFloorGate(Npc):
    images = ["topfloorgate.png"]

    def __init__(self, location):
        super(TopFloorGate, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        if player.get_top == True:
            Msgbox("I'll let you go on the top floor...").show()
            self.kill()
        else:
            Msgbox("Go away, you're so weak!").show()
            player.undo()


class Oldman(Npc):
    images = ["oldman.png"]

    def __init__(self, location):
        super(Oldman, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        Msgbox("Do not think about everything is so easy. Mind traps.").show()
        self.kill()


class Franklin(Npc):
    images = ["franklin.png"]

    def __init__(self, location):
        super(Franklin, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        Msgbox("My name is Franklin.").show()
        Msgbox("And you'll see you have magic sum now.").show()
        Msgbox("Some monsters have power to kill the magic.").show()
        Msgbox("These monsters have their own special power.").show()
        Msgbox("They have different features.").show()
        Msgbox("The Leafies have leaf-feature.").show()
        Msgbox("I just can tell you these informations. Good luck.").show()
        self.kill()


class Trap(Npc):
    images = ["trap.png"]

    def __init__(self, location):
        super(Trap, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        player.kill()
        Msgbox("Game over!!!").show()


class MoneyShop(Npc):
    images = ["moneyshop.png"]

    def __init__(self, location):
        super(MoneyShop, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        d = {pygame.K_1:player.buy_y, pygame.K_2:player.buy_b, pygame.K_3:player.buy_r, pygame.K_4:player.buy_g}
        Choicebox(["Press 1 to buy a yellow key, $ 20.", 
                "Press 2 to buy a blue key, $ 30.", 
                "Press 3 to buy a red key, $ 50.", 
                "Press 4 to buy a green key, $ 80.",
                "Press other key to quit."]).show(player, d)


class SecondMoney(Npc):
    images = ["secondmoney.png"]

    def __init__(self, location):
        super(SecondMoney, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        d = {pygame.K_1:player.buy_y2, pygame.K_2:player.buy_b2, pygame.K_3: player.buy_r2, pygame.K_4: player.buy_g2}
        Choicebox(["Press 1 to buy five yellow keys, $ 80.",
                "Press 2 to buy five blue keys, $ 130.",
                "Press 3 to buy five red keys, $ 220.",
                "Press 4 to buy five green keys, $ 360.",
                "Press other key to quit."]).show(player, d)


class ExpShop(Npc):
    images = ["expshop.png"]

    def __init__(self, location):
        super(ExpShop, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        d = {pygame.K_1:player.buy_smalldr, pygame.K_2:player.buy_defrk, pygame.K_3:player.buy_snakerk, pygame.K_4:player.buy_level}
        Choicebox(["Press 1 to buy a small drug, EXP 20.",
                "Press 2 to buy a defencerock, EXP 20.",
                "Press 3 to buy a snakerock, EXP 20.",
                "Press 4 to buy a level, EXP 100.",
                "Press other key to quit."]).show(player, d)


class SecondExp(Npc):
    images = ["secondexp.png"]

    def __init__(self, location):
        super(SecondExp, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        player.undo()
        d = {pygame.K_1:player.buy_largedr, pygame.K_2:player.buy_largedef, pygame.K_3:player.buy_magic, pygame.K_4:player.buy_level2}
        Choicebox(["Press 1 to buy a large drug, EXP 70.",
                "Press 2 to buy a large defence, EXP 150.",
                "Press 3 to buy a magic jewer, EXP 80.",
                "Press 4 to buy three levels, EXP 270.",
                "Press other key to quit."]).show(player, d)


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