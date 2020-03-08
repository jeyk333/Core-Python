# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# Allow duplicate values

# Different ways to create a list
nums1 = [1, 2, 3, 4, 5] 
nums2 = list((1, 2, 3, 4, 5)) # Using constructor

print(nums1) # prints - [1, 2, 3, 4, 5]
print(nums2) # prints - [1, 2, 3, 4, 5]

numbers = ["one", "two", "three", "four", "five"]

# To Get a single value
print(numbers[2]) # prints - three

# To Get length
print(len(numbers)) # prints - 5

# To append to list
numbers.append("six")
print(numbers) # prints - ['one', 'two', 'three', 'four', 'five', 'six']

# To Remove from list
numbers.remove("three")
print(numbers) # prints - ['one', 'two', 'four', 'five', 'six']

# To add into particular position
numbers.insert(3, "eight")
print(numbers) # prints - ['one', 'two', 'four', 'eight', 'five', 'six']

# To replace
numbers[1] = "ten"
print(numbers) # prints - ['one', 'ten', 'four', 'eight', 'five', 'six']

# To remove by index
numbers.pop(3)
print(numbers) # prints - ['one', 'ten', 'four', 'five', 'six']

# To reverse list
numbers.reverse()
print(numbers) # prints - ['six', 'five', 'four', 'ten', 'one']

# To sort
numbers.sort()
print(numbers) # prints - ['five', 'four', 'one', 'six', 'ten']

# Slicing
print(numbers[2:4]) # prints - ['one', 'six']

# To Copy list
new_nums = numbers.copy()
new_nums2 = list(numbers)
print(new_nums) # prints - ['five', 'four', 'one', 'six', 'ten']
print(new_nums2) # prints - ['five', 'four', 'one', 'six', 'ten']


# To loop through lists
for n in numbers:
    print(n) 

'''
The above loop prints - 
five
four
one
six
ten
'''

# To clear a list
numbers.clear()
print(numbers) # prints - []

# To delete a list
del numbers
# print(numbers) # prints - NameError: name 'numbers' is not defined

# To join two lists
new_list = new_nums + new_nums2
print(new_list) # prints - ['five', 'four', 'one', 'six', 'ten', 'five', 'four', 'one', 'six', 'ten']
num_list = [1, 2, 3]
new_list.extend(num_list) # Usind extend() method
print(new_list) # prints - ['five', 'four', 'one', 'six', 'ten', 'five', 'four', 'one', 'six', 'ten', 1, 2, 3]








