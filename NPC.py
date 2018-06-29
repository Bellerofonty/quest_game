#-------------------------------------------------------------------------------
# Name:        NPC
# Purpose:     Класс неигрового персонажа. Не воин
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class NPC:
    def __init__(self, name, goods_type = 0, goods = set(), talk = 0):
        self.name = name
        self.goods_type = goods_type
        self.goods = goods.copy()
        self.talk = talk

##    def dialog(self):
##        with open('dialogs/' + self.name + '.txt') as f:
##            #for line in f:
##            while True:
##                line = f.readline()
##                #if line
##                print(line)
##                answer = input()