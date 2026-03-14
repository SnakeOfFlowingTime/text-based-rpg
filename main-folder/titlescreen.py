# Main Menu, this sucks, had 3 functions at the start, now it's all in one
def title_screen_options():
    import sys
    import os
    valid_command = False
    while valid_command == False: 
        # Main menu text
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to Placeholder Text-Based RPG Game')
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
                if yes_no == 'y':
                    return 'wipe'
                
                # Not wipe save file
                elif yes_no == 'n':   
                    valid_command = False
            
            else:
                print("invalid command, command must be 'new' or 'load'")
                valid_command = False
        
        # Help menu, still not very helpfull
        if option == 'help':
            valid_command = False
            print("use 'go' to move, 'take' to take items, 'look' to survey the surroundings")
            input('>')
        
        # Quit
        if option == 'quit':
            valid_command = True
            sys.exit()
        
        else:
            print("no such command, valid commands: 'play', 'help', 'quit'")
            valid_command = False
