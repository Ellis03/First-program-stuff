#This code prints out in the terminal that "Hello world is cool!"
print ("Hello world is cool!")

# This is a single line comment in Python

# print("TASK 1")

# print("Hello")
# print("World")
# print("with Comments")
x = 12 + 5
print (x)
print(type(x))

x = 5+3.0
print (x)
print(type(x))

x = 12/5
print(x)
print(type(x))

x= 12 + 5 == 5 * 3.0
print(x)
print(type(x))

# You need to fix the following lines
# Run the code and then use the error messages to fix each line

# This line has a SyntaxError
print("hello world")

# This line has a NameError
print("Hello World!")

# The following lines cause a TypeError
int1 = 100
str1 = 10
print(int1 / str1)

# This line is not indented properly. Fix this
print ("Indentation matters in Python")

# You will notice that we have blank lines
# Python doesn't care about these!

# There is extra whitespace inside the print statement 
# Python doesn't care about this
print ("Hello World!")

name = input("Hello, what is your name?\n")
age = input("What is your age?\n")
print(f"Hello {name}, your age is {age}.")