
# Comments in Python begin with a hash mark (#) and set of triple quotes (''').
# The hash mark (#) used to define the Single line comment.
# The Set of Triple Quotes(''') used to define the Multiline Comments. It start and end with the set of triple quotes.
# Inbetween that, you can add any number of lines of comments

# This is a Single line comment


'''
This is a Multiline comment or Docstring.
you can add any number line inbetween the quotes.
It is used to describe the purpose of a function or method.
It can be in Single or Double Quotes.
'''

# Examples

# Block level comment

# This functions is used to add two numbers
# It has two parameters 'a' and 'b'
# You can pass two arguments to the function
# It will return the sum of the two arguments passed

'''
This functions is used to add two numbers
It has two parameters 'a' and 'b'
You can pass two arguments to the function
It will return the sum of the two arguments passed 
'''


def add_numbers(a, b):
    return a + b


print(add_numbers(2, 3))

# Inline Comment


def add_numbers(a, b):
    return a + b  # returning the value


print(add_numbers(2, 3))  # prints the return value of the function
