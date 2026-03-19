# Imports
import weapons, armor, items, time

# Player character
class Character:
    def __init__(self, name: str, max_hp: int, hp: int, inv: dict, weapon, armor, lvl: int, exp: int, money: int):
        self.name     = name
        self.max_hp   = max_hp
        self.hp       = hp
        self.weapon   = weapon
        self.inv      = inv
        self.armor = armor
        self.lvl = lvl
        self.exp = exp
        self.money = money


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
            print(f'you have succefuly leveled up, you are now level: {self.lvl}')
            print(f'your remaining experience: {self.exp} points')
        else:
            print(f"you don't have enough experience points to level up, current exp: {self.exp}, exp needed to level up: {self.lvl * 100}")

    def rest(self):
        # Rest, heals for number after number * 2 of seconds
        print('how long to rest?')
        number = input('>')
        number = int(number)
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

    def change_weapon(self):
        # Allows the player to change weapon
        player_input = input('>').lower()
        if player_input in self.inv and player_input in weapons.weapons.keys():
            add_to_inventory(self.inv, {self.weapon.id: 1})
            try:
                self.weapon = weapons.weapons[player_input]
                if self.inv[player_input] > 1:
                    self.inv[player_input] -= 1
                else:
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
                if self.inv[player_input] > 1:
                    self.inv[player_input] -= 1
                else:
                    del self.inv[player_input]
            except KeyError:
                print("there is no such armor in the inventory")
        else:
            print("there is no such armor in the inventory")
    
    def heal_self(self):
        # Allows the player to consume a healing item to recover hp
        player_input = input('>').lower()
        if player_input in self.inv and player_input in items.items.keys() and items.items[player_input].type == 'healing':
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
'wild boar': Enemy(name = 'Wild Boar', max_hp = 20, hp = 20, weapon = weapons.weapons['boar tusk'],
                   armor = armor.armors['hardened mud layer'], expvalue = 80, 
                   loot = {'boar tusk': 2, 'boar skin': 1, 'strong animal bone': 10, 'meat piece': 15, 'boar hoof': 4}),
'wolf': Enemy(name = 'Wolf', max_hp = 15, hp = 15, weapon = weapons.weapons['wolf bite'], armor = armor.armors['no armor'], expvalue = 50,
            loot = {'wolf skin': 1, 'wolf tooth': 4, 'strong animal bone': 20, 'meat piece': 15, 'wolf claw': 18}),
                
                }

