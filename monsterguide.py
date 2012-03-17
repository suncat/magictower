#! /usr/bin/env python
#coding=utf-8
import pygame

from consts import get_game
from enemy import Enemy
from dialog import Dialog

class MonsterGuide(Dialog):

    def __init__(self, location=(0, 0), surface=None):
        Dialog.__init__(self, (0, 0, 640, 640), (200, 200, 200), surface, closekey=pygame.K_ESCAPE, border_width=0, shadow_weight=0)
        self.font = pygame.font.Font(None, 30)
        self.player = get_game().player
        self.x, self.y = location
        
    
    def draw_content(self):
        s = set()
        floor = self.player.currentfloor
        for enemy in floor.group:
            if isinstance(enemy, Enemy):
                s.add(enemy.__class__)
        for i, cls in enumerate(s):
            self.surface.blit(pygame.transform.scale(cls.images[0], (80, 80)), [30, 35 + i * 90])
            if callable(cls.hp):
                hpval = cls.hp(self.player)
            else:
                hpval = cls.hp
            attackmsg = self.font.render("power: %d" % hpval, 1, (255, 0, 0))
            self.surface.blit(attackmsg, [115, 35 + i * 90])
            moneyexpmsg = self.font.render("money/exp: %d/%d" % (cls.money, cls.exp), 1, (255, 255, 0))
            self.surface.blit(moneyexpmsg, [115, 65 + i * 90])
            featuremsg = self.font.render("feature: %s" % cls.feature, 1, (0, 0, 255))
            self.surface.blit(featuremsg, [115, 95 + i * 90])
            namemsg = self.font.render("name: %s" % cls.__name__, 1, (0, 255, 0))
            self.surface.blit(namemsg, [320, 35 + i * 90])
            skillmsg = self.font.render("skill: %s" % cls.skill, 1, (255, 0, 255))
            self.surface.blit(skillmsg, [320, 65 + i * 90])
            condmsg = self.font.render("condition: %s" % cls.condition, 1, (0, 255, 255))
            self.surface.blit(condmsg, [320, 95 + i * 90])