import zones

# Interaction
def title_screen_options():
    import sys
    option = input('>').lower()
    if option == 'play':
        start_game()
    if option == 'help':
        help_menu()
    if option == 'quit':
        sys.exit()
    while option not in ['play', 'help', 'quit']:
        print('please enter a valid option')
        option = input('>').lower()
        if option == 'play':
            start_game()
        if option == 'help':
            help_menu()
        if option == 'quit':
            sys.exit()

# Main menu
def title_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome to Placeholder Text-Based RPG Game')
    print("Type 'play' to start the game")
    print("Type 'help' to open the help menu")
    print("Type 'quit' to close the game")
    title_screen_options()

# Help menu
def help_menu():
    print("use 'go' to move, 'take' to take items, 'look' to survey the surroundings")
    print("Type 'back' to go back to the main menu")
    if input('>').lower() == 'back':
        title_screen()

# Game start
def start_game():
    print(zones.zones['town square'].name + '\n' + zones.zones['town square'].description)