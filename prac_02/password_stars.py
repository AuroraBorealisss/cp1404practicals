"""password_stars.py"""
password_minimum_length = 10
password = ""
while len(password) < password_minimum_length:
    password = input("input password: ")
print("*" * len(password))