"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    random_score = random.randint(0, 100)
    print(get_result(random_score))


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
