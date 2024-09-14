# Chapter 4: Type Casting
# Type casting is the process of converting a variable from one data type to another.
# This chapter demonstrates how to perform type casting between integers, floats, and strings,
# and includes handling edge cases and potential errors.

# Initial variable assignments with different data types
x, y, z = 1, 2.5, '3'  # Assign integer 1 to 'x', float 2.5 to 'y', and string '3' to 'z'

# Print the initial values of the variables
print("Initial values:")
print(f"x: {x}")  # Output: 1
print(f"y: {y}")  # Output: 2.5
print(f"z: {z}")  # Output: 3

# Print the types of the initial variables
print("\nInitial types:")
print(f"type(x): {type(x)}")  # Output: <class 'int'> (x is an integer)
print(f"type(y): {type(y)}")  # Output: <class 'float'> (y is a float)
print(f"type(z): {type(z)}")  # Output: <class 'str'> (z is a string)

# Perform type casting
# Convert 'x' to float, 'y' to integer, and 'z' to integer
x, y, z = float(x), int(y), int(z)

# Print the values after type casting
print("\nAfter type casting:")
print(f"x: {x}")  # Output: 1.0 (x is now a float)
print(f"y: {y}")  # Output: 2 (y is now an integer)
print(f"z: {z}")  # Output: 3 (z is now an integer)

# Print the types of the variables after type casting
print("\nTypes after type casting:")
print(f"type(x): {type(x)}")  # Output: <class 'float'> (x is now a float)
print(f"type(y): {type(y)}")  # Output: <class 'int'> (y is now an integer)
print(f"type(z): {type(z)}")  # Output: <class 'int'> (z is now an integer)

# Convert all variables to strings
x, y, z = str(x), str(y), str(z)

# Print the values after converting to strings
print("\nAfter converting to strings:")
print(f"x: {x}")  # Output: '1.0' (x is now a string)
print(f"y: {y}")  # Output: '2' (y is now a string)
print(f"z: {z}")  # Output: '3' (z is now a string)

# Print the types of the variables after converting to strings
print("\nTypes after converting to strings:")
print(f"type(x): {type(x)}")  # Output: <class 'str'> (x is now a string)
print(f"type(y): {type(y)}")  # Output: <class 'str'> (y is now a string)
print(f"type(z): {type(z)}")  # Output: <class 'str'> (z is now a string)

# Additional Examples

# Handling invalid conversions
print("\nHandling invalid conversions:")
try:
    invalid_int = int('abc')  # Attempt to convert a non-numeric string to an integer
except ValueError as e:
    print(f"Error while casting 'abc' to int: {e}")  # Catch and print the ValueError

# Converting a string with a decimal to an integer
float_string = '123.456'
int_from_float_string = int(float(float_string))  # Convert string to float, then to integer (decimal part is truncated)
print("\nCasting '123.456' to int via float:")
print(f"int_from_float_string: {int_from_float_string}")  # Output: 123

# Converting an integer to a boolean
boolean_value = bool(0)  # Zero is considered False in boolean context
print("\nCasting integer 0 to boolean:")
print(f"boolean_value: {boolean_value}")  # Output: False

# Converting a boolean to an integer
int_from_boolean = int(True)  # True is cast to 1
print("\nCasting boolean True to integer:")
print(f"int_from_boolean: {int_from_boolean}")  # Output: 1
