# Input sentence
user_sentence = str(input("Enter a sentence: "))

# Input desired word to be indexed
user_word = str(input("Enter a character to find: "))

# Find desired in provided sentence, then determine its placement, then print its placement in the sentence
for i in range(len(user_sentence) - len(user_word) + 1):
    if user_sentence[i: i + len(user_word)] == user_word:
        print(f"The first location of {user_word} in the sentence, is at index: {i}")
        break

# Else, if not found, print not found in list
    else:
        print(f"The indicated character was not found in the sentence.")