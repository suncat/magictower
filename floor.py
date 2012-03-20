#! /usr/bin/env python
#coding=utf-8
from __future__ import with_statement
import pygame
import os.path
import csv

from consts import *
from npcs import NPC_DICT
from npcs import *


class Floor(object):

    def __init__(self, floornum):
        self.floornum = floornum
        self.group = pygame.sprite.Group()
        self.group_gk = pygame.sprite.Group()
        self.group_door = pygame.sprite.Group()
        self.group_ften = pygame.sprite.Group()
        self.loadmap()

    def loadmap(self):
        with open(os.path.join('map', 'floor%03d.dat' % self.floornum)) as f:
            m = f.readlines()
            self.decrypt(m)
        for i in range(MAP_ROWS):
            for j in range(MAP_COLS):
                loc = (j * CELL_SIZE + CELL_SIZE/2, 
                       i * CELL_SIZE + CELL_SIZE/2)
                k = m[i][j]
                npc_class = NPC_DICT.get(k)
                if npc_class:
                    if npc_class == GreenKey:
                        self.group_gk.add(npc_class(loc))
                    else:
                        self.group.add(npc_class(loc))
    
    def decrypt(self, map_):
        for i, s in enumerate(map_):
            map_[i] = s
            
    def show_greenkeys(self):
        for gk in self.group_gk:
            self.group.add(gk)
