from prac_06.guitar import Guitar

print("My Guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")

i = 1
for guitar in guitars:
    vintage_string = ""
    if guitar.is_vintage(2023):
        vintage_string = '(vintage)'
    (print(f"Guitar {i}: {guitar.name: >20} ({guitar.year}), worth ${guitar.cost: 10,.2f} {vintage_string}"))
    i += 1
