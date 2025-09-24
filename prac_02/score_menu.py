""" score menu """


#import prac_02.score
MENU_PROMPT = "Menu Options: \n(G)et a score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit \n>>> "

def main():
    score = get_valid_score()
    menu_choice = input(MENU_PROMPT).upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            score = get_valid_score()
        elif menu_choice == "P":
            result = check_result(score)
            print(result)
        elif menu_choice == "S":
            print(show_stars(score))
        else:
            print("Invalid menu choice, try again")
        menu_choice = input(MENU_PROMPT).upper()
    print("So long and thanks for all the fish")

def show_stars(score):
    return "*" * score



def get_valid_score():
    is_valid_input = False
    score = ''
    while not is_valid_input:
        try:
            score = int(input("Enter score: "))
            if score <0 or score > 100:
                print("Score must be 0-100 inclusive")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    return score

def check_result(score) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()








