def main():
    numbers = "1, 2, 3, 4"
    display_numbers(numbers.split(", "))


def display_numbers(numbers):
    for item in numbers:
        print("..".join(numbers))

main()