# Imports
import weapons, armor, items, time

# Player character
class Character:
    def __init__(self, name: str, max_hp: int, hp: int, inv: dict, weapon, armor, lvl: int, exp: int, money: int, quests_completed: list):
        self.name     = name
        self.max_hp   = max_hp
        self.hp       = hp
        self.weapon   = weapon
        self.inv      = inv
        self.armor = armor
        self.lvl = lvl
        self.exp = exp
        self.money = money
        self.quests_completed = quests_completed


    def attack(self, target):
        # Attacks enemies
        if target.armor.defense <= self.weapon.dmg:
            target.hp -= (self.weapon.dmg - target.armor.defense)
        elif target.armor.defense > self.weapon.dmg:
            target.hp -= 0

    def lvlup(self):
        # Level up
        if self.exp >= self.lvl * 100:
            self.exp = self.exp - self.lvl * 100
            self.lvl += 1
            self.max_hp = self.max_hp + (self.lvl - 1) * 2
            self.hp = self.max_hp
            print(f'you have leveled up, you are now level: {self.lvl}')
            print(f'your remaining experience: {self.exp} points')
        else:
            print(f"you don't have enough experience points to level up, current exp: {self.exp}, exp needed to level up: {self.lvl * 100}")

    def rest(self, number):
        # Rest, heals for number after number * 2 of seconds
        try:
            if number >= 0:
                print(f'resting for {number * 2} hours...')
                time.sleep(number * 2)
                print('you have rested')
                self.hp = self.hp + number
                if self.hp > self.max_hp:
                    self.hp = self.max_hp 
            else:
                print('must be a positive number')
        except ValueError:
            print('you must enter a number in digit form')

    def change_weapon(self, weapon_equip):
        # Allows the player to change weapon
        if weapon_equip in self.inv and weapon_equip in weapons.weapons.keys():
            if self.lvl >= weapons.weapons[weapon_equip].lvlreq:
                pass
            else:
                print("you don't meet the minimun requirements to use this weapon")
                return
            add_to_inventory(self.inv, {self.weapon.id: 1})
            try:
                self.weapon = weapons.weapons[weapon_equip]
                if self.inv[weapon_equip] > 1:
                    self.inv[weapon_equip] -= 1
                else:
                    del self.inv[weapon_equip]
            except KeyError:
                print("there is no such weapon in the inventory")
        else:
            print("there is no such weapon in the inventory")

    def change_armor(self, armor_equip):
        # Allows the player to change armor
        if armor_equip in self.inv and armor_equip in armor.armors.keys():
            if self.lvl >= armor.armors[armor_equip].lvlreq:
                pass
            else:
                print("you don't meet the minimun requirements to use this armor")
                return
            add_to_inventory(self.inv, {self.armor.id: 1})
            try:
                self.armor = armor.armors[armor_equip]
                if self.inv[armor_equip] > 1:
                    self.inv[armor_equip] -= 1
                else:
                    del self.inv[armor_equip]
            except KeyError:
                print("there is no such armor in the inventory")
        else:
            print("there is no such armor in the inventory")
    
    def heal_self(self, heal_item):
        # Allows the player to consume a healing item to recover hp
        if heal_item in self.inv and heal_item in items.items.keys() and items.items[heal_item].type == 'healing':
            print(f'used {heal_item} to heal {items.items[heal_item].hpheal} health points')
            try:
                if self.hp + items.items[heal_item].hpheal > self.max_hp and self.inv[heal_item] == 1:
                    self.hp = self.max_hp
                    del self.inv[heal_item]
                elif self.hp + items.items[heal_item].hpheal > self.max_hp and self.inv[heal_item] > 1:
                    self.hp = self.max_hp
                    self.inv[heal_item] -= 1
                else:
                    if self.inv[heal_item] > 1:
                        self.hp += items.items[heal_item].hpheal
                        self.inv[heal_item] -= 1
                    elif self.inv[heal_item] == 1:
                        self.hp += items.items[heal_item].hpheal
                        del self.inv[heal_item]
            except KeyError:
                print("there is no such healing item in the inventory")
        else:
            print("there is no such healing item in the inventory")



# Enemies character
class Enemy:
    def __init__(self, name: str, max_hp: int, hp: int, weapon, armor, expvalue: int, loot: dict):
        self.name   = name
        self.max_hp = max_hp
        self.hp     = hp
        self.weapon = weapon
        self.loot = loot
        self.armor = armor
        self.expvalue = expvalue

    def attack(self, target):
        # Attacks player
        if target.armor.defense <= self.weapon.dmg:
            target.hp -= (self.weapon.dmg - target.armor.defense)
        elif target.armor.defense > self.weapon.dmg:
            target.hp -= 0

    def ressurection(self):
        # Makes so that enemies have full health on encounter
            self.hp = self.max_hp

# To display the inventory and to add stuff to it, it's a mess but it works
def display_inventory(inventory):
    print('inventory: ')
    for k, v in inventory.items():
        print(str(k) + ': ' + str(v))

# Add stuff to the inventory
def add_to_inventory(inventory, item):
    for key, value in item.items():    
        if key in inventory:
            inventory[key] = inventory[key] + value
            print(str(key) + ' added to inventory')
        else:
            inventory.setdefault(key, value)
            print(str(key) + ' added to inventory')

# Enemies
enemies = {
'goblin': Enemy(name = 'Goblin', max_hp = 5, hp = 5, weapon = weapons.weapons['rusty dagger'],
                armor = armor.armors['no armor'], expvalue = 10, loot = {'rusty dagger': 1, 'rag': 1}),
'slime': Enemy(name = 'Slime', max_hp = 8, hp = 8, weapon = weapons.weapons['acid body'],
               armor = armor.armors['no armor'], expvalue = 20, loot = {'slime chunk': 1}),                
'wild boar': Enemy(name = 'Wild Boar', max_hp = 20, hp = 20, weapon = weapons.weapons['boar tusks'],
                   armor = armor.armors['hardened mud layer'], expvalue = 50, 
                   loot = {'boar tusk': 4, 'boar skin': 1, 'strong animal bone': 10, 'meat': 15, 'boar hoof': 4}),
'wolf': Enemy(name = 'Wolf', max_hp = 15, hp = 15, weapon = weapons.weapons['wolf bite'], armor = armor.armors['no armor'], expvalue = 40,
            loot = {'wolf skin': 1, 'wolf tooth': 4, 'strong animal bone': 20, 'meat': 15, 'wolf claw': 18}),
'big rat': Enemy(name = 'Magic Mutated Rat', max_hp= 4, hp = 4, weapon = weapons.weapons['rat bite'],
                armor = armor.armors['no armor'], expvalue = 5, 
                loot = {'magic mutated rat skin': 1, 'meat': 3}),
'bear': Enemy(name = 'Bear', max_hp = 25, hp = 25, weapon = weapons.weapons['bear punch'], armor = armor.armors['no armor'],
            expvalue = 150, loot = {'bear skin': 1, 'strong animal bone': 50, 'meat': 50, 'bear paw': 4}),
'goblin warrior': Enemy(name = 'Goblin Warrior', max_hp = 35, hp = 35, weapon = weapons.weapons['iron sword'],
                        armor = armor.armors['leather armor'], expvalue = 100, loot = {'iron sword': 1, 'leather armor': 1})
                }

