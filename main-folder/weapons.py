# Weapon class thingy
class Weapon:
    def __init__(self, name: str, id: str, type: str, dmg: int, value: int, lvlreq: int):
        self.name = name
        self.id = id
        self.type = type
        self.dmg = dmg
        self.value = value
        self.lvlreq = lvlreq

# Weapons
weapons = {
'fists' : Weapon(name = 'Fists', id = 'fists', type = 'melee', dmg = 1, value = 0, lvlreq = 0),

'wooden sword' : Weapon(name = 'Wooden Sword', id = 'wooden sword', type = 'blunt', dmg = 2, value = 1, lvlreq = 0),

'weak bow' : Weapon(name = 'Weak Bow', id = 'weak bow', type = 'piercing', dmg = 2, value = 4, lvlreq = 1),

'rusty dagger' : Weapon(name = 'Rusty Dagger', id = 'rusty dagger', type = 'slashing', dmg = 2, value = 2, lvlreq = 0),

'acid body' : Weapon(name = 'Acidic Body', id = 'acid body', type = 'acid', dmg = 2, value = 1, lvlreq = 0),

'iron sword': Weapon(name = 'Iron Sword', id = 'iron sword', type = 'slashing', dmg = 4, value = 30, lvlreq = 3),

'boar tusks': Weapon(name = 'Boar Tusks', id = 'boar tusks', type = 'piercing', dmg = 3, value = 0, lvlreq = 0),

'iron dagger': Weapon(name = 'Iron Dagger', id = 'iron dagger', type = 'slashing', dmg = 3, value = 8, lvlreq = 3),

'wolf bite': Weapon(name = 'Wolf Bite', id = 'wolf bite', type = 'piercing', dmg = 3, value = 0, lvlreq = 0),

'heavy iron stick': Weapon(name = 'Heavy Iron Stick', id = 'heavy iron stick', type = 'blunt', dmg = 4, value = 30, lvlreq = 3),

'iron scythe': Weapon(name = 'Iron Scythe', id = 'iron scythe', type = 'slashing', dmg = 3, value = 20, lvlreq = 3),

'rat bite': Weapon(name = 'Rat Bite', id = 'rat bite', type = 'piercing', dmg = 1, value = 0, lvlreq = 0),

'refined iron sword': Weapon(name = 'Refined Iron Sword', id = 'refined iron sword', type = 'slashing', dmg = 8, value = 600, lvlreq = 5),

'bear punch': Weapon(name = 'Bear Punch', id = 'bear punch', type = 'blunt', dmg = 4, value = 0, lvlreq = 0),

'iron spear': Weapon(name = 'Iron Spear', id = 'iron spear', type = 'piercing', dmg = 4, value = 25, lvlreq = 3),
}