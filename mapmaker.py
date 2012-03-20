#!/usr/bin/env python
from __future__ import division, with_statement
import pygame
import os.path
import sys
import csv

from consts import SCREEN_HEIGHT, CELL_SIZE, MAP_ROWS, MAP_COLS
from consts import games
from engine import Scene, Game
from msgbox import Msgbox
from floor import decrypt
from npcs import *

NPC_LIST = [
    Wall,
    Snake,
    UpStair,
    DownStair,
    Defencerock,
    Smalldrug,
    Butterfly,
    YellowKey,
    MiddleSnake,
    Middledrug,
    SnakeRock,
    YellowDoor,
    Oldman,
    Trap,
    MiddleDProck,
    MidButterfly,
    Soldier,
    MoneyShop,
    ExpShop,
    GreenKey,
    Fakewall,
    Specialdoor,
    MidSoldier,
    Largedprock,
    Largedrug,
    LargeSoldier,
    LargeSnake,
    RedDoor,
    BlueDoor,
    GreenDoor,
    TopFloorGate,
    NormalGkey,
    Ftendoor,
    MagicSnake,
    KingSnake,
    Switchdoor,
    BlueKey,
    Franklin,
    Leafy,
    Smallmagic,
    Fleavey,
    Firerock,
    SecondMoney,
    SecondExp,
    LargeButterfly,
    LightButterfly,
    SwordKey,
    SKeyKiller,
    Aquarock,
    Skyrock,
    Exlargedrug,
    Flowey,
]


def encrypt(string):
    return string


class Panel(object):
    def __init__(self, screen, rect, bgcolor):
        self.surface = screen.subsurface(rect)
        self.bgcolor = bgcolor
    
    def get_width(self):
        return self.surface.get_width()
    
    def draw(self):
        self.surface.fill(self.bgcolor)
        
selected = None

class Toolbox(Panel):
    WIDTH = 40
    HEIGHT = 40
    def __init__(self, screen, left, top, nrow, ncol, bgcolor):
        super(Toolbox, self).__init__(screen, (left, top, ncol*Toolbox.WIDTH+10, nrow*Toolbox.HEIGHT), bgcolor)
        self.nrow = nrow
        self.ncol = ncol
        self.tools = pygame.sprite.OrderedUpdates()
        self.loadtools()
        self.puttools()
        
    def loadtools(self):
        for cls in NPC_LIST:
            tool = cls((0, 0), (Toolbox.WIDTH, Toolbox.HEIGHT))
            self.tools.add(tool)
    
    def puttools(self):
        i = j = 0
        for tool in self.tools:
            tool.rect.move_ip((j*Toolbox.WIDTH+Toolbox.WIDTH/2, i*Toolbox.HEIGHT+Toolbox.HEIGHT/2))
            j += 1
            if j >= self.ncol:
                j = 0
                i += 1

    def draw(self):
        super(Toolbox, self).draw()
        self.tools.draw(self.surface)
        if selected is not None:
            pygame.draw.rect(self.surface, (255, 255, 255), selected.rect, 2)


    def on_click(self, x, y, button):
        global selected
        n = y // 40 * self.ncol + x // 40
        if n < len(self.tools.sprites()):
            selected = self.tools.sprites()[n]
            
        
class MapGrid(Panel):
    linecolor = (0, 0, 0)
    def __init__(self, floornum, *args, **kwargs):
        super(MapGrid, self).__init__(*args, **kwargs)
        self.floornum = floornum
        self.mapfile = os.path.join('map', 'floor%03d.dat' % floornum)
        self.group = pygame.sprite.RenderUpdates()
        self.sprites = []
        self.loadmap()
        
    def loadmap(self):
        if not os.path.exists(self.mapfile):
            for i in range(MAP_ROWS):
                for j in range(MAP_COLS):
                    self.sprites.append(None)
        else:
            with open(self.mapfile) as f:
                for i, line in enumerate(csv.reader(f)):
                    real_line = decrypt(line)
                    for j, cell in enumerate(real_line):
                        if cell:
                            loc = (j * CELL_SIZE + CELL_SIZE/2, 
                                   i * CELL_SIZE + CELL_SIZE/2)
                            npc = globals().get(cell)(loc)
                            self.group.add(npc)
                        else:
                            npc = None
                        self.sprites.append(npc)

    def draw(self):
        super(MapGrid, self).draw()
        for i in range(MAP_ROWS+1):
            pygame.draw.line(self.surface, self.linecolor, (0, i*CELL_SIZE), (MAP_COLS*CELL_SIZE, i*CELL_SIZE),3)
        for j in range(MAP_COLS+1):
            pygame.draw.line(self.surface, self.linecolor, (j*CELL_SIZE, 0), (j*CELL_SIZE, MAP_ROWS*CELL_SIZE),3)
        self.group.draw(self.surface)
        pygame.display.update()
    
    def on_click(self, x, y, button):
        global selected
        i = y // CELL_SIZE
        j = x // CELL_SIZE
        if j>=MAP_COLS:
            return
        n = i * MAP_COLS + j
        if button == 1:
            if self.sprites[n] is not None:
                self.group.remove(self.sprites[n])
            if selected is not None:
                sprite = selected.__class__((j*CELL_SIZE+CELL_SIZE/2, i*CELL_SIZE+CELL_SIZE/2))
                self.group.add(sprite)
                self.sprites[n] = sprite
        elif button == 3:
            if self.sprites[n] is not None:
                self.group.remove(self.sprites[n])
            self.sprites[n] = None
        
    def save_to_file(self):
        with open(self.mapfile, 'w') as f:
            l = []
            for i, sprite in enumerate(self.sprites):
                if sprite is not None:
                    l.append(sprite.__class__.__name__)
                else:
                    l.append('')
                if (i+1) % MAP_COLS == 0:
                    s = encrypt(','.join(l))
                    print >>f, s
                    l = []
        Msgbox("Save to %s ok" %  os.path.basename(self.mapfile)).show()
            
class MapEditScene(Scene):
    def __init__(self, screen, floornum):
        super(MapEditScene, self).__init__(screen)
        self.toolbox = Toolbox(screen, 0, 0, 12, 5, (100,200,200))
        self.mapgrid = MapGrid(
                floornum,
                screen,
                (
                    self.toolbox.get_width(),
                    0,
                    screen.get_width()-self.toolbox.get_width(),
                    screen.get_height()
                ),
                (200, 100, 100))
    
    def draw(self):
        self.toolbox.draw()
        self.mapgrid.draw()

    def response_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.mapgrid.save_to_file()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.pos[0] <= self.toolbox.get_width():
                self.toolbox.on_click(
                        event.pos[0],
                        event.pos[1],
                        event.button
                        )
            else:
                self.mapgrid.on_click(
                        event.pos[0]-self.toolbox.get_width(),
                        event.pos[1],
                        event.button
                        )
                

class MapMaker(Game):
    def response_event(self, event):
        self.current_scene.response_event(event)
    
    def draw(self):
        for scene in self.scenes:
            scene.draw()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python mapmaker.py <floornum>"
        sys.exit(1)
    floornum =  int(sys.argv[1])
    game = MapMaker(1000, SCREEN_HEIGHT, fps=15)
    scene1 = MapEditScene(game.screen, floornum)
    game.add_scene(scene1)
    games['DEFAULTGAME'] = game
    game.run()
