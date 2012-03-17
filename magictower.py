#! /usr/bin/env python
#coding=utf-8
""" TODO
实现Player的移动动画效果。
不要直接指定角色的实际位置坐标，而是告诉程序在第几行第几列，由程序自己计算坐标值。
player死后，显示2个按钮，允许玩家选择重新开始或退出游戏。
减血时显示血量信息，最好能有动画效果。
杀死怪物时播放相应的音响效果。
将地图存入map.dat文件中，从文件中读取地图，而不是用常量。
开发一个地图设计程序，可以用鼠标设计地图并保存为map.dat文件。
"""
from __future__ import absolute_import
import pygame

from consts import *
from game import Game
from player import Player
from keys import *
from monsterguide import MonsterGuide


font = pygame.font.Font(None, 30)


class MagicTowerGame(Game):
    musics = ["Michael_Jackson_-_Billie_Jean.ogg", "Michael_Jackson_Thriller.ogg", "Michael_Jackson_-_Beat_It.ogg"]

    def extra_init(self):
        
        self.textboard = self.screen.subsurface(0, 0, TEXTBOARD_WIDTH, TEXTBOARD_HEIGHT)
        self.gameboard = self.screen.subsurface(TEXTBOARD_WIDTH, 0, GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT)
        
        initspeed = [0, 0]
        self.player = Player(initspeed, (CELL_SIZE/2, MAP_ROWS*CELL_SIZE-CELL_SIZE/2), self.gameboard)
        self.group_player = pygame.sprite.Group()
        self.group_player.add(self.player)
                
        self.ykey = YellowKey([10, 130], (25, 25))
        self.bkey = BlueKey([10, 160], (25, 25))
        self.rkey = RedKey([10, 190], (25, 25))
        self.gkey = GreenKey([10, 220], (25, 25))
        
    def response_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.speed = [0, -STEP]
            elif event.key == pygame.K_DOWN:
                self.player.speed = [0, STEP]
            elif event.key == pygame.K_LEFT:
                self.player.speed = [-STEP, 0]
            elif event.key == pygame.K_RIGHT:
                self.player.speed = [STEP, 0]
            elif event.key == pygame.K_EQUALS:
                if pygame.mixer.music.get_volume()<1.0:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.2)
            elif event.key == pygame.K_MINUS:
                if pygame.mixer.music.get_volume()>0.0:
                    if pygame.mixer.music.get_volume()<0.2:
                        pygame.mixer.music.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.2)
            elif event.key == pygame.K_ESCAPE:
                MonsterGuide(surface=self.gameboard).show(self.player, self.player.currentfloor)
        
    def update(self):
        self.group_player.update()
        self.player.currentfloor.group.update()
        
    def draw(self):
        gameboard = self.gameboard
        textboard = self.textboard
        # 填充背景
        gameboard.fill([255, 255, 255])
        textboard.fill([120, 120, 120])
        # 画人
        self.group_player.draw(gameboard)
        # 画当前楼层地图
        self.player.currentfloor.group.draw(gameboard)
        
        # 显示体力
        health_text = font.render("health: " + str(self.player.health), 1, (255, 0, 255))
        textpos = [10, 10]
        textboard.blit(health_text, textpos)
        # 显示防御
        defence_text = font.render("defence: " + str(self.player.defence), 1, (150, 0, 255))
        textpos2 = [10, 40]
        textboard.blit(defence_text, textpos2)
        # 显示楼层
        floor_text = font.render("floor: " + str(self.player.currentfloor.floornum), 1, (150, 255, 0))
        textpos3 = [10, 70]
        textboard.blit(floor_text, textpos3)
        # 显示黄钥匙
        textboard.blit(self.ykey.image, [10, 130])
        key_text = font.render(str(self.player.ykeynum), 1, (255, 255, 0))
        textpos4 = [40, 130]
        textboard.blit(key_text, textpos4)
        #显示蓝钥匙
        textboard.blit(self.bkey.image, [10, 160])
        key_text2 = font.render(str(self.player.bkeynum), 1, (0, 0, 255))
        textpos7 = [40, 160]
        textboard.blit(key_text2, textpos7)
        #显示红钥匙
        textboard.blit(self.rkey.image, [10, 190])
        key_text3 = font.render(str(self.player.rkeynum), 1, (255, 0, 0))
        textpos8 = [40, 190]
        textboard.blit(key_text3, textpos8)
        #显示绿钥匙
        textboard.blit(self.gkey.image, [10, 220])
        key_text4 = font.render(str(self.player.gkeynum), 1, (0, 255, 0))
        textpos9 = [40, 220]
        textboard.blit(key_text4, textpos9)
        # 显示蛇怪防御石
        snakerock_text = font.render("snakerock: " + str(self.player.snakerocknum), 1, (0, 255, 255))
        textpos5 = [10, 100]
        textboard.blit(snakerock_text, textpos5)
        # 显示金币
        money_text = font.render("money: " + str(self.player.money), 1, (0, 150, 0))
        moneypos = [10, 250]
        textboard.blit(money_text, moneypos)
        # 显示经验
        exp_text = font.render("exp: " + str(self.player.exp), 1, (0, 0, 100))
        expos = [10, 280]
        textboard.blit(exp_text, expos)
        # 显示等级
        lv_text = font.render("level: " + str(self.player.level), 1, (150, 0, 0))
        lvpos = [10, 310]
        textboard.blit(lv_text, lvpos)
        # 显示魔力值
        if self.player.currentfloor.floornum >= 11:
            mg_text = font.render("magic: " + str(self.player.magic), 1, (150, 0, 200))
            mgpos = [10, 340]
            textboard.blit(mg_text, mgpos)
        # 显示属性
        if self.player.currentfloor.floornum >= 11:
            ft_text = font.render("feature: " + str(self.player.feature), 1, (150, 200, 0))
            ftpos = [10, 370]
            textboard.blit(ft_text, ftpos)
        
if __name__ == '__main__':
    game = MagicTowerGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()