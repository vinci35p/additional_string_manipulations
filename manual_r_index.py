# Input sentence
user_sentence = str(input("Enter a sentence: "))

# Input desired word to be indexed
user_word = str(input("Enter a character to find: "))

# Find desired word starting from the end, then determine its placement, then print its placement
for index in range(len(user_sentence) - len(user_word), -1, -1):
    if user_sentence[index:index + len(user_word)] == user_word:
        print(f"The first location of {user_word} in the sentence, is at index: {index}")
        break

# Else, if not found, print not found in sentence
    else:
        print(f"The indicated character was not found in the sentence.")