class Person:
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
        #print(enemy.armor)


class Player(Person):

    def __init__(self, name, health, armor, damage, money = 0, items = set(), \
        slots = {'head': 0, 'body':0, 'legs': 0, 'left_arm': 0, 'right_arm': 0}):
        super().__init__(name, health, armor, damage)
        self.money = money
        self.items = items
        self.slots = slots
        self._experience = 0
        self._exp_to_next_level = 100

    def _is_next_lvl(self):
        if self._experience >= self._exp_to_next_level:
            self._lvl += 1
            self._exp_to_next_level *= 2

    def battle_won(self, experience_count):
        self._experience += experience_count
        self._is_next_lvl()

    def count_armor(self):
        armor_sum = 0
        for i in self.slots:
            if self.slots[i]:
                armor_sum += self.slots[i].armor_points
        return armor_sum

    def add_money(self, ammount):
        self.money += ammount

    def add_item(self, item):
        self.items.add(item)

    def use_item(self, item):
        if hasattr(item, 'type'):
            self.slots[item.type] = item
            self.items.remove(item)
        else:
            print('Нельзя использовать')

    def show_items(self):
        if self.items:
            print('Инвентарь:')
            j = 1
            for i in self.items:
                print('{}: {}'.format(j, i.name))
                j += 1
            print('{} монет'.format(self.money))
            choice = int(input())
            try:
                if choice != 0 and list(self.items)[choice - 1]:
                    self.use_item(list(self.items)[choice - 1])
            except IndexError:
                pass
        else:
            print('Инвентарь пуст')
            print('{} монет'.format(self.money))

    def show_slots(self):
        for i in self.slots:
            if self.slots[i]:
                print(i, self.slots[i].name, self.slots[i].armor_points)

class Enemy(Person):

    def __init__(self, name, health, armor, damage, lvl):
        super().__init__(name, health, armor, damage)
        self._experience_for_won = 50
        self._lvl = lvl

    def get_experience_for_won(self):
        return self._experience_for_won * self._lvl


class Battle:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        print('Началась драка')
        self._player.armor = 1 + self._player.count_armor()
        print(self._player.armor)
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
        else:
            print('Враг победил')

class NPC:
    def __init__(self, name, goods_type = 0, goods = set(), talk = 0):
        self.name = name
        self.goods_type = goods_type
        self.goods = goods
        self.talk = talk


class Location:
    def __init__(self, name, player, npc = 0, enemy = 0, where_to_go = 0, items = {}):
        self.name = name
        self.npc = npc
        self.enemy = enemy
        self.where_to_go = where_to_go
        self.items = items
        self.player = player

    def talk_to_npc(self):
        print('Вы приветствуете NPC {}'.format(self.npc.name))
        if self.npc.talk:
            print('{} не против поговорить(1)'.format(self.npc.name))
        if self.npc.goods_type:
            print('{} предлагает поторговать {}(2)'.format(self.npc.name, self.npc.goods_type))
        answer = input()
        if answer == '2':
            self.trade(self.npc)

    def trade(self, npc):
        if npc.goods:
            goods = list(npc.goods)
            for num, i in enumerate(goods, start = 1):
                if isinstance(i, Armor):
                    print(num, i.name, i.armor_points, i.value)
                else:
                    print(num, i.name, i.value)
            choice = int(input()) - 1
            item = goods[choice]
            if item:
                if self.player.money >= item.value:
                    print(item.name)
                    self.player.items.add(item)
                    self.npc.goods.remove(item)
                    self.player.money -= item.value
                else:
                    print('Денег маловато')

        else:
            print('Увы, товаров нет')

    def start_battle(self, player, enemy):
        battle = Battle(player, enemy)
        battle.start()

    def change_location(self):
        print('Вы переходите в другую локацию')
        return self.where_to_go
    def pick_up_item(self):
        if 'money' in self.items.keys():
            self.player.add_money(self.items.get('money'))
            print('Деньги персонажа: {}'.format(self.player.money))
            self.items.pop('money')


class Item:
    def __init__(self, name, weight, value, stackable = False):
        self.name = name
        self.weight = weight
        self.value = value
        self.stackable = stackable


class Armor(Item):
    def __init__(self, name, weight, value, type, armor_points, stackable = False):
        super().__init__(name, weight, value, stackable = False)
        self.type = type
        self.armor_points = armor_points
        self.stackable = False

def main():
    player = Player('Путник', 100, 1, 10, 499)
    bandit = Enemy('Бандит', 100, 1.2, 10, 2)
    weapon_merchant = NPC('Торговец', 'Оружие', set())
    armor_merchant = NPC('Торговец', 'Броня', set())
    '''без set() weapon_merchant получал те же товары,
    т.к. они ссылались на один и тот же набор'''

    armor_shop = Location('Лавка продавца брони', player, armor_merchant)
    street = Location('Улица', player, weapon_merchant, bandit, armor_shop, {'money': 1})
    armor_shop.where_to_go = street
    location = street

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

    print('(0: Выйти из игры)')
    while True:
        print(location.name)
        #for i in location.npc.goods:
        #    print(i.name)
        #print(location.npc.goods)
        if location.npc:
            print('1: Поговорить с NPC')
        if location.enemy:
            print('2: Напасть на врага {}'.format(location.enemy.name))
        if location.where_to_go:
            print('3: Перейти в локацию {}'.format(location.where_to_go.name))
        if location.items:
            print('4: Подобрать предмет:\n', location.items)
        print('5: Посмотреть инвентарь')
        print('6: Посмотреть слоты')
        try:
            choice = int(input())
            if choice == 1 and location.npc:
                location.talk_to_npc()
            elif choice == 2 and location.enemy:
                location.start_battle(player, bandit)
            elif choice == 3 and location.where_to_go:
                location = location.change_location()
            elif choice == 4 and location.items:
                location.pick_up_item()
            elif choice == 5:
                player.show_items()
            elif choice == 6:
                player.show_slots()
            elif choice == 0:
                print('Выход из игры')
                break
            else:
                print('Ошибка, вариант отсутствует')
        except ValueError:
            print('Ошибка, введите цифру')
        #input('продолжить')
        print('')


if __name__ == '__main__':
    main()