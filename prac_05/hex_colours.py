"""
CP1404/CP5632 Practical
"""

COLOUR_TO_CODE = {"absolutezero": "#0048ba", "amaranth": "#e52b50", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                  "blue1": "#0000ff", "blue2": "#0000ee", "celadon": "#ace1af",
                  "ceruleanfrost": "#6d9bc3", "caribbeangreen": "#00cc99", "cadetblue1": "#98f5ff"}
print(COLOUR_TO_CODE)
colour_name = input("Enter colour: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
        colour_name = input("Enter colour: ").lower()
    except KeyError:
        print("Invalid colour")
        colour_name = input("Enter colour: ").lower()
