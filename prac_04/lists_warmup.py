"""
3
2
1
[3, 1, 4, 1, 5, 9]
[1]
True
False
False
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
print(["ten"] + numbers)

numbers.pop()
numbers.append(1)
print(numbers)

print(numbers[2:-1])
