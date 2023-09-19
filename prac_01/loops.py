for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star_amount = int(input("Number of stars: "))
for i in range(star_amount):
    print("*", end='')
print()

star_amount = int(input("Number of stars: "))
star_count = 1
for i in range(star_amount):
    print("*" * star_count)
    star_count += 1
print()