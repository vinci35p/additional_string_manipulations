# Input any characters
user_input = str(input("Enter any string characters: "))

# Input how many zeros to add at the beginning
zero_num = int(input("Enter how many zeros to add: "))

# Add zeros at the beginning of the string
modified_char = user_input.rjust(zero_num, '0')

# Print modified string
print(modified_char)