import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("\nYou wake up in a dark, unfamiliar forest.")
    print_pause("The trees are tall, the air is cold, and you hear distant howling.")
    print_pause("You have no memory of how you got here.")
    print_pause("There’s a path in front of you leading deeper into the woods.")
    print_pause("You check your pockets and find a flashlight and a pocket knife.")
    return ['flashlight', 'pocket knife']

def choose_path():
    print("\nDo you want to:")
    print("1. Follow the path")
    print("2. Explore off the trail")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ['1', '2']:
            return choice
        print("Invalid input.")

def follow_path(inventory):
    print_pause("\nYou cautiously follow the path.")
    print_pause("Suddenly, a wild wolf jumps out!")
    if 'pocket knife' in inventory:
        print_pause("You draw your pocket knife and scare the wolf off. You survive!")
        return True
    else:
        print_pause("You have nothing to defend yourself with.")
        print_pause("The wolf attacks...")
        return False

def explore_off_trail(inventory):
    print_pause("\nYou wander into the thick brush.")
    print_pause("You find a hidden cabin.")
    print("\nDo you want to:")
    print("1. Enter the cabin")
    print("2. Keep walking")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            return enter_cabin(inventory)
        elif choice == '2':
            return keep_walking(inventory)
        print("Invalid input.")

def enter_cabin(inventory):
    print_pause("\nYou enter the dusty, abandoned cabin.")
    if 'map' not in inventory:
        print_pause("You find a map inside! It shows a way out of the forest.")
        inventory.append('map')
    else:
        print_pause("It’s empty now — you’ve already taken the map.")
    print_pause("You head back outside.")
    return explore_off_trail(inventory)

def keep_walking(inventory):
    print_pause("\nAs you walk deeper into the woods...")
    if 'map' in inventory:
        print_pause("You use the map to find a hidden road.")
        print_pause("You follow it and escape the forest safely!")
        return True
    else:
        print_pause("You walk in circles and get lost.")
        print_pause("Night falls, and you can't find your way out...")
        return False

def play_game():
    inventory = intro()
    path_choice = choose_path()
    
    if path_choice == '1':
        survived = follow_path(inventory)
    else:
        survived = explore_off_trail(inventory)

    if survived:
        print_pause("\n🎉 You survived and escaped the forest!")
    else:
        print_pause("\n💀 Game Over. Try again.")

    replay = input("\nPlay again? (y/n): ").strip().lower()
    if replay == 'y':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
