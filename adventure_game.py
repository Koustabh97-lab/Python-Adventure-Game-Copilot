# the purpose of this code is to create an adventure game
# Task 1
print('Setup is Working 100%')

# Task 2
def start_game():
    player_name = input('Enter your name: ')
    print(f"\nWelcome, {player_name}! Your adventure begins at the edge of a dark forest.")
    print("Before you stands a mysterious, ancient forest. To your right, you see the dark entrance to a cave.")
    print("\nWhat will you do?")
    print("1. Explore the forest.")
    print("2. Enter the cave.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        forest_path()
    elif choice == '2':
        cave_path()
    else:
        print("Invalid choice. The adventure ends before it begins. Please restart.")

def forest_path():
    """Placeholder for the forest adventure path."""
    print("\nYou step into the eerie silence of the forest...")
    print("After walking for what feels like hours, you come across a gently flowing river cutting through the woods.")
    print("The trees here are tall and ancient, with low-hanging branches perfect for climbing.")
    print("\nWhat is your next move?")
    print("1. Follow the river downstream.")
    print("2. Climb a tree to get a better view.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        river_path()
    elif choice == '2':
        tree_path()
    else:
        print("Invalid choice. You hesitate for too long and a shadow passes over you. The adventure ends here.")

def cave_path():
    """Placeholder for the cave adventure path."""
    print("\nYou cautiously enter the echoing darkness of the cave...")
    print("The air is damp and cold. You can hear the faint sound of dripping water.")
    print("You have a torch and flint in your pack, but using it might attract unwanted attention.")
    print("\nWhat will you do?")
    print("1. Light your torch.")
    print("2. Proceed in the dark.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        torch_lit_path()
    elif choice == '2':
        dark_path()
    else:
        print("Invalid choice. You stumble in the darkness and the adventure ends.")


def river_path():
    """Placeholder for the river path adventure."""
    print("\nYou decide to follow the river, hoping it leads to civilization...")

def tree_path():
    """Placeholder for the tree path adventure."""
    print("\nYou begin to climb a massive oak tree, pulling yourself up branch by branch...")

def torch_lit_path():
    """Placeholder for the torch-lit cave path."""
    print("\nThe torch springs to life, revealing ancient carvings on the cave walls...")

def dark_path():
    """Placeholder for the dark cave path."""
    print("\nYou decide to save your torch and feel your way along the cold, damp wall...")

# Start the game
while True:
    # This line starts a new adventure
    start_game()

    # Ask the player if they want to play again after their journey ends
    play_again = input("\nYour journey has concluded. Do you want to play again? (yes/no): ").lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye.")
        break
    print("\n--- Starting a new adventure! ---")
    