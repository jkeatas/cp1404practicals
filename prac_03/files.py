OUTPUT_FILE = "../../programming2/prac03/name.txt"
out_file = open(OUTPUT_FILE, 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()

IN_FILE = "../../programming2/prac03/name.txt"
in_file = open(IN_FILE, 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

OUTPUT_FILE = "../../programming2/prac03/numbers.txt"
out_file = open(OUTPUT_FILE, 'w')
print("17\n42\n400", file=out_file)
out_file.close()

IN_FILE = "../../programming2/prac03/numbers.txt"
in_file = open(IN_FILE, 'r')
lines_used = in_file.readlines(3)
total = 0
for line in lines_used:
    total += int(line)
print(total)
in_file.close()

IN_FILE = "../../programming2/prac03/numbers.txt"
in_file = open(IN_FILE, 'r')
total = 0
for line in in_file:
    total += int(line)
print(total)
in_file.close()
