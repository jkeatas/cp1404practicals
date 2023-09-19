number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_cost = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_cost += price_of_item
if total_cost > 100:
    total_cost -= total_cost * .1
print(f"Total price for 3 items is ${total_cost:.2f}")
