"""Calculate Area"""


def main():
    """Main Function"""
    length = float(input("Length: "))
    width = float(input("Width: "))
    print(calculate_area(length, width))


def calculate_area(x, y):
    """Calculates area from 2 inputs"""
    area = x * y
    return area

main()
