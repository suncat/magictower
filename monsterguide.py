#! /usr/bin/env python
#coding=utf-8
import pygame, sys
from enemy import Enemy


class MonsterGuide(pygame.sprite.Sprite):

    def __init__(self, location=(0, 0), surface=None):
        self.font = pygame.font.Font(None, 30)
        self.surface = surface if surface else pygame.display.get_surface()
        self.x, self.y = location

    def show(self, player, floor):
        pygame.draw.rect(self.surface, [0, 255, 255], [0, 0, 640, 480], 0)
        s = set()
        for enemy in floor.group:
            if isinstance(enemy, Enemy):
                s.add(enemy.__class__)
        for i, cls in enumerate(s):
            self.surface.blit(pygame.transform.scale(cls.images[0], (80, 80)), [30, 35 + i * 90])
            if callable(cls.hp):
                hpval = cls.hp(player)
            else:
                hpval = cls.hp
            attackmsg = self.font.render("power: " + str(hpval), 1, (0, 0, 0))
            self.surface.blit(attackmsg, [115, 35 + i * 90])
            moneyexpmsg = self.font.render("money/exp: " + str(cls.money) + " / " + str(cls.exp), 1, (0, 0, 0))
            self.surface.blit(moneyexpmsg, [115, 65 + i * 90])
            featuremsg = self.font.render("feature: " + cls.feature, 1, (0, 0, 0))
            self.surface.blit(featuremsg, [115, 95 + i * 90])
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
