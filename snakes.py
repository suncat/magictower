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
from enemy import Enemy
from character import load_images


class Snake(Enemy):
    images = load_images(["snake.png", "snake2.png"])
    _hp = 10
    money = 1
    exp = 1
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"

    def __init__(self, location):
        super(Snake, self).__init__(location, (CELL_SIZE, CELL_SIZE))

    @classmethod
    def hp(cls, player):
        return max(cls._hp - player.snakerocknum * 13, 0)


class MiddleSnake(Snake):
    images = load_images(["middlesnake.png", "middlesnake2.png"])
    _hp = 105
    money = 4
    exp = 3
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"


class LargeSnake(Snake):
    images = load_images(["largesnake.png", "largesnake2.png"])
    _hp = 280
    money = 8
    exp = 8
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"


class MagicSnake(Snake):
    images = load_images(["magicsnake.png", "magicsnake2.png"])
    _hp = 300
    money = 9
    exp = 8
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"


class KingSnake(Snake):
    images = load_images(["kingsnake.png", "kingsnake2.png"])
    _hp = 350
    money = 10
    exp = 10
    first_ften = True
    feature = 'None'
    skill = "NO"
    condition = "NORMAL"

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