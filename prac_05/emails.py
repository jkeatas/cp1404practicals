"""
Emails
Estimate: 30 minutes
Actual:   20 minutes
"""


def main():
    email = input("Email: ")
    print(email)
    name_and_email = {}
    while email != "":
        extract_name(email)
        name_and_email[str(email).strip("[ ]' ' ")] = name
        email = input("Email: ")
    for item in name_and_email:
        print(f"{name_and_email[item]} ({item})")


def extract_name(email):
    name = email.replace('.', ' ').split("@")
    name.pop()
    name = str(name).strip("[ ]' ' ").title()
    correct = input(f"Is your name {name} (Y/n): ")
    if correct != "" and correct.lower() != "y":
        name = input("Name: ").title()
    return name


main()
