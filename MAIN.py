##import time
import importlib

from Warrior import *
from Player import *
from Enemy import *
from Battle import *
from NPC import *
from Location import *
from Item import *
from Armor import *
from Quest import *
import globals as gl


"""Основной цикл"""

print('(0: Выйти из игры)')
first = 1  # Флаг первого посещения
while True:
    mod_name = 'test_script'
    test_script = importlib.import_module(mod_name)
    print(test_script.check())
    if not first:
        time.sleep(0.3)
    else:
        first = 0

    if gl.location.name not in gl.player.locs_visited:
        print(gl.location.name,'(я здесь впервые)')
    else:
        print(gl.location.name)

    #Варианты действий
    if gl.location.npc:
        print('1: Поговорить с NPC')
    if gl.location.enemy:
        print('2: Напасть на врага {}'.format(gl.location.enemy.name))
    if gl.location.where_to_go:
        print('3: Перейти в другую локацию')
    if gl.location.items:
        print('4: Подобрать предмет:')
        for i in gl.location.items:
            print(i, gl.location.items[i])
    print('5: Посмотреть инвентарь')
    print('6: Посмотреть слоты')
    if gl.location.is_inn:
        print('7: Снять комнату за 5 монет')
    try:
        choice = int(input())
        if choice:
            print('')
        if choice == 1 and gl.location.npc:
            gl.location.talk_to_npc(gl.location.npc)
        elif choice == 2 and gl.location.enemy:
            gl.location.start_battle(player, gl.location.enemy)
        elif choice == 3 and gl.location.where_to_go:
            gl.player.locs_visited.add(gl.location.name)
            gl.location = gl.location.change_location()
        elif choice == 4 and gl.location.items:
            gl.location.pick_up_item()
        elif choice == 5:
            gl.player.show_items()
        elif choice == 6:
            gl.player.show_slots()
        elif choice == 7:
            gl.location.rent_room()
        elif choice == 0:
            print('Выход из игры')
            break
        else:
            print('Ошибка, вариант отсутствует')
    except ValueError:
        pass
    #input('продолжить')
    print('')