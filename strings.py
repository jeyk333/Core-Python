# Strings in python are surrounded by either Single quotes or Double quotes

name = 'Muniyandi'
age = 35

# To Concatinate or Combine two or more Variables

print('I am ' + name)  # prints - I am Muniyandi

# print('I am ' + name + '. My age is ' + age) # prints - TypeError: must be str, not int
print('I am ' + name + '. My age is ' + str(age)) # prints - I am Muniyandi. My age is 35
 
# Using format() Method
print('I am {name}. My age is {age}'.format(name=name, age=age)) # prints - I am Muniyandi. My age is 35

# Using F-Strings (To use this, the Python version should be 3.6+)
print(f'I am {name}. My age is {age}')  # prints - I am Muniyandi. My age is 35

# String Methods
a = "i Love python"

# To Capitalize String
print(a.capitalize()) # prints - I love python

# To Make all Uppercase
print(a.upper()) # prints - I LOVE PYTHON

# To Make all Lowercase
print(a.lower()) # prints - i love python

# To Swap case
print(a.swapcase()) # prints - I lOVE PYTHON

# To Get Length
print(len(a)) # prints - 13

# To Replace
print(a.replace('Love', 'Like')) # prints - i Like python

# To Count
print(a.count('o')) # prints - 2

# Starts with
print(a.startswith('i')) # prints - True
print(a.startswith('e')) # prints - False

# Ends with
print(a.endswith('n')) # prints - True
print(a.endswith('e')) # prints - False

# To Split into a List
print(a.split()) # prints - ['i', 'Love', 'python']

# To Find Index Position
print(a.find('L')) # prints - 2

# Is all alphanumberic
print(a.isalnum()) # prints - False (Due to space between sentences, it shows False. Else, It will show True)

# Is all alphabetic
print(a.isalpha()) # prints - False (Due to space between sentences, it shows False. Else, It will show True)

# Is all numeric
print(a.isnumeric()) # prints - False

# Strings are like Arrays/Lists
print(a[3]) # prints - o

# Slicing
print(a[2:6]) # prints - Love
print(a[2:]) # prints - Love python
print(a[:6]) # prints - i Love
print(a[-6: -2]) # prints - pyth

# To Remove unwanted spaces from the start and end of the string
c = " Hello "
print(c.strip()) # prints - Hello (Without spaces)

# To Check String
print('Lov' in a) # prints - True
print('lov' in a) # prints - False (Case Sensitive)
print('Lov' not in a) # prints - False
print('lov' not in a) # prints - True (Case Sensitive)





