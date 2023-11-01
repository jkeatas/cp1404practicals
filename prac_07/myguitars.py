from prac_07.guitar import Guitar
from operator import itemgetter

FILENAME = 'guitars.csv'
print("My Guitars!")
guitars = []
input_file = open(FILENAME)
for line in input_file:
    line = line.strip()
    parts = line.split(',')
    parts[1] = int(parts[1])
    parts[2] = float(parts[2])
    guitars.append(Guitar(parts[0], parts[1], parts[2]))
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")
input_file.close()
output_file = open(FILENAME, "w")
for guitar in guitars:
    output_file.write(str(guitar) + "\n")
output_file.close()
guitars.sort()
for guitar in guitars:
    print(guitar)
