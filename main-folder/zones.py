import json
# Zones class thingy
class Zones:
    def __init__(self, id: str, name: str, description: str, item: dict, danger: str):
        self.id          = id
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
# To load the items in the zone from save file, works like a charm rn, idk how or why, but it works
with open('zones save file.json') as zones_save:
        zones_data = json.load(zones_save)

# Zones
zones = {
'town square': Zones('town square', 'Town Square', "the center of the town, other than a small rock there's nothing to see",
                    zones_data['town square items'], 'No Danger'),
'town market': Zones('town market', 'Town Market',"the economic center of the town, best place to buy and sell your wares",
                    zones_data['town market items'], 'No Danger'),
'town exit': Zones('town exit', 'Town Gate',"a gate leading to the outside of town, it's dangerous out there",
                  zones_data['town exit items'], 'No Danger'),
'forest 0 0': Zones('forest 0 0', 'Low Danger Forest',
 """there's a lot of trees nearby,
luckly you're still near town, but be careful,
you could still be ambushed by some pesky monsters""", 
zones_data['forest 0 0 items'], 'Low Danger'),
}

# Connection between the zones
zones['town square'].north = zones['town market']
zones['town square'].south = zones['town exit']
zones['town exit'].north = zones['town square']
zones['town exit'].south = zones['forest 0 0']
zones['town market'].south = zones['town square']
zones['forest 0 0'].north = zones['town exit']