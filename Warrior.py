#-------------------------------------------------------------------------------
# Name:        Warrior
# Purpose:     Базовый класс воина
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Warrior:
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
        self._lvl = 1

    def _calculate_damage(self, enemy):
        return self.damage / enemy.armor

    def attack(self, enemy):
        enemy.health -= self._calculate_damage(enemy)

