"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Get a score and print result"""
    score = float(input("Enter score: "))
    print(check_score(score))


def check_score(score) -> str:
    """determine result from parameter score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()