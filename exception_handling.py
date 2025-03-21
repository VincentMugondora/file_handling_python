# x = 2
try:
    print(x)
except NameError:
    print("x is not defined")
finally:
    print("Done")

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

# Example
# In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

# Example
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# This can be useful to close objects and clean up resources:

# Example
# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

# Example
# Raise an error and stop the program if x is lower than 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.

# Example
# Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")