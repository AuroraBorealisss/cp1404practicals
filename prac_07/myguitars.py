"""
CP1404/CP5632 Practical - myguitars.py
reading and client program
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
MENU_STRING = f"Menu: \nD - Display guitars \nA - Add a new guitar \nQ - Quit \n>>>"

def main():
    """ Calls loading and saving functionality, runs menu loop. """
    guitars = []
    load_guitars(guitars)
    print("My guitars!")
    display_guitars(guitars)
    menu_choice = input(MENU_STRING).lower()
    while menu_choice != "q":
        if menu_choice == "d":
            display_guitars(guitars)
        elif menu_choice == "a":
            add_new_guitar(guitars)
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU_STRING).lower()
    save_guitars(guitars)


def load_guitars(guitars):
    """ Load guitars from .csv file. """
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    in_file.close()


def display_guitars(guitars):
    """ Displays a sorted inventory of guitars. """
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def add_new_guitar(guitars):
    """ Creates an object called guitar and appends it to guitars. """
    guitar_name = input("Name: ")
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print(guitars[-1], "Added.")


def save_guitars(guitars):
    """ Save guitars to .csv file. """
    guitars.sort()
    for guitar in guitars:
        guitar.year = str(guitar.year)
        guitar.cost = str(guitar.cost)
    with open(FILENAME, "w",encoding='UTF-8') as out_file:
        for guitar in guitars:
            print(repr(guitar),file=out_file)


main()