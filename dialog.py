import pygame
import sys
import os.path
import random

from consts import get_game

def draw_dialog(surface, rect, rect_color, frame_color, border_width=8, shadow_weight=12):
    rect = pygame.Rect(rect)
    frame = pygame.Rect(rect.left - border_width, rect.top - border_width, rect.w + 2 * border_width, rect.h + 2 * border_width)
    shadow = frame.move(shadow_weight, shadow_weight)
    if shadow_weight:
        pygame.draw.rect(surface, [0, 0, 0], shadow, 0)
    if border_width:
        pygame.draw.rect(surface, frame_color, frame, 0)
    pygame.draw.rect(surface, rect_color, rect, 0)
    

class Dialog(object):
    
    def __init__(self, rect, bgcolor, surface=None, closekey=pygame.K_RETURN, frame_color=(0,0,0), border_width=8, shadow_weight=12):
        self.surface = surface if surface else pygame.display.get_surface()
        self.rect = rect
        self.bgcolor = bgcolor
        self.frame_color = frame_color
        self.border_width = border_width
        self.shadow_weight = shadow_weight
        self.closekey = closekey
        self.closed = False

    def show(self):
        clock = pygame.time.Clock()
        while not self.closed:
            clock.tick(get_game().fps)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == self.closekey:
                    self.closed = True
                self.response_event(event)
            get_game().bgmusic()
            get_game().animate()
            get_game().draw()
            self.draw()
            pygame.display.update()
            
    def draw(self):
        draw_dialog(self.surface, self.rect, self.bgcolor, self.frame_color, self.border_width, self.shadow_weight)
        self.draw_content()
    
    def draw_content(self):
        pass
    
    def response_event(self, event):
        pass
