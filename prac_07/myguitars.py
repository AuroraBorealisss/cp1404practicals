"""
CP1404/CP5632 Practical - myguitars.py
reading program
"""
from prac_07.guitar import Guitar


def main():
    guitars = []
    load_guitars(guitars)
    display_guitars(guitars)
    print("")
    sort_guitars(guitars)


def load_guitars(guitars):
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    in_file.close()


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def sort_guitars(guitars):
    guitars.sort()
    display_guitars(guitars)



main()