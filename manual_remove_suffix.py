# Input any characters
user_input = str(input("Enter any characters that has several numbers at the end: "))

# Indicate suffix to remove
user_num = int(input("Enter the numbers at the end you want to remove: "))

# Remove desired suffix
new_input = user_input.rstrip(str(user_num))

# Print new string
print(new_input)