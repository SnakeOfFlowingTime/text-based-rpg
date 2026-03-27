import json, os, sys
# Zones class thingy
class Zones:
    def __init__(self, name: str, id: str, description: str, item: dict, danger: str, npc: list):
        self.name        = name
        self.id          = id
        self.description = description
        self.north       = None
        self.south       = None
        self.east        = None
        self.west        = None
        self.item        = item
        self.danger      = danger
        self.npc         = npc

    def getItem(self, item_name):
        # Get stuff from the zone
        item_name = ' '.join(item_name)
        if item_name in self.item:
            for key, value in self.item.items():
                if item_name == key:
                    item_taken = {key: value}
                    del self.item[item_name]
                    return item_taken
        else:
            print('invalid command')
            return False

def file_path(relative_path):
    # For the .exe to find the .json file needed to work
    try:
        base_path = sys._MEIPASS
    except Exception: 
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load game
zones_file = file_path('zones save file.json')
with open(zones_file) as zones_save:
    zones_data = json.load(zones_save)


# Zones
zones = {
'town square': Zones(name = 'Town Square', id = 'town square', description = "the center of the town, other than a small rock there's nothing to see",
                    item = zones_data['town square items'], danger = 'No Danger', npc = None),
'town market': Zones(name = 'Town Market', id = 'town market', description = "the economic center of the town, best place to buy and sell your wares",
                    item = zones_data['town market items'], danger = 'No Danger', npc = ['town merchant']),
'town exit': Zones(name = 'Town Gate', id = 'town exit', description = "a gate leading to the outside of town, it's dangerous out there",
                  item = zones_data['town exit items'], danger = 'No Danger', npc = None),

'adventurer guild': Zones(name = "The Adventurer's Guild", id = 'adventurer guild',
description = 'place where adventurers accept task posted by clients in exchange for a reward',
item = zones_data['adventurer guild items'], danger = 'No Danger', npc = ['quest board']),

'very low danger forest': Zones(name = 'Very Low Danger Forest', id ='very low danger forest',
 description = """there's a lot of trees nearby,
luckly you're still near town, but be careful,
you could still be ambushed by some pesky monsters""", 
item = zones_data['very low danger forest items'], danger = 'Very Low Danger', npc = None),

'low danger forest': Zones(name = 'Low Danger Forest', id = 'low danger forest', 
description = '''this place is further from town, be careful,
the guard team cleans this place with less frequency''', item = zones_data['low danger forest items'],
danger = 'Low Danger', npc = None),

'town farm': Zones(name = 'Town Farms', id = 'town farm', 
description = 'the farms east of town, the source of most food in town',
item = zones_data['town farm items'], danger = 'Rat Infestation', npc = None),

'alchemy guild': Zones(name = "Alchemist's Guild", id = 'alchemy guild', 
description = 
"""unlike the adventurer's guild, this place is as luxurious as it gets,
being responsible for ranking, protecting the rights of,
and representing the highest profession of the continent: alchemists""",
item = zones_data['alchemy guild items'], danger = 'No danger', npc = ['alchemy items vendor']),

'medium danger forest': Zones(name = 'Medium Danger Forest', id = 'medium danger forest', 
description = 
'''this place is quite far from town,
the only thing keeping the monster population in control
is the annual monster slaying event organized by the adventurer's guild ''',
item = zones_data['medium danger forest items'], danger = 'Medium Danger', npc = None),

}

# Connection between the zones, hope there's a better way to do this, it's getting big
zones['town square'].north = zones['town market']
zones['town square'].south = zones['town exit']
zones['town square'].west = zones['adventurer guild']
zones['town square'].east = zones['town farm']
zones['town farm'].west = zones['town square']
zones['adventurer guild'].east = zones['town square']
zones['adventurer guild'].north = zones['alchemy guild']
zones['alchemy guild'].south = zones['adventurer guild']
zones['town exit'].north = zones['town square']
zones['town exit'].south = zones['very low danger forest']
zones['town market'].south = zones['town square']
zones['very low danger forest'].north = zones['town exit']
zones['very low danger forest'].south = zones['low danger forest']
zones['low danger forest'].north = zones['very low danger forest']
zones['low danger forest'].south = zones['medium danger forest']
zones['medium danger forest'].north = zones['low danger forest']