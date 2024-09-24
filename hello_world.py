# #This code prints out in the terminal that "Hello world is cool!"
# print ("Hello world is cool!")

# # This is a single line comment in Python

# # print("TASK 1")

# # print("Hello")
# # print("World")
# # print("with Comments")
# x = 12 + 5
# print (x)
# print(type(x))

# x = 5+3.0
# print (x)
# print(type(x))

# x = 12/5
# print(x)
# print(type(x))

# x= 12 + 5 == 5 * 3.0
# print(x)
# print(type(x))

# # You need to fix the following lines
# # Run the code and then use the error messages to fix each line

# # This line has a SyntaxError
# print("hello world")

# # This line has a NameError
# print("Hello World!")

# # The following lines cause a TypeError
# int1 = 100
# str1 = 10
# print(int1 / str1)

# # This line is not indented properly. Fix this
# print ("Indentation matters in Python")

# # You will notice that we have blank lines
# # Python doesn't care about these!

# # There is extra whitespace inside the print statement 
# # Python doesn't care about this
# print ("Hello World!")

# #Input function which asks for the user to enter their name into the terminal
# name = input("Hello, what is your name?\n")
# age = input("What is your age?\n")
# print(f"Hello {name}, your age is {age}.")

# #more on input function
# input("Please enter something:\n")

# input_string = input("Please enter something:\n")
# print(f"You entered - {input_string}")

# input_string = input("Please enter a number:\n")
# #Using int will convert the string into an int as anything inputted by the user will automatically be a string
# x = int(input_string)
# #Adds 5 to the user input and prints the calculation and total
# print(f"{x} + 5 = {x+5}")

#Tries the code and handles an exception when data from another data type is entered
try:
    x = int(input("please enter a number:\n"))
except:
    print ("You have not entered a number, please try again.")
    x = int(input("please enter a number:\n"))
if x <= 0:
    print (f"Number entered needs to be more than 0")
elif x >= 15:
    print("Number entered needs to be less than 15")
else:
#F string used when you need to put the value of a variable into a string
#Whereas without the f string, the variable inside curly brackets will be counted in the string rather than as a variable and show the value inside it instead.
    print (f"{x} * 10 = {x*10}")

