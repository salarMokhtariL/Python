'''
Chapter 1: Variable and Type casting
A variable in Python is a symbolic name that refers to an object, value, or data in memory. It's a placeholder used to store and manipulate data throughout a program.
    String
    Integer
    Float
    Boolean
'''

# String

first_name = 'XXX'
last_name = 'YYY'
fulname = first_name + ' ' + last_name

print(f'hello {fulname}')
print(type(fulname))


# Integer 

age = 20
age += 5 # age = age + 5 ------------ 20 + 5 
print(f'your age is {age}')
print(type(age))


# Float 

height = 178.5
height -= 5
print(f'your height is {height} cm')
print(type(height))


# Boolean: False, True 

is_student = True
human = False

print(f'you are student? {is_student}')
print(type(is_student))