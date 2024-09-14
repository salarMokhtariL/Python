'''
Chapter 3 : String Methods 
'''

# Define a string with mixed case and spaces
name = 'AbCd abcd ABCD'

# Print the length of the string (number of characters including spaces)
print(len(name))  # Output: 14

# Find the index of the first occurrence of 'C' in the string
print(name.find('C'))  # Output: 2

# Capitalize the first character and make all other characters lowercase
print(name.capitalize())  # Output: "Abcd abcd abcd"

# Convert the entire string to uppercase
print(name.upper())  # Output: "ABCD ABCD ABCD"

# Convert the entire string to lowercase
print(name.lower())  # Output: "abcd abcd abcd"

# Check if the string contains only digits (should return False since it's alphabetic)
print(name.isdigit())  # Output: False

# Check if the string contains only alphabetic characters (returns False due to space)
print(name.isalpha())  # Output: False

# Count the occurrences of the character 'C' in the string
print(name.count('C'))  # Output: 2

# Replace all occurrences of 'A' with 'Z'
print(name.replace('A', 'Z'))  # Output: "ZbCd abcd ZBCD"

# Repeat the string 4 times and print the result
print(name * 4)  # Output: "AbCd abcd ABCDAbCd abcd ABCDAbCd abcd ABCDAbCd abcd ABCD"
