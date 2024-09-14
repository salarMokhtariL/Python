# Chapter 2: Multiple Assignment
# Python allows for multiple assignment, which lets you assign values to several variables in one line.
# This feature can help simplify code and improve readability.

# Single assignments to individual variables
name = 'XXX'          # Set 'name' to 'XXX'
age = 25              # Set 'age' to 25
attractive = True     # Set 'attractive' to True

# Display the values of the individual variables
print(name)           # Output: XXX
print(age)            # Output: 25
print(attractive)     # Output: True

# Multiple assignment in one line
Mname, Mage, Mattractive = 'YYY', 24, False

# Display the values of the variables after multiple assignment
print(Mname)          # Output: YYY
print(Mage)           # Output: 24
print(Mattractive)    # Output: False

# Multiple individual assignments with the same value
A = 1
B = 1
C = 1
D = 1

# Display the values of each variable
print(A)              # Output: 1
print(B)              # Output: 1
print(C)              # Output: 1
print(D)              # Output: 1

# Multiple assignment with the same value in one line
A_1 = B_1 = C_1 = D_1 = 1

# Display the values of these variables
print(A_1)            # Output: 1
print(B_1)            # Output: 1
print(C_1)            # Output: 1
print(D_1)            # Output: 1
