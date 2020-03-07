'''
Variables are containers for storing data values.
Unlike other programming languages, Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
Variables do not need to be declared with any particular type and can even change type after they have been set.
'''

'''
RULES TO  DEFINE VARIABLES
-A variable name must start with a letter or an underscore
-A variable name cannot start with a number. But, it can have a number
-A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
-Variable names are case-sensitive (one, One and ONE are three different variables)
'''

# Variable Types
# Assigning Values to variables
a = 3                # Integer
b = 3.5              # Float
name = "Muniyandi"   # String
is_submitted = True  # Boolean, First letter should be always Capital(True/False)

print(a)  # prints - 3
print(name)  # prints - Muniyandi
print(a, b, name)  # prints - 3 3.5 Muniyandi

# Assigning multiple values to multiple variables in a single line
a, b, name, is_submitted = (3, 3.5, "Muniyandi", True)

print(a)  # prints - 3
print(name)  # prints - Muniyandi
print(a, b, name)  # prints - 3 3.5 Muniyandi

# Basic Math
sum = a + b  # add
print(sum)  # prints - 6.5

subtract = a - b  # subtract
print(subtract)  # prints - -0.5

multiplication = a * b  # multiplication
print(multiplication)  # prints - 10.5

division = a / 2  # division
print(division)  # prints - 1.5

fd = a // 2  # Floor Division, The result will be rounded to the nearest interger. It won't allow float
print(fd)  # Prints - 1

exp = a ** 3  # Exponential Operator
print(exp)  # prints - 27

mod = a % 2  # Modulo Operator
print(mod)  # prints - 1

# Casting
x = 1.5
y = 2
z = "3"

print(x + y)  # prints - 3.5
print(int(x) + y)  # prints - 3
print(y + z)  # prints - TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(y + int(z))  # prints - 5
print((y) + float(z))  # prints - 5.0
print(str(x) + y)  # prints - TypeError: must be str, not int
print(str(x) + z)  # prints - 1.53
