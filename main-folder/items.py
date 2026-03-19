
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
value = 1, type = 'healing',hpheal = 3),

'rag': Item(name = 'Rag', id = 'rag', description = 'a torn and dirty piece of rag', type = 'miscellaneous',value = 1),

'slime chunk': Item(name = 'Slime Chunck', id = 'slime chunk',
                    description = 'low level ingredient widely used in alchemy, sourced from slimes', type = 'alchemy ingredient',value = 2),

'copper coin': Item(name = 'Copper coin', id = 'copper coin', description = 'coin made from copper', type = 'money', value = 1),

'small rock': Item(name = 'Small Rock', id = 'small rock', description = 'a small piece of stone', type = 'miscellaneous',value = 0),

'stick': Item(name = 'Stick', id = 'stick', description = 'a normal stick', type = 'miscellaneous', value = 0),

'boar skin': Item(name = 'Wild Boar Skin', id = 'boar skin', 
description = 'the skin of a wild boar, can be further processed into many usefull things', 
type = 'animal drop', value = 10),

'wolf skin': Item(name = 'Wolf Skin', id = 'wolf skin', 
description = 'the skin of a wolf, can be further processed for usefull materials', type = 'animal drop', value = 10),

'strong animal bone': Item(name = 'Strong Animal Bone', id = 'strong animal bone', 
description = 'animal bone that can be use in tool making and other things, can also be used in some alchemical processes or further processed for many usefull byproducts',
type = 'animal drop', value = 2),

'meat piece': Item(name = 'Meat Piece', id = 'meat piece', 
description = 'good meat that has a lot of nutrients, each piece is 1kg',
type = 'animal drop', value = 1),

'boar hoof': Item(name = 'Wild Boar Hoof', id = 'boar hoof', 
description = 'the hoof of a wild boar, can be used for cooking or futher processed for some usefull materials',
type = 'animal drop', value = 1),

'wolf tooth': Item(name = 'Wolf Tooth', id = 'wolf tooth', 
description = 'the canine of a wolf, used for many things including alchemy', type = 'animal drop', value = 3),

'wolf claw': Item(name = 'Wolf Claw', id = 'wolf claw', 
description = 'the claw of a wolf, might have some use', type = 'animal drop', value = 1),

}