# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

f = open("dummy.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("dummy.txt", "r")
print(f.read())


f = open("dummy.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())