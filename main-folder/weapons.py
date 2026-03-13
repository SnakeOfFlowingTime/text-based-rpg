# Weapon class thingy
class Weapon:
    def __init__(self, name: str, type: str, dmg: int, value: int):
        self.name = name
        self.type = type
        self.dmg = dmg
        self.value = value

# Weapons
weapons = {
'fists' : Weapon(name  = 'fists',
               type  = 'unarmed',
               dmg   = 1,
               value = 0),

'wooden sword' : Weapon(name  = 'wooden sword',
                      type  = 'blunt',
                      dmg   = 2,
                      value = 1),

'weak bow' : Weapon(name  = 'weak bow',
                  type  = 'bow',
                  dmg   = 3,
                  value = 3),

'rusty dagger' : Weapon(name  = 'rusty dagger',
                      type  = 'short blade',
                      dmg   = 2,
                      value = 2),
'acid body' : Weapon(name  = 'acidic body',
                   type  = 'acid',
                   dmg   = 2,
                   value = 1)}