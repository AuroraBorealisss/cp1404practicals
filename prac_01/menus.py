"""
CP1404/CP5632 - Practical
# asks users name, opens menu with hello, goodbye, quit, runs menu until user quits
"""


MENU_OPTIONS = "(H)ello \n(G)oodbye \n(Q)uit"
name = input("Enter name: ")
print(MENU_OPTIONS)
choice = input(">>>")
while choice != "Q":
   if choice == "H":
       print(f"Hello {name}")
   elif choice == "G":
       print(f"Goodbye {name}")
   else:
       print("Invalid choice")
   print(MENU_OPTIONS)
   choice = input(">>>")
print("Finished.")
