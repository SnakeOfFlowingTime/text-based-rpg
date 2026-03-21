# Imports, a lot of them
import time, shutil, sys, os, Zones, titlescreen, armor, weapons, characters, random, json, npcs
from characters import add_to_inventory
from characters import display_inventory
from characters import Character
from characters import Enemy

def file_path(relative_path):
    # For the .exe to find the .json file needed to work
    try:
        base_path = sys._MEIPASS
    except Exception: 
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def save():
    # Save player data
    player_save = file_path('save file.json')
    with open(player_save, 'w') as save_file:
        player_data = {'name': player.name,
               'hp': player.hp,
               'maxhp': player.max_hp,
               'inventory': player.inv,
               'weapon': player.weapon.id,
               'armor': player.armor.id,
               'level': player.lvl,
               'exp': player.exp,
               'money': player.money,
               'location': current_location.id
                    }
        json.dump(player_data, save_file, indent=4)
    
    # Save map data
    zone_save = file_path('zones save file.json')
    with open(zone_save, 'w') as zone_save_file:
        zones_data = {'town square items': Zones.zones['town square'].item,
                'town market items': Zones.zones['town market'].item,
                'town exit items': Zones.zones['town exit'].item,
                'forest 0 0 items': Zones.zones['forest 0 0'].item
                   }
        json.dump(zones_data, zone_save_file, indent=4)

    # Save merchant data
    merchant_file = file_path('merchant save file.json')
    with open(merchant_file, 'w') as merchant_save:
        merchant_data = {'town market merchant stock': npcs.merchants['town merchant'].selling
                         }
        json.dump(merchant_data, merchant_save, indent=4)

def load():
    # Load player data
    global player_data
    player_file = file_path('save file.json')
    with open(player_file) as player_save:
        player_data = json.load(player_save)

def wipe():
    # Wipes save file
    player_default_start = file_path('player default start.json')
    zones_default_start = file_path('zones default start.json')
    merchant_default_start = file_path('merchant default start.json')
    player_save = file_path('save file.json')
    zones_save = file_path('zones save file.json')
    merchant_save = file_path('merchant save file.json')
    shutil.copy2(player_default_start, player_save)
    shutil.copy2(zones_default_start, zones_save)
    shutil.copy2(merchant_default_start, merchant_save)

def enemy_spawn(number):
    # this "spawns" the enemy
    if battling == False:
        if current_location.danger == 'Very Low Danger':
            if number == 1:
                random_chance = random.randint(0, 30)
            else:
                random_chance = random.randint(0, 100)
            if random_chance <= 30:
                chosen_enemy = random.choice(very_weak_enemies)
                return chosen_enemy
            else:
                print("you are safe, for now...")
                return False
        elif current_location.danger == 'Low Danger':
            if number == 1:
                random_chance = random.randint(0, 60)
            else:
                random_chance = random.randint(0, 100)
            if random_chance <= 30:
                chosen_enemy = random.choice(weak_enemies)
                return chosen_enemy
            elif random_chance <= 60 and random_chance > 30:
                chosen_enemy = random.choice(very_weak_enemies)
                return chosen_enemy
            else:
                print("you are safe, for now...")
                return False
    
    else:
        return False

def battle(enemy):
    # Battle system, now improved
    if player.hp <= 0:
        print('GAME OVER!')
        input('>')
        sys.exit()
    
    # Player action
    print('what do you do?')
    print('(a)ttack, (u)se item, (e)scape, or (s)kip turn?')
    player_input = input('>').lower()
    
    # Attack
    if player_input in ['attack', 'hit', 'a']:
        player.attack(target = enemy)
        if enemy.armor.defense <= player.weapon.dmg:
            print(f'{player.name} has attacked {enemy.name} with {player.weapon.name} for {player.weapon.dmg - enemy.armor.defense}.')
        elif enemy.armor.defense > player.weapon.dmg:
            print(f'{player.name} has attacked {enemy.name} with {player.weapon.name} for 0.')
        print(f'{enemy.name} has {enemy.hp} health left')
        input('>')
    # Use
    elif player_input in ['use', 'consume', 'u']:
        print(f"which item would you like to {player_input}? {player.inv}")
        player.heal_self()
    # Escape
    elif player_input in ['escape', 'run', 'e']:
        characters.Enemy.ressurection(enemy)
        return False
    # Skip turn
    elif player_input in ['skip', 's']:
        pass

    else:
        return True
    
    # What to do when win
    if enemy.hp <= 0 and player.hp > 0:
        add_to_inventory(player.inv, enemy.loot)
        player.exp += enemy.expvalue
        print(f"Exp + {enemy.expvalue}")
        characters.Enemy.ressurection(enemy)
        return False
    
    # Enemy attack
    Enemy.attack(self=enemy, target=player)
    if player.armor.defense <= enemy.weapon.dmg:
        print(f'{enemy.name} has attacked {player.name} with {enemy.weapon.name} for {enemy.weapon.dmg - player.armor.defense}')
    elif player.armor.defense > enemy.weapon.dmg:
        print(f'{enemy.name} has attacked {player.name} with {enemy.weapon.name} for 0')
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
    print('please rejoin to load new save')
    input('>')
    sys.exit()
elif return_output == 'load':
    load()
    print(Zones.zones[player_data['location']].name + '\n' + Zones.zones[player_data['location']].description)

# Some variables
player = Character(name=player_data['name'], max_hp=player_data['maxhp'], hp=player_data['hp'],
                   inv=player_data['inventory'],armor=armor.armors[player_data['armor']],
                    weapon=weapons.weapons[player_data['weapon']], lvl=player_data['level'],
                    exp=player_data['exp'], money=player_data['money'])

very_weak_enemies = [characters.enemies['goblin'], characters.enemies['slime']]
weak_enemies = [characters.enemies['wild boar'], characters.enemies['wolf'], characters.enemies['bear']]
battling = False
current_location = Zones.zones[player_data['location']]

# Main loop
while True:

    # Decides whether to spawn an enemy
    if current_location.danger != 'No Danger' and enemy_spawn(0) and battling == False:
        enemy_spawned = enemy_spawn(0)
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
    if player_input in ['inv', 'inventory', 'items']:
        display_inventory(player.inv)

    # Look around
    elif player_input in ['look', 'examine']:
        print(current_location.name)
        print(current_location.description)
        if current_location.npc != None:
            print('you see a(n): ' + str(current_location.npc))
        print('you see: ' + str(current_location.item) + ' in this place')
    
    # Starts a fight
    elif player_input in ['fight', 'battle']:
        if current_location.danger != 'No Danger' and enemy_spawn(1) and battling == False:
            enemy_spawned = enemy_spawn(1)
        else:
            enemy_spawned = False
        if enemy_spawned != False:
            battling = True
            print(f"you've encountered a(n) {enemy_spawned.name}!")
        else:
            print(f"there's no one to {player_input} here")

    # Status menu
    elif player_input in ['status', 'stats']:
        print(
f"""Name: {player.name} 
Level: {player.lvl}
Health: {player.hp}/{player.max_hp} 
Exp: {player.exp}/{player.lvl * 100}
Weapon Name: {player.weapon.name}   Armor Name: {player.armor.name} 
Weapon Type: {player.weapon.type}   Armor Type: {player.armor.type}
Weapon Damage: {player.weapon.dmg}  Armor Defense: {player.armor.defense}
Money: {player.money}
""")    
    
    # Selling stuff
    elif player_input in ['sell']:
        if current_location.npc != None:
            print(f'which merchant would you like to sell stuff to: {current_location.npc}?')
            answer = input('>').lower()
            if answer in current_location.npc:
                npcs.merchants[answer].buy(player)
        else:
            print("there's no merchant here to sell stuff to")

    # Buying stuff
    elif player_input in ['buy', 'acquire']:
        if current_location.npc != None:
            print(f'from which merchant would you like to buy stuff from: {current_location.npc}?')
            answer = input('>').lower()
            if answer in current_location.npc:
                npcs.merchants[answer].sell(player)
        else:
            print("there's no merchant here to buy from")

    # Taking stuff from the zone
    elif player_input in ['take', 'get']:
        print(f'what would you like to {player_input}: ' + str(current_location.item)  + '?')
        action = input('>').lower()
        if action in current_location.item:
            output = current_location.getItem(action)
            add_to_inventory(player.inv, output)
        else:
            print('no such item')
    
    # Change weapon and armor
    elif player_input in ['switch', 'change', 'equip', 'swap']:
        print(f"what would you like to {player_input}? ['armor'] or ['weapon']")
        sub_input = input('>').lower()
        if sub_input == 'weapon':
            print(f'to which weapon would you like to {player_input}? {player.inv}')
            player.change_weapon()
        elif sub_input == 'armor':
            print(f'to which armor would you like to {player_input}? {player.inv}')
            player.change_armor()
        else:
            print(f'no such item type: {sub_input}')
    
    # Use items, just heals for now though
    elif player_input in ['use', 'consume']:
        print(f"which item would you like to {player_input}? {player.inv}")
        player.heal_self()
    
    # Level up
    elif player_input in ['lvl up', 'lvlup', 'level up']:
        player.lvlup()
    
    # Rest to heal, also save
    elif player_input in ['rest', 'sleep']:
        # Save just in case someone inputs 99999999... and get stuck waiting for 2 irl years or smth
        save()
        player.rest()
        save()

    # Moving around
    elif player_input in ['move', 'go', 'travel', 'm']:
        print(f'where would you like to {player_input}?')
        direction = input('>').lower()
        if direction in ['north', 'n'] and current_location.north != None:
            current_location = current_location.north
            print(current_location.name + '\n' + current_location.description)
        elif direction in ['south', 's'] and current_location.south != None:
            current_location = current_location.south
            print(current_location.name + '\n' + current_location.description)
        elif direction in ['east', 'e'] and current_location.east != None:
            current_location = current_location.east
            print(current_location.name + '\n' + current_location.description)
        elif direction in ['west', 'w'] and current_location.west != None:
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
    