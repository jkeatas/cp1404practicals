"""
Emails
Estimate: 30 minutes
Actual:   20 minutes
"""
email = input("Email: ")
print(email)
name_and_email = {}
while email != "":
    name = email.replace('.', ' ').split("@")
    name.pop()
    name = str(name).strip("[ ]' ' ").title()
    print(name)
    correct = input(f"Is your name {name} (Y/n): ")
    if correct != "" and correct.lower() != "y":
        name = input("Name: ").title()
    name_and_email[str(email).strip("[ ]' ' ")] = name
    email = input("Email: ")
for item in name_and_email:
    print(f"{name_and_email[item]} ({item})")
