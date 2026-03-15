# Imports
import weapons
import armor
import items
import time

# Player character
class Character:
    def __init__(self, name: str, max_hp: int, hp: int, inv: dict, weapon, armor, lvl: int, exp: int):
        self.name     = name
        self.max_hp   = max_hp
        self.hp       = hp
        self.weapon   = weapon
        self.inv      = inv
        self.armor = armor
        self.lvl = lvl
        self.exp = exp


    def attack(self, target):
        # Attacks enemies
        target.hp -= (self.weapon.dmg - target.armor.defense)

    def lvlup(self):
        if self.exp >= self.lvl * 100:
            self.exp = self.exp - self.lvl * 100
            self.lvl += 1
            self.max_hp = self.max_hp + (self.lvl - 1) * 2
            self.hp = self.max_hp
            print(f'you have succefuly leveled up, you are now level: {self.lvl}')
            print(f'your remaining experience: {self.exp} points')
        else:
            print(f"you don't have enough experience points to level up, current exp: {self.exp}, exp needed to level up: {self.lvl * 100}")

    def rest(self):
        print('how long to rest?')
        number = input('>')
        number = int(number)
        try:
            print(f'resting for {number * 2} hours...')
            time.sleep(number * 2)
            self.hp = self.hp + number
            if self.hp > self.max_hp:
                self.hp = self.max_hp 
        except ValueError:
            print('you must enter a number in digit form')

    def change_weapon(self):
        # Allows the player to change weapon
        player_input = input('>').lower()
        if player_input in self.inv and player_input in weapons.weapons.keys():
            add_to_inventory(self.inv, {self.weapon.id: 1})
            try:
                self.weapon = weapons.weapons[player_input]
                del self.inv[player_input]
            except KeyError:
                print("there is no such weapon in the inventory")
        else:
            print("there is no such weapon in the inventory")

    def change_armor(self):
        # Allows the player to change armor
        player_input = input('>').lower()
        if player_input in self.inv and player_input in armor.armors.keys():
            add_to_inventory(self.inv, {self.armor.id: 1})
            try:
                self.armor = armor.armors[player_input]
                del self.inv[player_input]
            except KeyError:
                print("there is no such armor in the inventory")
        else:
            print("there is no such armor in the inventory")
    
    def heal_self(self):
        player_input = input('>').lower()
        if player_input in self.inv and player_input in items.items.keys():
            print(f'used {player_input} to heal {items.items[player_input].hpheal} health points')
            try:
                if self.hp + items.items[player_input].hpheal > self.max_hp and self.inv[player_input] == 1:
                    self.hp = self.max_hp
                    del self.inv[player_input]
                elif self.hp + items.items[player_input].hpheal > self.max_hp and self.inv[player_input] > 1:
                    self.hp = self.max_hp
                    self.inv[player_input] -= 1
                else:
                    if self.inv[player_input] > 1:
                        self.hp += items.items[player_input].hpheal
                        self.inv[player_input] -= 1
                    elif self.inv[player_input] == 1:
                        self.hp += items.items[player_input].hpheal
                        del self.inv[player_input]
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
        target.hp -= (self.weapon.dmg - target.armor.defense)

    def ressurection(self):
        # Makes so that enemies have full health on encounter
            self.hp = self.max_hp
# Enemies
goblin = Enemy('Goblin', 5, 5, weapons.weapons['rusty dagger'], armor.armors['no armor'], 10,{'rusty dagger': 1, 'rag': 1})
slime = Enemy('Slime', 8, 8, weapons.weapons['acid body'], armor.armors['no armor'], 20,{'slime chunk': 1})



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