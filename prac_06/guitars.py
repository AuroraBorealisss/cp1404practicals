"""
CP1404/CP5632 Practical - guitars.py
client program for class definition Guitar
"""

from prac_06.guitar import Guitar

def main():
    """ Calls add_guitars until user inputs blank guitar name, then calls print_guitars. """
    print("My guitars!")
    guitars = []
    is_blank_input = False
    while not is_blank_input:
        is_blank_input = add_guitar(guitars)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    if guitars:
        print_guitars(guitars)


def add_guitar(guitars):
    """ Creates an object called guitar and appends it to guitars. """
    guitar_name = input("Name: ")
    if guitar_name == "":
        return True
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print(guitars[-1], "Added.")
    return False

def print_guitars(guitars):
    """ Prints the inventory of guitars. """
    if guitars:
        name_length = max(len(guitar.name) for guitar in guitars)
        cost_length = max(len(str(guitar.cost))for guitar in guitars)
        print("These are my guitars:")
        for index, guitar in enumerate(guitars, 1):
            # print(f"Guitar {index}: {(str(guitar).split(":")[0]).rstrip()}, worth $ {guitar.cost:10,.2f} {"(vintage)" if guitar.is_vintage() else ""} ")
            print(f"Guitar {index}: {guitar.name:>{name_length}}, worth $ {guitar.cost:{cost_length},.2f} {"(vintage)" if guitar.is_vintage() else ""} ")
    else:
        print("What are you waiting for? Better start buying some guitars!")


if __name__ == "__main__":
    main()