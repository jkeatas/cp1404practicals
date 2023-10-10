"""
Word Occurrences
Estimate: 30 minutes 
Actual:   25 minutes
"""
string = input("Text: ")
words = string.split(" ")
string_dictionary = {}
longest_word_length = 0
for item in words:
    item.lower()
    if item in string_dictionary:
        string_dictionary[item] += 1
    else:
        string_dictionary[item] = 1
for item in string_dictionary:
    if len(item) > longest_word_length:
        longest_word_length = len(item)
for item in string_dictionary:
    print(f"{item:{longest_word_length}} : {string_dictionary[item]}")

