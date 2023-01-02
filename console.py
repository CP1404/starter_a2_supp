"""..."""

from placecollection import PlaceCollection


def main():
    """..."""
    placecollection = PlaceCollection()
    placecollection.load()
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            display(placecollection)
        elif choice == "R":
            recommend(placecollection)
        elif choice == "A":
            add(placecollection)
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input(">>> ").upper()
    placecollection.save()
    print("Have a nice day :)")


def display_menu():
    """Display the main menu."""
    print("""
D - Display places
R - Recommend random place
A - Add new place
Q - Quit""")


main()
