import characters
# Quests class
class Quests:
    def __init__(self, name: str, id: str, description: str, requirements: dict, reward: dict, type: str, stage: str):
        self.name = name
        self.id = id
        self.description = description
        self.requirements = requirements
        self.reward = reward
        self.type = type

    def complete_quest(self, target):
        keys = []
        number = 0
        for k, v in self.requirements.items():
            keys.append(k)
        for i in range(len(keys)):
            if keys[i] in target.inv and target.inv[keys[i]] >= self.requirements[keys[i]]:
                number += 1
        if number == len(self.requirements.keys()):
            characters.add_to_inventory(target.inv, self.reward)
            for k, v in self.requirements.items():
                if k in target.inv and target.inv[k] > self.requirements[k]:
                    target.inv[k] -= self.requirements[k]
                elif k in target.inv and target.inv[k] == self.requirements[k]:
                    del target.inv[k]
                else:
                    print("you don't meet the requirements to hand in this quest")
            if self.type != 'unlimited':
                return 'completed'
        else:
            print("you don't meet the requirements to hand in this quest")

            

quests = {'gather slime chunks': Quests(name = 'Gather Slime Chunks', id = 'gather slime chunks', 
description = "slime chunks are widely used in alchemy, so there's always a demand," \
" the adventurer's guild is paying 30 copper coins for every 10 slime chunks handed in",
requirements = {'slime chunk': 10}, reward = {'copper coin': 30}, type = 'unlimited', stage = None),

'clear rat infestation': Quests(name = 'Clear Rat Infestation', id = 'clear rat infestation', 
description = 
"""the farms are overrun with mutated rats, so the farmers have pooled their money
to issue a quest at the adventurer's guild, requesting that the pesky rodents be taken care of""",
requirements = {'magic mutated rat skin': 100},
reward = {'silver coin': 30}, type = 'singular', stage = None),
}