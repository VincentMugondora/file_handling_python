# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

f = open("new_file.txt", "x")
f.close()
# The code snippet creates a new file called new_file.txt. If the file already exists, the code will raise an error.