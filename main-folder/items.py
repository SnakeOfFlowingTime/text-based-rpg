
# Items class
class Item:
    def __init__(self, name: str, id: str, description: str, value: int):
        self.name = name
        self.id = id
        self.description = description
        self.value = value

# Healing items subclass
class HealItem(Item):
    def __init__(self, name: str, id: str, description: str, value: int, hpheal: int):
        super().__init__(name, id, description, value)
        self.hpheal = hpheal



items = {
't0 bandage': HealItem(name = 'Slime-Based Bandages', id = 't0 bandage',
description = 'bandages infused with specially treated slime, very effective in healing small wounds', 
value = 1, hpheal = 3),
'rag': Item(name = 'Rag', id = 'rag', description = 'a torn and dirty piece of rag', value = 1),
'slime chunk': Item(name = 'Slime Chunck', id = 'slime chunk', description = 'low level ingredient widely used in alchemy, sourced from slimes', value = 2),
'copper coin': Item(name = 'Copper coin', id = 'copper coin', description = 'coin made from copper', value = 1),
'small rock': Item(name = 'Small Rock', id = 'small rock', description = 'a small piece of stone', value = 0),
'stick': Item(name = 'Stick', id = 'stick', description = 'a normal stick', value = 0)

}