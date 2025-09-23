"""password_stars.py"""

def main():
    """check password"""
    password = get_password()
    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))


def get_password() -> str:
    password_minimum_length = 10
    password = ""
    while len(password) < password_minimum_length:
        password = input("input password: ")
    return password


main()