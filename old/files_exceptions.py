# Reading files
with open('pi.txt') as file_object:
    content = file_object.read()

print(content.upper())
print(type(content))


# Writing to an Empty File
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. \n")


# Appending to a File
with open(filename, 'a') as file_object:
    file_object.write("I love programming.")


# Exceptions
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero")

# Handling the FileNotFoundError Exception
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")