# Input sentence
user_input = str(input("Enter a sentence: "))

# Input desired word to count
user_word = str(input("Enter desired word to count in the sentence provided: "))

# Count words in sentence
count = 0
start = 0

while True:
    start = user_input.find(user_word, start)
    if start == -1:
        break

    count += 1
    start += len(user_word)

# Print word count
print(count)