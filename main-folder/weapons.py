# Weapon class thingy
class Weapon:
    def __init__(self, name: str, id: str, type: str, dmg: int, value: int):
        self.name = name
        self.id = id
        self.type = type
        self.dmg = dmg
        self.value = value

# Weapons
weapons = {
'fists' : Weapon(name = 'Fists', id = 'fists', type = 'melee', dmg = 1, value = 0),

'wooden sword' : Weapon(name = 'Wooden Sword', id = 'wooden sword', type = 'blunt', dmg = 2, value = 1),

'weak bow' : Weapon(name = 'Weak Bow', id = 'weak bow', type = 'piercing', dmg = 2, value = 4),

'rusty dagger' : Weapon(name = 'Rusty Dagger', id = 'rusty dagger', type = 'slashing', dmg = 2, value = 2),

'acid body' : Weapon(name = 'Acidic Body', id = 'acid body', type = 'acid', dmg = 2, value = 1),

'iron sword': Weapon(name = 'Iron Sword', id = 'iron sword', type = 'slashing', dmg = 4, value = 30),

'boar tusk': Weapon(name = 'Boar Tusk', id = 'boar tusk', type = 'piercing', dmg = 3, value = 5),

'iron dagger': Weapon(name = 'Iron Dagger', id = 'iron dagger', type = 'slashing', dmg = 3, value = 8),

'wolf bite': Weapon(name = 'Wolf Bite', id = 'wolf bite', type = 'piercing', dmg = 3, value = 0),

'heavy iron stick': Weapon(name = 'Heavy Iron Stick', id = 'heavy iron stick', type = 'blunt', dmg = 4, value = 30)
}