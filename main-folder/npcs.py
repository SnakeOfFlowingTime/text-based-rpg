import items, weapons, armor
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
            if sell in target.inv and sell in items.items or sell in weapons.weapons or sell in armor.armors:
                print('and how many would you like to sell?')
                number = input('>').lower()
                number = int(number)
                if number >= 0 and sell in items.items:
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
                elif number >= 0 and sell in weapons.weapons:
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
                elif number >= 0 and sell in armor.armors:
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
                    print('please enter a positive number or the item you are trying to sell is worthless/cannot be sold')
        except ValueError:
            print('please enter a number in digit form')

    # For the player to buy stuff, untested
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
                    if buying in items.items:
                        print(f'that will be {items.items[buying].value * number}')
                    elif buying in weapons.weapons:
                        print(f'that will be {weapons.weapons[buying].value * number}')
                    elif buying in armor.armors:
                        print(f'that will be {armor.armors[buying].value * number}')
                    print(f'are you sure you want to buy {number} {buying}?')
                    y_n = input('>').lower()
                    if y_n in ['yes', 'y']:
                        if buying in items.items:
                            target.money -= items.items[buying].value * number
                            purchase = {buying: number}
                            add_to_inventory(target.inv, purchase)
                            ('congratulations on your purchase')
                        elif buying in weapons.weapons:
                            target.money -= weapons.weapons[buying].value * number
                            purchase = {buying: number}
                            add_to_inventory(target.inv, purchase)
                            ('congratulations on your purchase')
                        elif buying in armor.armors:
                            target.money -= armor.armors[buying].value * number
                            purchase = {buying: number}
                            add_to_inventory(target.inv, purchase)
                            ('congratulations on your purchase')
                        else:
                            print('something somehow went wrong')
                    elif y_n in ['no', 'n']:
                        return
                    else:
                        print('must be an yes or no answer')
                else:
                    print(f"i don't have that many {buying}")
            else:
                print(f"i don't sell {buying}")
        except ValueError:
            print('must be a number in digit form')


# Merchant npcs
merchants = {'town merchant': Merchant(name = 'Town Nerchant', id = 'town merchant',
                                       description = 'just an ordinary merchant in an ordinary town',
                                       selling = {'weak bow': 3}, location ='town market',
                                       )



}