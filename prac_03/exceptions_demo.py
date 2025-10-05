"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ValueError will occur when the user input a value that is not an integer (when numerator or denominator is not integer)
2. When will a ZeroDivisionError occur?
When the denominator is 0 (because the answer is undefined)
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
by using the error checking loop in the programming patterns one could make the program only finish once both potential
errors have been rectified, this ensures that the program avoids a ZeroDivisionError.
"""
is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        is_valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")

print(fraction)# cannot reach without defining

print("Finished.")
