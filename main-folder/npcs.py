import items, weapons, armor, json
from characters import add_to_inventory
# Merchant npcs
class Merchant:
    def __init__(self, name: str, id: str, description: str, selling: dict, location: str):
        self.name = name
        self.id = id
        self.description = description
        self.selling = selling
        self.location = location
    
    # For the player to sell stuff, should be working
    def buy(self, target):
        print('what would you like to sell?')
        print(target.inv)
        sell = input('>').lower()
        try:
            
            # Checks if it's a real item
            if sell in target.inv and sell in items.items or sell in weapons.weapons or sell in armor.armors:
                print('and how many would you like to sell?')
                number = input('>').lower()
                number = int(number)
                
                # Checks if number is positive and deducts the item from player and gives the money
                if number > 0 and sell in items.items and items.items[f'{sell}'].value != 0:
                    if number < target.inv[sell]:
                        target.inv[sell] -= number
                        target.money += items.items[sell].value * number
                        print(f"you've sold: {number} {sell}")
                    elif number == target.inv[sell]:
                        target.money += items.items[sell].value * number
                        del target.inv[sell]
                        print(f"you've sold: {number} {sell}")
                    else:
                        print(f"you don't have that much {sell} to sell")
                elif number > 0 and sell in weapons.weapons[f'{sell}'].value != 0:
                    if number < target.inv[sell]:
                        target.inv[sell] -= number
                        target.money += weapons.weapons[sell].value * number
                        print(f"you've sold: {number} {sell}")
                    elif number == target.inv[sell]:
                        target.money += weapons.weapons[sell].value * number
                        del target.inv[sell]
                        print(f"you've sold: {number} {sell}")
                    else:
                        print(f"you don't have that much {sell} to sell")
                elif number > 0 and sell in armor.armors[f'{sell}'].value != 0:
                    if number < target.inv[sell]:
                        target.inv[sell] -= number
                        target.money += armor.armors[sell].value * number
                        print(f"you've sold: {number} {sell}")
                    elif number == target.inv[sell]:
                        target.money += armor.armors[sell].value * number
                        del target.inv[sell]
                        print(f"you've sold: {number} {sell}")
                    else:
                        print(f"you don't have that much {sell} to sell")
                else:
                    print('please enter a positive non zero number or the item you are trying to sell is worthless/cannot be sold')
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

# Load game
with open('merchant save file.json') as merchant_save:
    merchant_data = json.load(merchant_save)


# Merchant npcs
merchants = {'town merchant': Merchant(name = 'Town Nerchant', id = 'town merchant',
                                       description = 'just an ordinary merchant in an ordinary town',
                                       selling = merchant_data['town market merchant stock'], location ='town market',
                                       )



}