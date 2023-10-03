"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    display_details(get_data())


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        datas.append(parts)
    input_file.close()
    return datas

def display_details(list):
    for item in list:
        print(f"{item[0]} is taught by {item[1]} and has {item[2]} students")

main()
