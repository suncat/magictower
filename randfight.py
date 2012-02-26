# coding:utf8
import easygui
import random
from fight import *


class Fighter(Fight):

    def __init__(self):
        super(Fighter, self).__init__(value)


class Player(Fight):

    def __init__(self):
        super(Fighter, self).__init__(value)

a=easygui.enterbox(msg="Input your name:")
b=easygui.buttonbox(
        msg="What do you want to do, "+a+" ?",
        choices=("FIGHT", "STORE", "LIST"))
if b=="FIGHT":
    life=True
    level=random.randint(0, 20)
    enemy=random.randint(0, 20)
    player = Player(level)
    fighter = Fighter(enemy)
    while life==True:
        if player.sped >= fighter.sped:
            randskil = random.randint(0, level / 4 + 2)
            randweap = random.randint(0, level / 5 + 1)
            randturn = random.randint(0, 1)
            if randturn == 0:
                c=easygui.msgbox(msg=player.skil[randskil])
            else:
                c=easygui.msgbox(msg=player.weap[randweap])