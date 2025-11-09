"""
CP1404/CP5632 Practical
Program to store user's email and names in a dictionary
"""

def main():
    """ function that enters email and name in dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        is_name = input(f"Is your name {get_name_from_email(email)}? (Y/n) ").upper()
        if is_name != 'Y':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        """print all names and emails in dictionary"""
        print(f"{name} ({email})")



def get_name_from_email(email):
    """ function to extract and format name from email local-part """
    local_part = email.split('@')[0]
    local_parts = local_part.split('.')
    name = " ".join(local_parts).title()
    return name

main()