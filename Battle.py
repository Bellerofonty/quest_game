#-------------------------------------------------------------------------------
# Name:        Battle
# Purpose:     Класс битвы
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Battle:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        print('Началась драка')
        self._player.armor = 1 + self._player.count_armor()
        #print(self._player.armor)
        last_attacker = self._player
        while self._player.health > 0 and self._enemy.health > 0:
            if last_attacker == self._player:
                self._enemy.attack(self._player)
                last_attacker = self._enemy
            else:
                self._player.attack(self._enemy)
                last_attacker = self._player
        if self._player.health > 0:
            print('Игрок победил')
            #self._player.battle_won(enemy.get_experience_for_won())
            # Система опыта и уровней не реализована
        else:
            print('Враг победил')
        self._player.health = 100
        self._enemy.health = 100