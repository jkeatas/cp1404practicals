import csv
filename = "wimbledon.csv"
print("Wimbledon Champions:")
champions_to_victories = {}
champions = []
champion_countries = []
longest_name = 0
with open(filename, "r") as in_file:
    reader = csv.reader(in_file)
    next(reader)
    for record in reader:
        champion = (record[2])
        champions.append(champion)
        if record[3] not in champion_countries:
            champion_countries.append(record[3])
        if len(champion) > longest_name:
            longest_name = len(champion)
    for item in champions:
        champions_to_victories[str(item)] = champions.count(item)
    for item in champions_to_victories:
        print(f"{item:<{longest_name}} : {champions_to_victories[item]}")

print(f"These {len(champion_countries)} countries have won championships: \n {', '.join(champion_countries)}")
