#-------------------------------------------------------------------------------
# Name:        Armor
# Purpose:     Броня
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Item import *

class Armor(Item):
    def __init__(self, name, weight, value, type, armor_points, stackable = False):
        super().__init__(name, weight, value, stackable = False)
        self.type = type
        self.armor_points = armor_points
        self.stackable = False
