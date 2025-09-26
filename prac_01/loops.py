"""
CP1404/CP5632 - Practical
different number or star generating loops
"""

# 1 to 20 in steps of 1 with a space between each
for i in range(1, 21, 2):
    print(i, end=' ')
print()
# a. counts from 0 to 100 in steps of 10 with a space between each
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# b. counts down from 20 to 0 in steps of 1 with a space between each
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. asks user for a number and prints number of stars on single line without a space between each
number_of_stars = int(input("Number of stars: "))
if number_of_stars > 0:
    for i in range(number_of_stars):
        print("*", end="")
        i += 1
    print("")

# d. asks user for number and prints lines of stars with increasing number of stars until it reaches the number
number_of_lines = int(input("Number of lines: "))
if number_of_lines > 0:
    for i in range(number_of_lines):
        print("*" * (i + 1))
