# Imports, a lot of them
import time
import shutil
import sys
import os
import Zones
import titlescreen
import weapons
import characters
import random
import json
from characters import add_to_inventory
from characters import display_inventory
from characters import Character
from characters import Enemy


def save():
    # Save player data
    with open('save file.json', 'w') as save_file:
        player_data = {'name': player.name,
               'hp': player.hp,
               'maxhp': player.max_hp,
               'inventory': player.inv,
               'weapon': player.weapon.name,
               'location': current_location.id
                    }
        json.dump(player_data, save_file, indent=4)
    # Save map data
    with open('zones save file.json', 'w') as zone_save_file:
        zones_data = {'town square items': Zones.zones['town square'].item,
                'town market items': Zones.zones['town market'].item,
                'town exit items': Zones.zones['town exit'].item,
                'forest 0 0 items': Zones.zones['forest 0 0'].item
                   }
        json.dump(zones_data, zone_save_file, indent=4)

def load():
    # Load save file
    global player_data
    with open('save file.json') as player_save:
        player_data = json.load(player_save)

def wipe():
    # Wipes save file
    player_default_start = 'player default start.json'
    zones_default_start = 'zones default start.json'
    player_save = 'save file.json'
    zones_save = 'zones save file.json'
    shutil.copy2(player_default_start, player_save)
    shutil.copy2(zones_default_start, zones_save)

def enemy_spawn():
    # this "spawns" the enemy
    if battling == False:
        if current_location.danger == 'Low Danger':
            random_chance = random.randint(0, 100)
            if random_chance <= 30:
                chosen_enemy = random.choice(weak_enemies)
                return chosen_enemy
            else:
                print("you are safe, for now...")
                return False
    else:
        return False

def battle(enemy):
    # Battle system, gotta maybe improve this later, low priority really
    if player.hp <= 0:
        print('GAME OVER!')
        input('>')
        sys.exit()
    if enemy.hp <= 0 and player.hp > 0:
        add_to_inventory(player.inv, enemy.loot)
        characters.Enemy.ressurection(enemy)
        return False
    player.attack(target=enemy)
    print(f'{player.name} has attacked {enemy.name} with {player.weapon.name} for {player.weapon.dmg}.')
    print(f'{enemy.name} has {enemy.hp} health left')
    input('>')
    Enemy.attack(self=enemy, target=player)
    print(f'{enemy.name} has attacked {player.name} with {enemy.weapon.name} for {enemy.weapon.dmg}')
    print(f'{player.name} has {player.hp} health left')
    input('>')

# Some variables, suspect moving these breaks the code
player_data = {}
current_location = Zones.zones['town square']

# Title screen
return_output =  titlescreen.title_screen_options()

# Wipe save file or load save file
if return_output == 'wipe':
    wipe()
    print('overwriting...')
    time.sleep(1)
    print(Zones.zones['town square'].name + '\n' + Zones.zones['town square'].description)
    load()
elif return_output == 'load':
    load()
    print(Zones.zones[player_data['location']].name + '\n' + Zones.zones[player_data['location']].description)

# Some variables
player = Character(name=player_data['name'], max_hp=player_data['maxhp'], hp=player_data['hp'],
                   inv=player_data['inventory'], weapon=weapons.weapons[player_data['weapon']])
weak_enemies = [characters.goblin, characters.slime]
battling = False
current_location = Zones.zones[player_data['location']]

# Main loop
while True:

    # Decides whether to spawn an enemy
    if current_location.danger != 'No Danger' and enemy_spawn()  and battling == False:
        enemy_spawned = enemy_spawn()
        if enemy_spawned != False:
            battling = True
            print(f"you've encountered a(n) {enemy_spawned.name}!")

    # Battles the enemy i think
    while battling == True:
        if battle(enemy_spawned) == False:
            battling = False
        else:
            battling = True
    


    # Inv display
    player_input = input('>').lower()
    if player_input == 'inv':
        display_inventory(player.inv)

    # Look around
    elif player_input in ['look', 'examine']:
        print(current_location.name)
        print(current_location.description)
        print('you see: ' + str(current_location.item) + ' in this place')
    
    # Status menu
    elif player_input in ['status', 'stats']:
        print(
f"""Name: {player.name} 
Health: {player.hp}/{player.max_hp} 
Weapon Name: {player.weapon.name}
Weapon Type: {player.weapon.type}
Weapon Damage: {player.weapon.dmg}
""")    
    
    # Taking stuff from the zone
    elif player_input in ['take', 'get']:
        print('what would you like to take: ' + str(current_location.item)  + '?')
        action = input('>').lower()
        if action in current_location.item:
            output = current_location.getItem(action)
            add_to_inventory(player.inv, output)
        else:
            print('no such item')
    
    # Change weapon
    elif player_input in ['switch', 'change', 'equip', 'swap']:
        print(f'to which weapon would you like to change?{player.inv}')
        player.change_weapon()

    # Moving around
    elif player_input in ['move', 'go', 'travel']:
        print('where would you like to go?')
        direction = input('>').lower()
        if direction == 'north' and current_location.north != None:
            current_location = current_location.north
            print(current_location.name + '\n' + current_location.description)
        elif direction == 'south' and current_location.south != None:
            current_location = current_location.south
            print(current_location.name + '\n' + current_location.description)
        elif direction == 'east' and current_location.east != None:
            current_location = current_location.east
            print(current_location.name + '\n' + current_location.description)
        elif direction == 'west' and current_location.west != None:
            current_location = current_location.west
            print(current_location.name + '\n' + current_location.description)
        else:
            print('invalid command')
    
    # Quit command
    elif player_input == 'quit':
        save()
        sys.exit()
    
    # Save
    elif player_input == 'save':
        save()
    
    # Wait a turn
    elif player_input == '':
        print('waited 1 turn')
    else:
        print('invalid command')
    