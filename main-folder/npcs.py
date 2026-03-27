import items, weapons, armor, json, os, sys, quests
from characters import add_to_inventory

class QuestNpc:
    def __init__(self, name: str, id: str, description: str, quest: list, location: str):
        self.name = name
        self.id = id
        self.description = description
        self.quest = quest
        self.location = location
        
# Merchant npcs
class Merchant:
    def __init__(self, name: str, id: str, description: str, selling: dict, location: str):
        self.name = name
        self.id = id
        self.description = description
        self.selling = selling
        self.location = location
    
    # For the player to sell stuff, should be working
    def buy(self, target, item, number):
        try:
            
            # Checks if it's a real item
            if item in target.inv and item in items.items or item in weapons.weapons or item in armor.armors:
                if item in items.items.keys():
                    if items.items[f'{item}'].value == 0:
                        print(f'this item ({item}) is worthless/cannot be sold')
                        return
                if item in weapons.weapons.keys():
                    if weapons.weapons[f'{item}'].value == 0:
                        print(f'this item ({item}) is worthless/cannot be sold')
                        return
                if item in armor.armors.keys():
                    if armor.armors[f'{item}'].value == 0:
                        print(f'this item ({item}) is worthless/cannot be sold')
                        return
                
                # Checks if number is positive and deducts the item from player and gives the money
                if number != None and number > 0 and item in items.items and items.items[f'{item}'].value != 0:
                    if number < target.inv[item]:
                        target.inv[item] -= number
                        target.money += items.items[item].value * number
                        print(f"you've sold: {number} {item}")
                    elif number == target.inv[item]:
                        target.money += items.items[item].value * number
                        del target.inv[item]
                        print(f"you've sold: {number} {item}")
                    else:
                        print(f"you don't have that much {item} to sell")
                elif number != None and number > 0 and item in weapons.weapons and weapons.weapons[f'{item}'].value != 0:
                    if number < target.inv[item]:
                        target.inv[item] -= number
                        target.money += weapons.weapons[item].value * number
                        print(f"you've sold: {number} {item}")
                    elif number == target.inv[item]:
                        target.money += weapons.weapons[item].value * number
                        del target.inv[item]
                        print(f"you've sold: {number} {item}")
                    else:
                        print(f"you don't have that much {item} to sell")
                elif number != None and number > 0 and item in armor.armors and armor.armors[f'{item}'].value != 0:
                    if number < target.inv[item]:
                        target.inv[item] -= number
                        target.money += armor.armors[item].value * number
                        print(f"you've sold: {number} {item}")
                    elif number == target.inv[item]:
                        target.money += armor.armors[item].value * number
                        del target.inv[item]
                        print(f"you've sold: {number} {item}")
                    else:
                        print(f"you don't have that much {item} to sell")
                else:
                    print('please enter a positive non zero number or the item you are trying to sell is worthless/cannot be sold')
            else:
                print(f"you don't have {item}")
        except ValueError:
            print('please enter a number in digit form')

    # For the player to buy stuff, think it works now
    def sell(self, target):
        print('what would you like to buy?')
        print(f"{self.selling}")
        buying = input('>').lower()
        try:
            if buying in self.selling:
                print('and how many would you like to buy?')
                number = input('>')
                number = int(number)
                if number <= self.selling[buying]:
                    if number <= 0:
                        print('please enter positive non zero number')
                        return
                    
                    # Determines if the item to be bought is a real item and checks if player has enough money
                    if buying in items.items and target.money >= items.items[buying].value * number:
                        print(f'that will be {items.items[buying].value * number}')
                    elif buying in weapons.weapons and target.money >= weapons.weapons[buying].value * number:
                        print(f'that will be {weapons.weapons[buying].value * number}')
                    elif buying in armor.armors and target.money >= armor.armors[buying].value * number:
                        print(f'that will be {armor.armors[buying].value * number}')
                    else:
                        print(f"you don't have enough money to buy {number} {buying}")
                        return
                    print(f'are you sure you want to buy {number} {buying}?')
                    y_n = input('>').lower()
                    if y_n in ['yes', 'y']:
                        
                        # Based on some stuff, decides whether to reduce stock or remove from stock
                        # Also deducts the money and gives item to player
                        if buying in items.items:
                            if number < self.selling[buying]:
                                target.money -= items.items[buying].value * number
                                purchase = {buying: number}
                                add_to_inventory(target.inv, purchase)
                                print('congratulations on your purchase')
                                self.selling[buying] -= number
                            elif number > self.selling[buying]:
                                print(f"i don't have that many {buying} to sell")
                                return
                            elif number == self.selling[buying]:
                                del self.selling[buying]
                                target.money -= items.items[buying].value * number
                                purchase = {buying: number}
                                add_to_inventory(target.inv, purchase)
                                print('congratulations on your purchase')
                        elif buying in weapons.weapons:
                            if number < self.selling[buying]:
                                target.money -= weapons.weapons[buying].value * number
                                purchase = {buying: number}
                                add_to_inventory(target.inv, purchase)
                                print('congratulations on your purchase')
                                self.selling[buying] -= number
                            elif number > self.selling[buying]:
                                print(f"i don't have that many {buying} to sell")
                                return
                            elif number == self.selling[buying]:
                                del self.selling[buying]
                                target.money -= weapons.weapons[buying].value * number
                                purchase = {buying: number}
                                add_to_inventory(target.inv, purchase)
                                print('congratulations on your purchase')
                        elif buying in armor.armors:
                            if number < self.selling[buying]:
                                target.money -= armor.armors[buying].value * number
                                purchase = {buying: number}
                                add_to_inventory(target.inv, purchase)
                                print('congratulations on your purchase')
                                self.selling[buying] -= number
                            elif number > self.selling[buying]:
                                print(f"i don't have that many {buying} to sell")
                                return
                            elif number == self.selling[buying]:
                                del self.selling[buying]
                                target.money -= armor.armors[buying].value * number
                                purchase = {buying: number}
                                add_to_inventory(target.inv, purchase)
                                print('congratulations on your purchase')
                        else:
                            print('something somehow went wrong')
                    elif y_n in ['no', 'n']:
                        return
                    else:
                        print('must be an yes or no answer')
                else:
                    print(f"i don't have {number} {buying}")
            else:
                print(f"i don't sell {buying}")
        except ValueError:
            print('must be a number in digit form')

def file_path(relative_path):
    # For the .exe to find the .json file needed to work
    try:
        base_path = sys._MEIPASS
    except Exception: 
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load game
merchant_file = file_path('merchant save file.json')
with open(merchant_file) as merchant_save:
    merchant_data = json.load(merchant_save)


# Quest npcs
quest_npcs = {'quest board': QuestNpc(name = 'Quest Board', id = 'quest board', 
description = "the quest board of the adventure's guild", quest = ['gather slime chunks', 'clear rat infestation'],
location = 'adventurer guild')}

# Merchant npcs
merchants = {'town merchant': Merchant(name = 'Town Merchant', id = 'town merchant',
description = 'just an ordinary merchant in an ordinary town',
selling = merchant_data['town market merchant stock'], location = 'town market'),

'alchemy items vendor': Merchant(name = 'Alchemy Items Vendor', id = 'alchemy items vendor', 
description = 'a vendor consigned by some alchemists to sell some of their products', 
selling = merchant_data['alchemy items vendor stock'], location = 'alchemy guild')



}