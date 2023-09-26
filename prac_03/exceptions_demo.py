"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a float is inputted
2. When will a ZeroDivisionError occur?
When the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, either a while loop to get a number above 0 or set the minimum possible number to 1
using an if statement
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator < 1:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
