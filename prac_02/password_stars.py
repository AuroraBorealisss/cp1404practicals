"""password_stars.py"""
PASSWORD_MINIMUM_LENGTH = 10
def main():
    """print stars length of password"""
    password = get_password()
    print(write_stars(password))


def write_stars(password: str):
    """write line of stars length of password"""
    return "*" * len(password)


def get_password() -> str:
    """check password"""
    password = ""
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        password = input("input password: ")
    return password


main()