#! /usr/bin/env python
#coding=utf-8
from npc import Npc


class Enemy(Npc):
    should_disappear = True
    hp = 0
    money = 0
    exp = 0

    def do_collide(self, player):
    	if callable(self.hp):
    		player.hurt(self.hp(player))
    	else:
    		player.hurt(self.hp)
    	player.money += self.money
    	player.exp += self.exp
    	if self.should_disappear:
    		self.kill()