# coding:utf8
from __future__ import absolute_import
import pygame

from consts import CELL_SIZE
from npc import Npc
from doors import Switchdoor
from dprocks import Largedprock
from drugs import Middledrug
from keys import BlueKey
from msgbox import Msgbox


class Snake(Npc):
    images = ["snake.png", "snake2.png"]
    hp = 10
    bonus_money = 1
    bonus_exp = 1

    def __init__(self, location):
        super(Snake, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    def do_collide(self, player):
        self.kill()
        if player.snakerocknum * 13 < self.hp:
            player.hurt(self.hp - player.snakerocknum * 13)
        player.money += self.bonus_money
        player.exp += self.bonus_exp


class MiddleSnake(Snake):
    images = ["middlesnake.png", "middlesnake2.png"]
    hp = 105
    bonus_money = 4
    bonus_exp = 3


class LargeSnake(Snake):
    images = ["largesnake.png", "largesnake2.png"]
    hp = 280
    bonus_money = 8
    bonus_exp = 8


class MagicSnake(Snake):
    images = ["magicsnake.png", "magicsnake2.png"]
    hp = 300
    bonus_money = 9
    bonus_exp = 8


class KingSnake(Snake):
    images = ["kingsnake.png", "kingsnake2.png"]
    hp = 350
    bonus_money = 10
    bonus_exp = 10
    first_ften = True

    def do_collide(self, player):
        super(KingSnake, self).do_collide(player)
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
        if player.health > 0:
            Msgbox("No!!! How can you kill me! How can you be so terrible!").show()
