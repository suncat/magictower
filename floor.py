#! /usr/bin/env python
#coding=utf-8
from __future__ import with_statement
import pygame
import os.path
import csv

from consts import *
from npcs import *

def decrypt(string):
    return string
            

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
            for i, line in enumerate(csv.reader(f)):
                real_line = decrypt(line)
                for j, cell in enumerate(real_line):
                    if cell:
                        loc = (j * CELL_SIZE + CELL_SIZE/2, 
                               i * CELL_SIZE + CELL_SIZE/2)
                        npc = globals().get(cell)(loc)
                        if cell == 'GreenKey':
                            self.group_gk.add(npc)
                        else:
                            self.group.add(npc)
    
    def show_greenkeys(self):
        for gk in self.group_gk:
            self.group.add(gk)
