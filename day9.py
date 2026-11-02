# Functions

# Function is a block of code that performs a specific task
# Function helps in code reusability, reduces code repetation
# Function makes our code structured

# To define a function we use def keyword
# syntax:
# def function_name(parameters):
#     block of code

# Parameters are the variables that receives the value for the function
age = 27

def sub(a,b):
    name = "Ujjwal Neupane"
    print(name)
    print(a-b)
    print(age)

# By only defining the function doesnot works, we need to call the function
# To call a function, function_name(arguments)
# Arguments are the values passed to the function

sub(b=5,a=7)

# print(a)
# print(b)
# print(name)
print(age)
# Positional Arguments
# The parameter receives the value according to the position

# Keyword Arguments
# The arguments passed in key=value pair, is called keyword arguments
# key should be the parameters


# Local Variable => The variable defined inside the function is local variable
# can be accessed from inside the function only

# GLobal Variable => The variable defined outside the function is global variable
# Can be accessed from anywhere, either from inside the function or from outside the function

# DRY => Dont Repeat Yourself

# Task: Update calculator program and login register program using function

# Login Register Program
# Register flow:
# Ask username and password from user
# Convert them into dictionary
# Append the dictionary in the list

# Login FLow:
# Ask usernane and password from user
# Loop in the list of dictationary
# Check if username == username and dict.get(username) == password

credentials = []

def operation(method):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if method == 'register':
        # register code
        dict_cred = {username:password}
        credentials.append(dict_cred)
        print("Registration successfull")
    else:
        for cred in credentials:
            if username == username and cred.get(username) == password:
                print("Login SUccessfull")
                break
        else:
            print("Login Failed")
        # login code

while True:
    choice = input("Enter 1 for register, 2 for login, 3 for exit: ")
    match choice:
        case '1':
            operation('register')
        case '2':
            operation('login')
        case '3':
            print("Thank you")
            break
        case _:
            print("Invalid Input")