import random
AMOUNT_OF_RANDOM = 6
MIN_RANDOM = 1
MAX_RANDOM = 45
amount_of_quick_picks = int(input("How many quick picks? "))
for i in range(amount_of_quick_picks):
    line = []
    for j in range(AMOUNT_OF_RANDOM):
        j = random.randint(MIN_RANDOM, MAX_RANDOM)
        if j in line:
            j = random.randint(MIN_RANDOM, MAX_RANDOM)
        line.append(j)
    line.sort()
    for item in line:
        print(f"{item:>2}", end=" ")
    print()
