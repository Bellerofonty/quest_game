#-------------------------------------------------------------------------------
# Name:        Player
# Purpose:     Класс игрока
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Warrior import *

class Player(Warrior):

    def __init__(self, name, health, armor, damage, money = 0, items = set(), \
        slots = {'head': 0, 'body':0, 'legs': 0, 'left_arm': 0, 'right_arm': 0},
        locs_visited = set()):
        super().__init__(name, health, armor, damage)
        self.money = money
        self.items = items.copy()
        self.slots = slots
        self.locs_visited = locs_visited.copy()
        self._experience = 0
        self._exp_to_next_level = 100

    def _is_next_lvl(self):
        """(Не реализовано) Проверяет, хватает ли опыта для нового уровня"""
        if self._experience >= self._exp_to_next_level:
            self._lvl += 1
            self._exp_to_next_level *= 2

    def battle_won(self, experience_count):
        """(Не реализовано) Добавляет опыт при победе.
        Проверяет, хватает ли опыта для нового уровня"""
        self._experience += experience_count
        self._is_next_lvl()

    def count_armor(self):
        """Вычисляет сумму очков экипированной брони"""
        armor_sum = 0
        for i in self.slots:
            if self.slots[i]:
                armor_sum += self.slots[i].armor_points
        return armor_sum

    def add_money(self, ammount):
        self.money += ammount

    def subtract_money(self,ammount):
        self.money -= ammount

    def add_item(self, item):
        """Добавить предмет в инвентарь"""
        self.items.add(item)

    def use_item(self, item):
        """Поместить предмет из инвентаря в слот.
        Другое использование будет добавлено"""
        if hasattr(item, 'type'):
            self.slots[item.type] = item
            self.items.remove(item)
        else:
            print('\nНельзя использовать')

    def show_items(self):
        """Посмотреть предметы в инвентаре.
        Выйти (пустой input) либо исползовать предмет
        """
        if self.items:
            print('Инвентарь:')
            j = 1
            tmp_items = list(self.items)
            for i in tmp_items:
                print('{}: {}'.format(j, i.name))
                j += 1
            print('{} монет'.format(self.money))
            choice = int(input())
            try:
                if choice != 0 and tmp_items[choice - 1]:
                    self.use_item(tmp_items[choice - 1])
            except (IndexError, ValueError):
                pass
        else:
            print('Инвентарь пуст')
            print('{} монет'.format(self.money))

    def show_slots(self):
        """Посмотреть предметы в слотах.
        Выйти (пустой input) либо снять предмет и положить в инвентарь"""
        slot_numbers = dict()
        num = 1
        for i in self.slots:
            if self.slots[i]:
                print(num, i, self.slots[i].name, self.slots[i].armor_points)
                slot_numbers[num] = self.slots[i].type
                num += 1
        try:
            choice = int(input())
            if slot_numbers[choice]:
                self.items.add(self.slots[slot_numbers[choice]])
                self.slots[slot_numbers[choice]] = 0
        except (ValueError, KeyError):
            pass
