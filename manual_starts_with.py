# Input sentence
user_sentence = str(input("Enter a sentence: "))

# Input word value to check if it matches the starting string
word_value = str(input("Enter desired value to check if it the sentence starts with it: "))

# Print true value if it starts with desired word value
if user_sentence[len(word_value):] == word_value:
    print("The sentence starts with the desired value!")

# Print false value if it doesn't
else:
    print("The sentence doesn't start with the desired value.")