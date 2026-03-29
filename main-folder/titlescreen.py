# Main Menu, this sucks, had 3 functions at the start, now it's all in one
def title_screen_options():
    import sys
    import os
    valid_command = False
    while valid_command == False: 
        # Main menu text
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to Alchemy Ascension Text RPG')
        print("Type 'play' to start the game")
        print("Type 'help' to open the help menu")
        print("Type 'quit' to close the game") 
        option = input('>').lower()
        # play option
        if option == 'play':
            valid_command = True
            print('do you wish to [Start a New Game (new)]')
            print('or do you wish to [Load Game (load)]')
            answer = input('>').lower()
            
            # Load game
            if answer == 'load':
                return 'load'
            
            # New game
            elif answer == 'new':
                print('are you sure, doing this will wipe your save file? Y/N')
                yes_no = input('>').lower()
                
                # Wipe save file
                if yes_no in ['y', 'yes']:
                    return 'wipe'
                
                # Not wipe save file
                elif yes_no in ['n', 'no']:   
                    valid_command = False
            
            else:
                print("invalid command, command must be 'new' or 'load'")
                valid_command = False
        
        # Help menu, still not very helpfull
        if option == 'help':
            valid_command = False
            print(""" 
================================================================================================================================                
| Note: all commands must be typed exactly or you will get a 'invalid command' prompt.                                         |
|                                                                                                                              |
| Commands: ['look' or 'examine'] to get a name, description and items that can be picked up as well as a list of npcs in      |
|           the current zone;                                                                                                  |
|                                                                                                                              |
| ['status' or 'stats'] to see the status menu;                                                                                |
|                                                                                                                              |
| ['take' or 'get'] to get the items you see using ['look' or 'examine'],                                                      |
| after typing one of the 'take' commands you must type the name of the item;                                                  |
|                                                                                                                              |
| ['switch', 'change', 'equip' or 'swap'] to change current weapon/armor,                                                      |
| after typing the command you must enter the weapon/armor name;                                                               |
|                                                                                                                              |
| ['move', 'go', 'travel', 'm'] to move, after typing the command you must also                                                |
| type one of the four cardinal directions ['north' or 'n', 'south' or 's', 'east' or 'e', 'west' or 'w'];                     |
|                                                                                                                              |
| ['quit'] to quit the game, it will also auto save before exiting;                                                            |
|                                                                                                                              |
| ['save'] to save the game;                                                                                                   |
|                                                                                                                              |
| ['sell'] to sell stuff to a merchant;                                                                                        |
|                                                                                                                              |
| ['buy', 'acquire'] to buy stuff from a merchant;                                                                             |
|                                                                                                                              |
| ['rest', 'sleep'] to rest, resting saves the game and heals for the amount you input, though it does take twice the number   |
| of seconds you input to do so;                                                                                               |
|                                                                                                                              |
| ['lvl up', 'lvlup', 'level up'] to level up, leveling up increases max hp;                                                   |
|                                                                                                                              |
| ['fight', 'battle'] to instantly trigger an encounter, only works in non safe areas;                                         |
|                                                                                                                              |
| Note 2: you can use 'Enter' to skip 1 turn.                                                                                  |
|                                                                                                                              |
| Important: as the game is still in development bugs and crashes will definitely happen, so remember to save your game often. |
================================================================================================================================
""")
            input('>')
        
        # Quit
        if option == 'quit':
            valid_command = True
            sys.exit()
        
        else:
            print("no such command, valid commands: 'play', 'help', 'quit'")
            valid_command = False
