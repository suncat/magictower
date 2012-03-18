from __future__ import division
import pygame

from consts import *
from engine import Scene, Game
from npcs import NPC_DICT


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
        keys = NPC_DICT.keys()
        keys.sort()
        for key in keys:
            tool = NPC_DICT[key]((0, 0), (Toolbox.WIDTH, Toolbox.HEIGHT))
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
    def __init__(self, *args, **kwargs):
        super(MapGrid, self).__init__(*args, **kwargs)
        self.group = pygame.sprite.RenderUpdates()
        self.sprites = []
        for i in range(MAP_ROWS * MAP_COLS):
            self.sprites.append(None)
        
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
        
            
class MapEditScene(Scene):
    def __init__(self, screen):
        super(MapEditScene, self).__init__(screen)
        self.toolbox = Toolbox(screen, 0, 0, 12, 5, (100,200,200))
        self.mapgrid = MapGrid(screen, (self.toolbox.get_width(), 0, screen.get_width()-self.toolbox.get_width(), screen.get_height()), (200, 100, 100))
    
    def draw(self):
        self.toolbox.draw()
        self.mapgrid.draw()

    def response_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.pos[0] <= self.toolbox.get_width():
                self.toolbox.on_click(event.pos[0], event.pos[1], event.button)
            else:
                self.mapgrid.on_click(event.pos[0]-self.toolbox.get_width(), event.pos[1], event.button)
                

class MapMaker(Game):
    def response_event(self, event):
        self.current_scene.response_event(event)
    
    def draw(self):
        for scene in self.scenes:
            scene.draw()

if __name__ == '__main__':
    game = MapMaker(1000, SCREEN_HEIGHT, fps=15)
    scene1 = MapEditScene(game.screen)
    game.add_scene(scene1)
    game.current_scene = scene1
    games['DEFAULTGAME'] = game
    game.run()