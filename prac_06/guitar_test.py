from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
gibson = Guitar(name, year, cost)

name = "Another Guitar"
year = 2014
cost = 1
another_guitar = Guitar(name, year, cost)

print(f"Expected 101 got {gibson.get_age(2023)}")
print(f"Expected 9 got {another_guitar.get_age(2023)}")
print(f"Expected True. got {gibson.is_vintage(2023)}")
print(f"Expected False. got {another_guitar.is_vintage(2023)}")
