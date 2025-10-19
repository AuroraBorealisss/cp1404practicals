"""
CP1404/CP5632 Practical
Program to store user's email and names in a dictionary
"""
# TODO: Write for email in email_to_name loop as exit path like: name (with brackets around email)
# TODO: find the input string that is annoying
def main():
    """ function that enters email and name in dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        is_name = input(f"Is your name {get_name_from_email(email)}").upper() # probably bad variable name, check styleguide or whatevr from prac3 response
        if is_name != 'Y':
            name = input("Name:")
        email_to_name[email] = name
        email = input("Email: ")





def get_name_from_email(email):
    """ function to extract and format name from email local-part """
    local_part = email.split('@')[0]
    local_parts = local_part.split('.')
    name = " ".join(local_parts).title()
    return name

main()