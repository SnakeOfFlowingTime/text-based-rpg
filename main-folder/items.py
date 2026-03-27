
# Items class
class Item:
    def __init__(self, name: str, id: str, description: str, type: str,value: int):
        self.name = name
        self.id = id
        self.description = description
        self.type = type
        self.value = value

# Healing items subclass
class HealItem(Item):
    def __init__(self, name: str, id: str, description: str, type: str,value: int, hpheal: int):
        super().__init__(name, id, description, type, value)
        self.hpheal = hpheal


# Items
items = {
't0 bandage': HealItem(name = 'Slime-Based Bandages', id = 't0 bandage',
description = 'bandages infused with specially treated slime, very effective in healing small wounds', 
value = 1, type = 'healing', hpheal = 3),

'rag': Item(name = 'Rag', id = 'rag', description = 'a torn and dirty of rag', type = 'miscellaneous',value = 1),

'slime chunk': Item(name = 'Slime Chunck', id = 'slime chunk',
description = 'low level ingredient widely used in alchemy, sourced from slimes', type = 'alchemy ingredient',value = 2),

'copper coin': Item(name = 'Copper coin', id = 'copper coin', description = 'coin made from copper', type = 'money', value = 1),

'silver coin': Item(name = 'Silver Coin', id = 'silver coin', description = 'coin made from silver', type = 'money', value = 100),

'gold coin': Item(name = 'Gold Coin', id = 'gold coin', description = 'coin made from gold', type = 'money', value = 10000),

'small rock': Item(name = 'Small Rock', id = 'small rock', description = 'a small of stone', type = 'miscellaneous',value = 0),

'stick': Item(name = 'Stick', id = 'stick', description = 'a normal stick', type = 'miscellaneous', value = 0),

'boar skin': Item(name = 'Wild Boar Skin', id = 'boar skin', 
description = 'the skin of a wild boar, can be further processed into many useful things', 
type = 'animal drop', value = 10),

'wolf skin': Item(name = 'Wolf Skin', id = 'wolf skin', 
description = 'the skin of a wolf, can be further processed for useful materials', type = 'animal drop', value = 10),

'strong animal bone': Item(name = 'Strong Animal Bone', id = 'strong animal bone', 
description = 'animal bone that can be use in tool making and other things, can also be used in some alchemical processes or further processed for many useful byproducts',
type = 'animal drop', value = 2),

'meat': Item(name = 'Meat', id = 'meat', 
description = 'good meat that has a lot of nutrients, each piece is 1kg',
type = 'animal drop', value = 1),

'boar tusk': Item(name = 'Wild Boar Tusk', id = 'boar tusk', 
description = 'the tusk of a wild boar, useful as a material', type = 'animal drop', value = 5),

'boar hoof': Item(name = 'Wild Boar Hoof', id = 'boar hoof', 
description = 'the hoof of a wild boar, can be used for cooking or futher processed for some useful materials',
type = 'animal drop', value = 1),

'wolf tooth': Item(name = 'Wolf Tooth', id = 'wolf tooth', 
description = 'the canine of a wolf, used for many things including alchemy', type = 'animal drop', value = 3),

'wolf claw': Item(name = 'Wolf Claw', id = 'wolf claw', 
description = 'the claw of a wolf, might have some use', type = 'animal drop', value = 1),

'magic mutated rat skin': Item(name = 'Magicaly Mutated Rat Skin', id = 'magic mutated rat skin', 
description = 'the skin of rat that underwent a magicaly induced mutation, thus growing big and strong, has some uses in alchemy but it other than that it has minimal use', 
type = 'alchemy ingredient', value = 15),

'bear skin': Item(name = 'Bear Skin', id = 'bear skin', 
description = 'the skin of a bear, can be further processed for many useful materials',
type = 'animal drop', value = 50),

'bear paw': Item(name = 'Bear Paw', id = 'bear paw', 
description = 'the paw of a bear, is said to be the most delicious part of a bear', 
type = 'animal drop', value = 10),
}