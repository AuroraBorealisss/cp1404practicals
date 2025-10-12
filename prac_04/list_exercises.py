"""
CP1404/CP5632 Practical
Program that adds user inputted number to list for a constant number times
displays first, last, smallest, largest and overall average of list
"""
NUMBER_OF_NUMBERS = 5 # Allows programmer to easily change number of numbers for the user to input

numbers = [] # initialises list called numbers

for i in range(0,NUMBER_OF_NUMBERS): # loops for NUMBER_OF_NUMBERS number of times
    numbers.append(int(input("Number: "))) # adds number to numbers until numbers has NUMBER_OF_NUMBERS number of numbers

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

"""
Woefully inadequate security checker
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username:")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")