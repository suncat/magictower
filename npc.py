#! /usr/bin/env python
#coding=utf-8
import character
import pygame

from consts import *


class Npc(character.Character):

    def __init__(self, image_file, location, realsize):
        super(Npc, self).__init__(image_file, location, realsize)

    def do_collide(self, player):
        pass
