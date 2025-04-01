# Input any characters
user_input = str(input("Enter any characters: "))

# Check if characters inputted is in lower case, then print if it is
if user_input == user_input.swapcase().lower():
    print("The string inputted is all in lower case.")

# If it is not, print not in lower case
else:
    print("All or some string inputted is not in lower case.")