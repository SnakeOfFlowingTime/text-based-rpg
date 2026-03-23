
# Armor class
class Armor:
    def __init__(self, name: str, id: str, type: str, defense: int, value: int):
        self.name = name
        self.id = id
        self.type = type
        self.defense = defense
        self.value = value

# Armors
armors = {
'no armor': Armor(name = 'No Armor', id = 'no armor', type = 'unarmored', defense = 0, value = 0),

'linen clothing': Armor(name = 'Linen Clothes', id = 'linen clothing', type = 'cloth', defense = 0, value = 2),

'weak wood armor': Armor(name = 'Weak Wood Armor', id = 'weak wood armor', type = 'wood', defense = 1, value = 10),

'iron plate armor': Armor(name = 'Iron Plate Armor', id = 'iron plate armor', type = 'plate', defense = 5, value = 1000),

'hardened mud layer': Armor(name = 'Hardened Mud Layer', id = 'hardened mud layer', type = 'earth', defense = 1, value= 0),

'wood armor': Armor(name = 'Wood Armor', id =  'wood armor', type = 'wood', defense = 2, value = 80),

'leather armor': Armor(name = 'Leather Armor', id = 'leather armor', type = 'leather', defense = 3, value = 300),

'iron chainmail armor': Armor(name = 'Iron Chainmail Armor', id = 'iron chainmail armor', type  = 'chainmail', defense = 4, value = 500),

'adventurer armor': Armor(name = 'Adventurer Armor', id = 'adventurer armor', type = 'composite', defense = 4, value = 400),
}