# Input full name with spaces after
user_name = str(input("Enter your full name with several spaces after: "))

# Remove spaces after name
spaceless_name = user_name.rstrip()

# Print spaceless name
print(spaceless_name)