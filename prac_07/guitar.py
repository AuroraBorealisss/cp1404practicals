"""
CP1404/CP5632 Practical - guitar.py
Class definition Guitar
"""
CURRENT_YEAR = 2025
VINTAGE = 50

class Guitar:

    def __init__(self, name="",year=0,cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        return f"{self.name:>25}, ({self.year}) : ${self.cost:.2f}"


    def __repr__(self):
        return f"{self.name}, {self.year}, {self.cost}"


    def get_age(self):
        """ Get year of creation, return age of guitar. """
        return 2025 - self.year


    def is_vintage(self):
        """ Determines if the guitar is vintage. """
        return self.get_age() >= VINTAGE

    def __lt__(self, other):
        return self.year < other.year