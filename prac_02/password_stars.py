"""
CP1404/CP5632 - Practical
password_stars
get minimum length password, print asterisks length of password
"""
PASSWORD_MINIMUM_LENGTH = 10


def main():
    """print stars length of password"""
    password = get_password()
    print_stars(len(password))


def print_stars(number_of_stars):
    """ Print parameter: 'number_of_stars' number of stars """
    print("*" * number_of_stars)


def get_password() -> str:
    """ check password by length """
    password = input("input password: ")
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        password = input(f"Too short, please input password with a minimum {PASSWORD_MINIMUM_LENGTH} characters:")
    return password


main()
