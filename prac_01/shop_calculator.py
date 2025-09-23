"""
CP1404/CP5632 - Practical
# asks user for number of items, prices of items, calculates and prints total price
"""


total_price_of_items = 0
number_of_items = 0
while number_of_items==0:
    number_of_items = int(input("Number of items:"))
    if number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price_of_items += price_of_item
    i += 1
print(f"Total price for {number_of_items} is ${total_price_of_items:.2f}")