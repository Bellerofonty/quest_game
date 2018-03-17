##import time

from Warrior import *
from Player import *
from Enemy import *
from Battle import *
from NPC import *
from Location import *
from Item import *
from Armor import *
from Quest import *



from globals import *
import test_script

"""Основной цикл"""

print('(0: Выйти из игры)')
first = 1  # Флаг первого посещения
while True:
    print(test_script.check())
    if not first:
        time.sleep(0.3)
    else:
        first = 0

    if location.name not in player.locs_visited:
        print(location.name,'(я здесь впервые)')
    else:
        print(location.name)

    #Варианты действий
    if location.npc:
        print('1: Поговорить с NPC')
    if location.enemy:
        print('2: Напасть на врага {}'.format(location.enemy.name))
    if location.where_to_go:
        print('3: Перейти в другую локацию')
    if location.items:
        print('4: Подобрать предмет:')
        for i in location.items:
            print(i, location.items[i])
    print('5: Посмотреть инвентарь')
    print('6: Посмотреть слоты')
    if location.is_inn:
        print('7: Снять комнату за 5 монет')
    try:
        choice = int(input())
        if choice:
            print('')
        if choice == 1 and location.npc:
            location.talk_to_npc(location.npc)
        elif choice == 2 and location.enemy:
            location.start_battle(player, location.enemy)
        elif choice == 3 and location.where_to_go:
            player.locs_visited.add(location.name)
            location = location.change_location()
        elif choice == 4 and location.items:
            location.pick_up_item()
        elif choice == 5:
            player.show_items()
        elif choice == 6:
            player.show_slots()
        elif choice == 7:
            location.rent_room()
        elif choice == 0:
            print('Выход из игры')
            break
        else:
            print('Ошибка, вариант отсутствует')
    except ValueError:
        pass
    #input('продолжить')
    print('')