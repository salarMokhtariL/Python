# Chapter 1: Variables and Type Casting
# In Python, a variable is a symbolic name that refers to a value or data stored in memory.
# Variables act as placeholders for data and allow us to manipulate this data throughout our program.
# This chapter covers four fundamental data types:
#    - String: A sequence of characters
#    - Integer: Whole numbers
#    - Float: Decimal numbers
#    - Boolean: True or False values

# String Example
first_name = 'XXX'         # Assign the string 'XXX' to the variable 'first_name'
last_name = 'YYY'          # Assign the string 'YYY' to the variable 'last_name'
fulname = first_name + ' ' + last_name  # Concatenate 'first_name' and 'last_name' with a space in between

print(f'hello {fulname}')   # Output a greeting message with the full name using an f-string for formatting
print(type(fulname))        # Output the type of 'fulname' to confirm it's a string (Expected output: <class 'str'>)

# Integer Example
age = 20                   # Assign the integer value 20 to the variable 'age'
age += 5                   # Increase the value of 'age' by 5 (This is the same as 'age = age + 5')
# After this operation, 'age' will be 25

print(f'your age is {age}') # Output the updated age using an f-string for formatting
print(type(age))            # Output the type of 'age' to confirm it's an integer (Expected output: <class 'int'>)

# Float Example
height = 178.5             # Assign the floating-point number 178.5 to the variable 'height'
height -= 5                # Decrease the value of 'height' by 5 (This is the same as 'height = height - 5')
# After this operation, 'height' will be 173.5

print(f'your height is {height} cm')  # Output the updated height with a unit using an f-string for formatting
print(type(height))        # Output the type of 'height' to confirm it's a float (Expected output: <class 'float'>)

# Boolean Example
is_student = True          # Assign the boolean value True to the variable 'is_student'
human = False              # Assign the boolean value False to the variable 'human'

print(f'you are student? {is_student}') # Output whether the person is a student using an f-string for formatting
print(type(is_student))    # Output the type of 'is_student' to confirm it's a boolean (Expected output: <class 'bool'>)
