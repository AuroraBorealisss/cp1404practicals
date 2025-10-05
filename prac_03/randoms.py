"""
CP1404/CP5632 - Practical
Answer the following questions:
1.
    a) What did you see on line 1?
    an integer between 5 and 20
    b) What was the smallest number you could have seen, what was the largest?
    smallest: 20
    largest: 20
2.
    a) What did you see on line 2?
    an odd integer between 2 and 10 (3, 5, 7, 9)
    b) What was the smallest number you could have seen, what was the largest?
    smallest: 3
    largest: 9
    c) Could line 2 have produced a 4?
    no, the step is 2, the lower bound is 3, it could not produce a 2.


3.
    a) What did you see on line 3?
    a number between 3.5 and 5.5 with 15 decimal places
    b) What was the smallest number you could have seen, what was the largest?
    smallest: 2.5
    largest: 5.5
"""

import random
print(random.randint(1, 100))
