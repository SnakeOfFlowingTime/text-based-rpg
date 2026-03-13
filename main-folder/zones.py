# Zones class thingy
class Zones:
    def __init__(self, name: str, description: str, item: dict, danger: str):
        self.name        = name
        self.description = description
        self.north       = None
        self.south       = None
        self.east        = None
        self.west        = None
        self.item        = item
        self.danger      = danger

    def getItem(self, item_name):
        # Get stuff from the zone, took a while to fix
        if item_name in self.item:
            for key, value in self.item.items():
                if item_name == key:
                    item_taken = {key: value}
                    del self.item[item_name]
                    return item_taken
        else:
            print('invalid command')
            return False

# Zones
town_square = Zones('Town Square', "the center of the town, other than a small rock there's nothing to see",
                    {'small rock': 1}, 'No Danger')
town_market = Zones('Town Market', "the economic center of the town, best place to buy and sell your wares",
                    {'copper coin': 5}, 'No Danger')
town_exit = Zones('Town Gate', "a gate leading to the outside of town, it's dangerous out there",
                  {'wooden sword': 1}, 'No Danger')
forest_0_0 = Zones('Low Danger Forest',           
 """there's a lot of trees nearby,
luckly you're still near town, but be careful,
you could still be ambushed by some pesky monsters""", 
{'stick': 2, 'small rock': 1}, 'Low Danger')

# Connection between the zones
town_square.north = town_market
town_square.south = town_exit
town_exit.north = town_square
town_exit.south = forest_0_0
town_market.south = town_square
forest_0_0.north = town_exit