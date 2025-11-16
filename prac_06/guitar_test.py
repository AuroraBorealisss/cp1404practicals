"""
CP1404/CP5632 Practical - guitar_test.py
test program for class definition Guitar
"""

from prac_06.guitar import Guitar

def main():
    gibson_guitar = Guitar("Gibson L-5 CES",1922, 16035.40)
    edge_case_guitar = Guitar("50-year old guitar", 1975, 240)
    another_guitar = Guitar("Another Guitar", 2016, 16)
    a_fourth_guitar = Guitar("A fourth, really??", 1976, 100000.4222)
    guitars = [gibson_guitar, edge_case_guitar, another_guitar, a_fourth_guitar]


    expected_ages = [103, 50, 9, 49]
    expected_is_vintages = [True, True, False, False]

    for index, guitar in enumerate(guitars):
        print(f"{guitar.name} get age () - expected {expected_ages[index]}. Got {guitar.get_age()}")

    print("-"*60 + "\n")
    for index, guitar, in enumerate(guitars):
        print(f"{guitar.name} is_vintage() - expected {expected_is_vintages[index]}. Got {guitar.is_vintage()}")

if __name__ == "__main__":
    main()