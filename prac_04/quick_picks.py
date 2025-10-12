"""
CP1404/CP5632 Practical
quick picks
"""
import random

MAXIMUM = 45
MINIMUM = 1

LINE_LENGTH = 6


number_of_quick_picks = int(input("how many quick picks:"))

for i in range(number_of_quick_picks):
    quick_pick = []
    for pick in range(LINE_LENGTH):
        number = random.randint(MINIMUM, MAXIMUM)
        if number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(' '.join(f"{number:2}" for number in quick_pick))