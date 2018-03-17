#-------------------------------------------------------------------------------
# Name:        globals
# Purpose:     глобальные переменные для MAIN, квестов и скриптов
#
# Author:      Daniil
#
# Created:     17.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Warrior import *
from Player import *
from Enemy import *
from Battle import *
from NPC import *
from Location import *
from Item import *
from Armor import *
from Quest import *

# Инициация персонажей
player = Player('Путник', 100, 1, 10, 499)
bandit = Enemy('Бандит', 100, 1.2, 10, 2)
weapon_merchant = NPC('Торговец оружием', 'Оружие')
armor_merchant = NPC('Торговец бронёй', 'Броня', talk = 1)
boozy_hacksmith = NPC('Пьяный кузнец')

# Инициация локаций
armor_shop = Location('Лавка продавца брони', player, armor_merchant)
street = Location('Улица', player, weapon_merchant, bandit, {armor_shop}, {'money': 1})
armor_shop.where_to_go = {street}
tavern = Location('Таверна', player, boozy_hacksmith, where_to_go = {street}, is_inn = 1)
forge = Location('Кузница', player, where_to_go = {street})
street.where_to_go.add(tavern)
street.where_to_go.add(forge)

location = street

# Инициация предметов
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

# Инициализация квестов
quest_list = []
quest1 = Quest('Найти Таверну', 'Должна же здесь где-то быть таверна',
     0, 'go_to_tavern')
quest_list.append(quest1)
