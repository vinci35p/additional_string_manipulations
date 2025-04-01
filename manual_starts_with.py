# Input sentence
user_sentence = str(input("Enter a sentence: "))

# Input word value to check if it matches the starting string
word_value = str(input("Enter desired value to check if it the sentence starts with it: "))

# Print true value if it starts with desired word value
if user_sentence.find(word_value) == 0:
    print(f"The sentence does start with {word_value}.")

# Print false value if it doesn't
else:
    print(f"The sentence doesn't start with {word_value}.")