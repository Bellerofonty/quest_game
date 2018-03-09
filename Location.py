#-------------------------------------------------------------------------------
# Name:        Location
# Purpose:     Локация и действия в ней
#
# Author:      Daniil
#
# Created:     09.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import time
import json

from Battle import *
from Armor import *

class Location:
    def __init__(self, name, player, npc = 0, enemy = 0, where_to_go = set(),
        items = {}, is_inn = 0):
        self.name = name
        self.npc = npc
        self.enemy = enemy
        self.where_to_go = where_to_go.copy()
        self.items = items.copy()
        self.player = player
        self.is_inn = is_inn

    def talk_to_npc(self, npc):
        # Чтение словаря с диалогом из файла
        path = os.path.join('dialogs', npc.name + '.txt')
        with open(path, "r") as file:
            dialog = json.load(file)

        phrase_code = 'begin'
##        exit_loop = 0
        while True:
            """Структура фразы:
            Код фразы: [кто говорит/ключевое слово "code"[0],
            фраза/ключевая фраза[1], код следующей фразы/список кодов[2]]
            """
            phrase = dialog[phrase_code]
            # Действия по ключевым фразам
            if phrase[0] == 'code':
                if phrase[1] == 'exit_loop':
                    break
                elif phrase[1] == 'trade':
                    self.trade(npc)
                elif phrase[1] == 'repairs':
                    print('-repairing-') # Заглушка
                elif phrase[1] == 'fight':
                    tmp_enemy = Enemy('Враг', 100, 1.2, 10, 2)
                    self.start_battle(self.player, tmp_enemy)
##                exec(phrase[1])
            else:
                # Кто и что говорит
                print('--{}--\n{}'.format(phrase[0], phrase[1]))
##            if exit_loop:
##                break
            if type(phrase[2]) is not list: # Не вилка
                phrase_code = phrase[2]
            else:   # Вилка
                input()
                print('')
                fork = phrase[2]
                print('--{}--'.format(dialog[fork[0]][0])) # Имя игрока
                for num, i in enumerate(fork): # Варианты реплик игрока
                    print(num + 1, dialog[i][1])
            choice = input()
            try:
                choice = int(choice)
            except ValueError:
                pass # Пустой ввод - далее
##            if choice == 0:
##                    sys.exit()
            if choice:
                try:
                    # Код фразы, следующей за выбранной пользователем
                    phrase_code = dialog[phrase[2][choice - 1]][2]
                except KeyError:
                    pass
            print('')
            time.sleep(0.1)

##            # Старый формат диалога
##        print('Вы приветствуете NPC {}'.format(self.npc.name))
##        if self.npc.talk:
##            print('{} не против поговорить(1)'.format(self.npc.name))
##            self.npc.dialog()
##        if self.npc.goods_type:
##            print('{} предлагает поторговать {}(2)'.format(self.npc.name, self.npc.goods_type))
##        answer = input()
##        if answer == '2':
##            self.trade(self.npc)

    def trade(self, npc):
        """Торговля с NPC"""
        if npc.goods:
            # Показать товары. Если это броня, то с очками брони
            goods = list(npc.goods)
            for num, i in enumerate(goods, start = 1):
                if isinstance(i, Armor):
                    print(num, i.name, i.armor_points, i.value)
                else:
                    print(num, i.name, i.value)
            try:
                choice = int(input()) - 1
                item = goods[choice]
                if item:
                    if self.player.money >= item.value:
                        print('\n{} куплен'.format(item.name))
                        self.player.items.add(item)
                        self.npc.goods.remove(item)
                        self.player.money -= item.value
                    else:
                        print('Денег маловато')
            except ValueError:
                return # Пустой input - выйти из торговли

        else:
            print('Увы, товаров нет')

    def start_battle(self, player, enemy):
        battle = Battle(player, enemy)
        battle.start()

    def change_location(self):

        locs_list = list(self.where_to_go)
        if len(locs_list) == 1: # Если путь всего один
            print('Перейти в локацию {}'.format(locs_list[0].name))
            input()
            return locs_list[0]
        else: # Если путей несколько
            print('Перейти в локацию:')
            for num, i in enumerate(locs_list, start = 1):
                print(num, i.name)
            choice = int(input()) - 1
            if locs_list[choice]:
                print('Вы переходите в другую локацию')
                return locs_list[choice]

    def pick_up_item(self):
        # Подобрать предмет (пока только деньги)
        if 'money' in self.items.keys():
            self.player.add_money(self.items.get('money'))
            print('Деньги персонажа: {}'.format(self.player.money))
            self.items.pop('money')
        if self.items:
            for i in self.items:
                pass # Дописать. Решить, оставить items {} или set()

    def rent_room(self):
        # Ночевать (пока без эффектов)
        if self.player.money >= 5:
            print('Комната твоя на ночь')
            self.player.subtract_money(5)
            for i in range(10):
                print('-', end = '')
                time.sleep(0.07)
            print('\nНаступило утро')
        else:
            print('Денег маловато. Спи на улице')