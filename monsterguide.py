#! /usr/bin/env python
#coding=utf-8
import pygame, sys
from enemy import Enemy


class MonsterGuide(pygame.sprite.Sprite):

    def __init__(self, location=(0, 0), surface=None):
        self.font = pygame.font.Font(None, 30)
        self.surface = surface if surface else pygame.display.get_surface()
        self.x, self.y = location

    def show(self, floor):
        pygame.draw.rect(self.surface, [0, 255, 255], [0, 0, 640, 480], 0)
        s = set()
        for enemy in floor.group:
            if isinstance(enemy, Enemy):
                s.add(enemy)
        for i, cls in enumerate(s):
            self.surface.blit(cls.image, [30, 30 + i * 80])
            attackmsg = self.font.render("power: " + str(cls.hp), 1, (0, 0, 0))
            self.surface.blit(attackmsg, [110, 30 + i * 80])
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
