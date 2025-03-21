# 1. Create three variables:

# name (a string)
# age (an integer)
# height (a float) 



# 2. Given a = 15 and b = 4, calculate and print the results of:

# Addition
# Subtraction
# Multiplication
# Division
# Integer division
# Modulus
# Exponentiation



# 3. create a list of 5 elements and print the 3rd element
# print from the 2nd element to the 4th element
# change the value of the first element
# add a new element to the list
# remove the last element of the list
# clear the list
# delete the the list





# 4. Create a dictionary with the following keys and values:    name: "John", age: 30, isStudent: False
# print the dictionary
# print the value of the age key
# change the value of the name key
# add a new key value pair: isAdult: True
# remove the isStudent key

# father = "foden"
# mother="Halaand"
# print(f"my mother is {mother}and my father is {father}")

f = open("main.py", "rt")
print(f.read())

f.close()

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Example
# Return the 5 first characters of the file:
print()
print("Reading Five first characters")
f = open("main.py", "r")
print(f.read(5))


print()
# Read Lines
# You can return one line by using the readline() method:

# Example
# Read one line of the file:
print("Read one line of the file:")
f = open("main.py", "r")
print(f.readline())

print()
# By calling readline() two times, you can read the two first lines:

# Example
# Read two lines of the file:
print("Read two lines of the file:")
f = open("main.py", "r")
print(f.readline())
print(f.readline())