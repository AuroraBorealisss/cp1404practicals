"""
CP1404/CP5632 - Practical
score_menu
get score (0-100 inclusive), run menu, change score, show result, print stars, farewell
"""
MENU_PROMPT = "Menu Options: \n(G)et a score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit \n>>> "


def main():
    """ run menu loop, call function from user choice """
    score = get_valid_score()
    menu_choice = input(MENU_PROMPT).upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            score = get_valid_score()
        elif menu_choice == "P":
            result = check_result(score)
            print(result)
        elif menu_choice == "S":
            print_stars(score)
        else:
            print("Invalid menu choice, try again")
        menu_choice = input(MENU_PROMPT).upper()
    print("So long and thanks for all the fish")


def print_stars(number_of_stars):
    """ 'Print as many stars as the score' - Lindsay Ward """
    print("*" * number_of_stars)


def get_valid_score():
    """ Get valid score """
    is_valid_input = False
    while not is_valid_input:
        try:
            score = int(input("Enter score: "))
            if not 0 <= score <= 100:
                print("Score must be 0-100 inclusive")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    return score


def check_result(score) -> str:
    """ take user score return result (line: 349-351 Practicals/prac_02/README.md) """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
