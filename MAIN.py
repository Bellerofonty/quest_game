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


def main():
    #Инициация персонажей
    player = Player('Путник', 100, 1, 10, 499)
    bandit = Enemy('Бандит', 100, 1.2, 10, 2)
    weapon_merchant = NPC('Торговец оружием', 'Оружие')
    armor_merchant = NPC('Торговец бронёй', 'Броня', talk = 1)
    boozy_hacksmith = NPC('Пьяный кузнец')

    #Инициация локаций
    armor_shop = Location('Лавка продавца брони', player, armor_merchant)
    street = Location('Улица', player, weapon_merchant, bandit, {armor_shop}, {'money': 1})
    armor_shop.where_to_go = {street}
    tavern = Location('Таверна', player, boozy_hacksmith, where_to_go = {street}, is_inn = 1)
    forge = Location('Кузница', player, where_to_go = {street})
    street.where_to_go.add(tavern)
    street.where_to_go.add(forge)

    #Инициация предметов
    small_helmet = Armor('Маленький шлем', 1, 500, 'head', 0.5)
    mail_shirt = Armor('Кольчуга', 7, 2000, 'body', 2)
    armor_merchant.goods = {small_helmet, mail_shirt}
##    armor_merchant.goods.add(small_helmet)
##    armor_merchant.goods.add(mail_shirt)
    jacket = Armor('Куртка', 1, 100, 'body', 0.3)
    pants = Armor('Штаны', 0.5, 50, 'legs', 0)
    old_medallion = Item('Старый медальон', 0.1, 300)
##    player.add_item(small_helmet)
    player.add_item(old_medallion)
    player.slots['body'] = jacket
    player.slots['legs'] = pants


    """Основной цикл"""
    location = street
    print('(0: Выйти из игры)')
    first = 1  # Флаг первого посещения
    while True:
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


if __name__ == '__main__':
    main()