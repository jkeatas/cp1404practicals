"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    print_menu()
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            fahrenheit = covert_celsius_to_fahrenheit(float(input("Celsius: ")))
            print(f"Result: {fahrenheit:.2f}F")
        elif choice == "F":
            celsius = covert_fahrenheit_to_celsius(float(input("Fahrenheit: ")))
            print(f"Result: {celsius:.2f}C")
        else:
            print("Invalid option")
        print_menu()
        choice = get_choice()
    print("Thank you.")


def covert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def covert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def print_menu():
    MENU = """        C - Convert Celsius to Fahrenheit
        F - Convert Fahrenheit to Celsius
        Q - Quit"""
    print(MENU)


def get_choice():
    choice = input(">>> ").upper()
    return choice


main()

