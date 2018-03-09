#-------------------------------------------------------------------------------
# Name:        Item
# Purpose:     Игровой предмет
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Item:
    def __init__(self, name, weight, value, stackable = False):
        self.name = name
        self.weight = weight
        self.value = value
        self.stackable = stackable
