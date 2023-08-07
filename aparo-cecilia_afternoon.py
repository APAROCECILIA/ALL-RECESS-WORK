'''file handling in python
Python has several functions for 
creating, reading, updating, and deleting files.
The open() function takes two parameters; filename, and mode



"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

'''
me = open("work.txt")

me = open("work.txt", "r")
print(me.read())
print("am done")


# Read two lines of the file:
h = open("work.txt", "r")
print(h.readline())
print("........................................")
print(h.readline())
h.close()

# Loop through the file line by line:
print("........................................")

z = open("work.txt", "r")
for x in z:
    print(x)

# f = open("give it's path", "r")
# print(f.read())

# f.close() you always have to close the opened file

# Return the 5 first characters of the file:
fopen = open("work.txt", "r")
print(fopen.read(5))


# exception handling;

try:
    file = open("no_file.txt", "w")  # this createsthe file that doesn't exist
    try:
        file.write("This is my test file for exception handling")
    finally:
        print("Going to close the file")
        file.close()
except IOError:
    print("Error: can't find file")

s = open("no_file.txt")

s = open("no_file.txt", "r")
print(s.read())

#The 'finally' block contains code that
# will always be executed,
# regardless of whether an exception
# occurs or not within the “try” block.
