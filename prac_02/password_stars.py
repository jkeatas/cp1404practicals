"""Password stars"""


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("Password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
