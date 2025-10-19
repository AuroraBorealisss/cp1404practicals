"""
CP1404/CP5632 Practical
Program to store user's email and names in a dictionary
"""
# TODO: finish writing iterating loop in main() (might pay to test it too, doombry). Write for email in email_to_name loop as exit path like: name (with brackets around email)
# def main():
""" does the important stuff i hope"""
#     email_to_name = {}
#     email = input("Email: ")
#     while email != "":
#         name = get_name_from_email(email)
#         is_name = input(f"Is your name {get_name_from_email(email)}")
#         if is_name != 'Y'.isupper():
#             name = input("Name:")
#         email_to_name[email] = name





def get_name_from_email(email):
    """ function to extract and format name from email's local-part """
    local_part = email.split('@')[0]
    local_parts = local_part.split('.')
    name = " ".join(local_parts).title()
    return name
