#! /usr/bin/env python
#coding=utf-8
import character
import pygame

from consts import *


class Npc(character.Character):

    def __init__(self, location, realsize):
        super(Npc, self).__init__(location, realsize)

    def do_collide(self, player):
        pass
