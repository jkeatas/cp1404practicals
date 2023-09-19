"""score menu"""


def main():
    print_menu()
    choice = get_choice()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid input")
        choice = get_choice()

    print("farewell")


def print_menu():
    print("""    (G)et a valid score
    (P)rint result 
    (S)how stars (this should print as many stars as the score)
    (Q)uit """)


def get_valid_score():
    score = int(input("Score:"))
    while 0 > score or 100 < score:
        print("Invalid input")
        score = int(input("Score:"))
    return score


def get_choice():
    choice = input(">>> ").upper()
    return choice


def get_result(score):
    if score < 50:
        return "Bad"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
