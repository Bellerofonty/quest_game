#-------------------------------------------------------------------------------
# Name:        Enemy
# Purpose:     Класс врага
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Warrior import *

class Enemy(Warrior):

    def __init__(self, name, health, armor, damage, lvl):
        super().__init__(name, health, armor, damage)
        self._experience_for_won = 50
        self._lvl = lvl

    def get_experience_for_won(self):
        return self._experience_for_won * self._lvl