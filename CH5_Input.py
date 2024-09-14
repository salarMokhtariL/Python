# Chapter 5: The `input()` Function

# Prompt the user to enter their name and store the response in the variable 'user_name'.
# The input() function displays the prompt message and waits for the user to type something and press Enter.
user_name = input("Enter your name: ")  
# Output a personalized greeting using the name provided by the user.
print(f"Hello, {user_name}!")  # The f-string allows embedding the variable 'user_name' directly in the string.

# Prompt the user to enter their age. The input() function returns data as a string, which we then convert to an integer.
age = int(input("Enter your age: "))  
# Output the user's age. The conversion from string to integer allows us to perform numerical operations if needed.
print(f"You are {age} years old.")  # The age variable, now an integer, is embedded into the output string.

# Prompt the user to enter their height. Convert the input string to a float to handle decimal values.
height = float(input("Enter your height in meters: "))  
# Output the user's height. Using float conversion allows for decimal precision in the height measurement.
print(f"Your height is {height} meters.")  # The height variable, now a float, is used in the output string.

# Prompt the user to enter two numbers. Convert both inputs to floats for accurate arithmetic operations.
num1 = float(input("Enter the first number: "))  # Convert the first input to float to support decimal values.
num2 = float(input("Enter the second number: "))  # Convert the second input to float for consistency in arithmetic.
# Calculate the sum of the two numbers. Using float ensures that decimal numbers are accurately summed.
sum_result = num1 + num2  
# Output the result of the addition. The f-string format makes it easy to include variable values in the output.
print(f"The sum of {num1} and {num2} is {sum_result}.")  # Display the result of the addition operation.

# Prompt the user to enter a string. Perform string manipulations to demonstrate string handling capabilities.
user_string = input("Enter a string: ")  
# Convert the user input to uppercase and print it. The .upper() method transforms all characters to uppercase.
print(f"The string in uppercase is {user_string.upper()}.")  
# Convert the user input to lowercase and print it. The .lower() method transforms all characters to lowercase.
print(f"The string in lowercase is {user_string.lower()}.")  

# Example of handling invalid input with try-except to prevent program crashes due to unexpected data types.
try:
    # Prompt the user to enter a number and attempt to convert the input to an integer.
    number = int(input("Enter a number: "))  
    # If conversion is successful, print the entered number.
    print(f"You entered the number {number}.")  
except ValueError:
    # Handle the case where input is not a valid integer and print an error message.
    print("Invalid input! Please enter a valid number.")  # Provide feedback to the user when invalid input is detected.
