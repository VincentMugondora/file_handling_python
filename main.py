# name = "sama"

# print(type(name))

# integer types

# number_of_pupils = 40
# print(number_of_pupils)
# print(type(number_of_pupils))

# float types

# number_of_pupils = 0.0
# print(number_of_pupils)
# print(type(number_of_pupils))

# x = 15
# y = 5
# print(f"Addition {x + y}")
# print(f"Subtraction {x - y}")
# print(f"Multiplication {x * y}")
# print(f"Division {x / y}") # float division
# print(f"integer division {x // y}")
# print(f"modulus {x % y}")
# print(f"expo or power of {x ** y}")

# operators
# +, -, *, /, //, %, **

# num = 5_000_000
# print(num)

# boolean => it returns True or False

# comparison operators

#  == means eaqual to
# != means not equal to
# > means greater than
# < means less than
# >= means greater than or equal to
# <= means less than or equal to

# print(10 > 5)
# print(7 <= 7)

# lists is a collection of items that is used to store multiple items in a single variable
# lists are ordered, changeable and indexed
# lists are denoted by square brackets []
# lists are mutable
# lists are ordered collection of items

fruits = ["apple", "banana", "cherry", "orange", "mango"]
numbers = [10, 9, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [100, 0, 20]
mixed_list = [True, 1, 2.0, "sama", [1, 2, 3]]

# print(fruits)
# print(numbers)
# print(mixed_list)

# accessing items in a list
# indexing => we use a positive index and a negative index to access items in a list
# positive index => starts from 0 (this is the first item)

print(fruits[0])  
print(fruits[-1])  

# list slicing
# list[start:end]

NUMBERS = [10, 20, 30, 40, 50]

print(NUMBERS[1:-3])
print(NUMBERS[-3])

# changing items in a list
NUMBERS[0] = 5
print(NUMBERS)