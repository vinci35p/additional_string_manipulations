# Input any characters
user_input = str(input("Enter any string characters: "))

# Input how many characters desired
desired_char = str(input(f"Enter desired whole characters width (current width count : {len(user_input)}): "))

# Justify string based on number of characters desired
just_char = "{:<{}}".format(user_input, desired_char)

# Print the justified string
print(just_char)