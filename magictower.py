#! /usr/bin/env python
#coding=utf-8
""" TODO
$ 碰到蛇时，蛇消失。
$ 蛇消失后，玩家体力扣除10点。
$ 蛇全部消失后，屏幕右上角出现一个向上箭头。
$ 碰到第一层的向上箭头后，升至第二层。
$ 升至第二层后，屏幕左下角出现一个向下箭头。
$ 升至第二层后，玩家移至向下箭头旁边。
$ 碰到第二层的向下箭头后，降至第一层。
$ 四条同样的蛇。
$ snakerock的错误情况纠正。
$ 钱商店和经验商店。
$ 杀死蛇王后，弹出对话框，switchdoors消失。
$ 实现所有角色的动画效果。
$ 目前文件太多太乱，不易管理，应该将所有图片文件放到image目录下，所有声音文件放到sound目录下。
$ npcs.py中的类太多，不易管理，应重新设计类之间的继承关系，将不同类型的NPC抽象出几个基类，如Enemy, Stair, Door, Key, Shop, Drug等，在此基础上分别派生出所有的子类，可以有多层继承关系，将子类的共同代码放入基类中，同时将npcs.py按此原则分割为多个模块。
$ 钥匙直接画出来。
$ 在屏幕上放一个声音开关按钮和音量调节按钮。
$ 背景音乐随机播放不同的音乐，一首放完后自动切换到另一首。
$ 美化MsgBox, ChoiceBox的显示效果。
$ MsgBox可以看成ChoiceBox的一种特殊情况，将MsgBox改写为ChoiceBox的子类。
实现Player的移动动画效果。
不要直接指定角色的实际位置坐标，而是告诉程序在第几行第几列，由程序自己计算坐标值。
player死后，显示2个按钮，允许玩家选择重新开始或退出游戏。
减血时显示血量信息，最好能有动画效果。
杀死怪物时播放相应的音响效果。
将地图存入map.dat文件中，从文件中读取地图，而不是用常量。
开发一个地图设计程序，可以用鼠标设计地图并保存为map.dat文件。
"""
import pygame
import sys
import random

from consts import *
from player import Player
from npcs import *
from keys import *
from monsterguide import MonsterGuide


def randmusic():
    music = random.choice(musics)
    pygame.mixer.music.load("sound/" + music)
    pygame.mixer.music.play()

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
#pygame.time.delay(1000)
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
textboard = screen.subsurface(0, 0, TEXTBOARD_WIDTH, TEXTBOARD_HEIGHT)
gameboard = screen.subsurface(TEXTBOARD_WIDTH, 0, GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT)
#pygame.time.delay(1000)

initspeed = [0, 0]
player = Player(initspeed, (CELL_SIZE/2, MAP_ROWS*CELL_SIZE-CELL_SIZE/2),gameboard)
group_player = pygame.sprite.Group()
group_player.add(player)

#group_dic = {}

musics = ["Michael_Jackson_-_Billie_Jean.ogg", "Michael_Jackson_Thriller.ogg", "Michael_Jackson_-_Beat_It.ogg"]
randmusic()
pygame.mixer.music.set_endevent(EVENT_MUSIC_END)

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == EVENT_MUSIC_END:
            randmusic()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speed = [0, -STEP]
            elif event.key == pygame.K_DOWN:
                player.speed = [0, STEP]
            elif event.key == pygame.K_LEFT:
                player.speed = [-STEP, 0]
            elif event.key == pygame.K_RIGHT:
                player.speed = [STEP, 0]
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
                MonsterGuide(surface=gameboard).show(player, player.currentfloor)
                

    group_player.update()
    player.currentfloor.group.update()

    # 填充背景
    gameboard.fill([255, 255, 255])
    textboard.fill([120, 120, 120])
    # 画人
    group_player.draw(gameboard)
    # 画当前楼层地图
    player.currentfloor.group.draw(gameboard)
    # 显示体力
    font = pygame.font.Font(None, 30)
    health_text = font.render("health: " + str(player.health), 1, (255, 0, 255))
    textpos = [10, 10]
    textboard.blit(health_text, textpos)
    # 显示防御
    defence_text = font.render("defence: " + str(player.defence), 1, (150, 0, 255))
    textpos2 = [10, 40]
    textboard.blit(defence_text, textpos2)
    # 显示楼层
    floor_text = font.render("floor: " + str(player.currentfloor.floornum), 1, (150, 255, 0))
    textpos3 = [10, 70]
    textboard.blit(floor_text, textpos3)
    # 显示黄钥匙
    ykey = YellowKey([10, 130], (25, 25))
    textboard.blit(ykey.image, [10, 130])
    key_text = font.render(str(player.ykeynum), 1, (255, 255, 0))
    textpos4 = [40, 130]
    textboard.blit(key_text, textpos4)
    #显示蓝钥匙
    bkey = BlueKey([10, 160], (25, 25))
    textboard.blit(bkey.image, [10, 160])
    key_text2 = font.render(str(player.bkeynum), 1, (0, 0, 255))
    textpos7 = [40, 160]
    textboard.blit(key_text2, textpos7)
    #显示红钥匙
    rkey = RedKey([10, 190], (25, 25))
    textboard.blit(rkey.image, [10, 190])
    key_text3 = font.render(str(player.rkeynum), 1, (255, 0, 0))
    textpos8 = [40, 190]
    textboard.blit(key_text3, textpos8)
    #显示绿钥匙
    gkey = GreenKey([10, 220], (25, 25))
    textboard.blit(gkey.image, [10, 220])
    key_text4 = font.render(str(player.gkeynum), 1, (0, 255, 0))
    textpos9 = [40, 220]
    textboard.blit(key_text4, textpos9)
    # 显示蛇怪防御石
    snakerock_text = font.render("snakerock: " + str(player.snakerocknum), 1, (0, 255, 255))
    textpos5 = [10, 100]
    textboard.blit(snakerock_text, textpos5)
    # 显示金币
    money_text = font.render("money: " + str(player.money), 1, (0, 150, 0))
    moneypos = [10, 250]
    textboard.blit(money_text, moneypos)
    # 显示经验
    exp_text = font.render("exp: " + str(player.exp), 1, (0, 0, 100))
    expos = [10, 280]
    textboard.blit(exp_text, expos)
    # 显示等级
    lv_text = font.render("level: " + str(player.level), 1, (150, 0, 0))
    lvpos = [10, 310]
    textboard.blit(lv_text, lvpos)
    # 显示魔力值
    if player.currentfloor.floornum >= 11:
        mg_text = font.render("magic: " + str(player.magic), 1, (150, 0, 200))
        mgpos = [10, 340]
        textboard.blit(mg_text, mgpos)
    # 显示属性
    if player.currentfloor.floornum >= 11:
        ft_text = font.render("feature: " + str(player.feature), 1, (150, 200, 0))
        ftpos = [10, 370]
        textboard.blit(ft_text, ftpos)
    # 刷新屏幕
    pygame.display.flip()
